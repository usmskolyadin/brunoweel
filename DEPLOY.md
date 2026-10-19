# Деплой на Timeweb Cloud (облачный сервер)

Домен `brunoweel.ru` зарегистрирован на Timeweb. Ниже — деплой на **облачный
сервер** (VPS с root-доступом), а не на shared-хостинг: Ubuntu 24.04,
nginx как reverse proxy и gunicorn как systemd-сервис, без Apache/mod_wsgi.

Что уже подготовлено в репозитории:

- [doghotel/settings.py](doghotel/settings.py) — `SECRET_KEY`, `DEBUG`,
  `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` берутся из `.env`; добавлен
  `SECURE_PROXY_SSL_HEADER`, чтобы Django понимал, что nginx отдал запрос
  по HTTPS.
- [.env.example](.env.example) — шаблон продакшен-переменных.
- [requirements.txt](requirements.txt) — добавлен `gunicorn`.
- [deploy/gunicorn.service](deploy/gunicorn.service) — systemd-юнит для
  gunicorn.
- [deploy/nginx.conf](deploy/nginx.conf) — конфиг сайта для nginx
  (статика, медиа, прокси на gunicorn).
- [deploy/deploy.sh](deploy/deploy.sh) — скрипт повторного деплоя
  (`git pull` → сборка CSS → миграции → collectstatic → restart).

---

## 0. Первоначальная настройка нового облачного сервера

Выполняется один раз сразу после создания сервера в панели Timeweb Cloud
(рекомендуемый образ — **Ubuntu 24.04 LTS**; минимального тарифа 1 CPU /
1 GB RAM для этого сайта достаточно).

### 0.1. Первый вход и создание рабочего пользователя

Timeweb даёт root-пароль по почте/в панели. Заходим под root и сразу
создаём обычного пользователя — работать и разворачивать проект под root
не нужно:

```bash
ssh root@<IP_сервера>

apt update && apt upgrade -y

adduser brunoweel
usermod -aG sudo brunoweel
```

Скопировать свой SSH-ключ на нового пользователя (с локальной машины):

```bash
ssh-copy-id brunoweel@<IP_сервера>
# если ssh-copy-id недоступен (Windows) — вручную добавить публичный ключ
# в /home/brunoweel/.ssh/authorized_keys на сервере
```

Проверить, что входит по ключу без пароля (`ssh brunoweel@<IP_сервера>`),
и только после этого отключить вход под root и по паролю:

```bash
sudo nano /etc/ssh/sshd_config
# PermitRootLogin no
# PasswordAuthentication no
sudo systemctl restart ssh
```

### 0.2. Базовая защита

```bash
sudo apt install -y ufw fail2ban
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable

sudo timedatectl set-timezone Europe/Moscow
```

Если тариф с 1 GB RAM — добавить swap, иначе `pip install`/сборка CSS
могут падать по памяти:

```bash
sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

### 0.3. Системные пакеты

```bash
sudo apt install -y python3 python3-venv python3-pip git nginx certbot python3-certbot-nginx
```

Node.js (нужен только для сборки Tailwind CSS):

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

### 0.4. DNS

В панели Timeweb (раздел «Домены» → `brunoweel.ru` → DNS) указать
A-записи `brunoweel.ru` и `www.brunoweel.ru` на IP нового облачного
сервера (вместо старого shared-хостинга).

Дальше всё выполняется от имени пользователя `brunoweel` (`su - brunoweel`
или новая SSH-сессия).

---

## 1. Клонирование и настройка проекта

```bash
cd ~
git clone https://github.com/usmskolyadin/brunoweel.git brunoweel.ru
cd brunoweel.ru

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

npm ci
npm run build:css
```

Настроить `.env`:

```bash
cp .env.example .env
nano .env
```

```
DJANGO_SECRET_KEY=<сгенерировать, см. ниже>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=brunoweel.ru,www.brunoweel.ru
DJANGO_CSRF_TRUSTED_ORIGINS=http://brunoweel.ru,http://www.brunoweel.ru,https://brunoweel.ru,https://www.brunoweel.ru
DJANGO_SECURE_SSL_REDIRECT=False
```

Сгенерировать `SECRET_KEY`:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Накатить миграции, собрать статику, создать администратора:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

```bash
deactivate
```

---

## 2. Gunicorn как systemd-сервис

```bash
sudo cp ~/brunoweel.ru/deploy/gunicorn.service /etc/systemd/system/gunicorn.service
sudo systemctl daemon-reload
sudo systemctl enable --now gunicorn
sudo systemctl status gunicorn
```

Сервис запускает `gunicorn` от пользователя `brunoweel`, слушает
`127.0.0.1:8001` и читает переменные из `.env` сам (через `python-dotenv`
в `settings.py`), отдельный `EnvironmentFile` не нужен.

---

## 3. nginx

```bash
sudo cp ~/brunoweel.ru/deploy/nginx.conf /etc/nginx/sites-available/brunoweel.ru
sudo ln -s /etc/nginx/sites-available/brunoweel.ru /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

sudo nginx -t
sudo systemctl reload nginx
```

На этом шаге сайт должен уже открываться по `http://brunoweel.ru`.

---

## 4. SSL (Let's Encrypt)

```bash
sudo certbot --nginx -d brunoweel.ru -d www.brunoweel.ru
```

Certbot сам допишет в `/etc/nginx/sites-available/brunoweel.ru` блок с
`listen 443 ssl` и редирект с 80 на 443, настроит автопродление
(systemd-таймер `certbot.timer`, он включается установкой пакета).

После этого включить строгие cookie/редирект в `.env`:

```bash
nano ~/brunoweel.ru/.env
# DJANGO_SECURE_SSL_REDIRECT=True
sudo systemctl restart gunicorn
```

---

## 5. Повторный деплой (обновления)

После `git push` в `main` на локальной машине — на сервере:

```bash
cd ~/brunoweel.ru
./deploy/deploy.sh
```

Скрипт делает `git pull`, пересобирает CSS, ставит зависимости, гоняет
миграции, `collectstatic` и перезапускает `gunicorn`.

---

## Полезные команды

```bash
sudo systemctl status gunicorn        # статус приложения
sudo journalctl -u gunicorn -f        # логи gunicorn (stdout/stderr)
tail -f ~/brunoweel.ru/gunicorn-error.log
sudo systemctl status nginx
sudo nginx -t                         # проверка конфига перед reload
sudo certbot renew --dry-run          # проверка автопродления SSL
```

## Нюансы

- **База данных** — SQLite (`db.sqlite3` в корне проекта), не в git.
  Для такого размера сайта (одна витрина + админка) этого достаточно;
  бэкапить — просто скопировать файл.
- **Медиа** (загруженные через админку фото) — лежат в `media/` на
  сервере, тоже не в git. При переезде/масштабировании не забыть их
  забэкапить отдельно от репозитория.
- **Статика** собирается в `staticfiles/` командой `collectstatic` и
  отдаётся nginx напрямую (а не через Django/gunicorn) — см. `location
  /static/` в [deploy/nginx.conf](deploy/nginx.conf).
