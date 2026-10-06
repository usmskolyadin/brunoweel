# Деплой на Timeweb Hosting (shared, Apache + mod_wsgi)

Домен `brunoweel.ru` уже зарегистрирован на Timeweb. Хостинг — classic shared
(hosting.timeweb.ru), без root-доступа: Python-приложения там обслуживает
Apache через `mod_wsgi`, а не gunicorn/Passenger.

## Что уже подготовлено в репозитории

- [doghotel/settings.py](doghotel/settings.py) — `SECRET_KEY`, `DEBUG`,
  `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` берутся из `.env` (через
  `python-dotenv`), а не хардкодятся. Без `.env` локально поведение как
  раньше (`DEBUG=True`, `localhost`).
- `.env.example` — шаблон продакшен-переменных, на сервере скопировать в
  `.env` и заполнить реальными значениями.
- [wsgi.py](wsgi.py) (корень проекта) — точка входа для Apache/mod_wsgi:
  активирует venv и запускает `doghotel.wsgi`. Путь `~/brunoweel.ru`
  зашит внутри — это стандартная для Timeweb структура каталогов
  (совпадает с именем сайта/домена в панели).
- [.htaccess](.htaccess) (корень проекта) — перенаправляет все запросы на
  `wsgi.py`.
- [requirements.txt](requirements.txt) — `Django`, `python-dotenv`.
  `gunicorn` не нужен — на этом хостинге процесс обслуживает сам Apache.

## Шаги

1. **Тариф с SSH.** Нужен доступ по SSH для `virtualenv`/`pip install`.
   Если на текущем тарифе SSH нет — включить в панели или сменить тариф.

2. **Создать сайт на домен.** В разделе «Сайты» панели создать сайт на
   `brunoweel.ru`, если ещё не создан — Timeweb сам создаёт структуру
   `~/brunoweel.ru/public_html`. Домен привязать к этому сайту/тарифу в
   разделе «Домены» (DNS обычно уже настроен, т.к. домен зарегистрирован
   там же).

3. **Собрать Tailwind CSS локально** (на хостинге Node может не быть):
   ```powershell
   npm run build:css
   ```

4. **Подключиться по SSH и создать venv** (Python 3.10 / Ubuntu 22.04 у
   Timeweb):
   ```bash
   cd ~/brunoweel.ru
   wget https://bootstrap.pypa.io/virtualenv/3.10/virtualenv.pyz
   python3 virtualenv.pyz venv
   source venv/bin/activate
   ```

5. **Залить проект** по SFTP/SCP в `~/brunoweel.ru/public_html` — всё
   содержимое репозитория, **кроме** `.venv`, `node_modules`,
   `__pycache__`, `db.sqlite3` (её пересоздать миграциями на сервере).

6. **Установить зависимости и накатить миграции:**
   ```bash
   pip install -r public_html/requirements.txt
   cd public_html
   cp .env.example .env
   nano .env   # реальный SECRET_KEY, DEBUG=False,
               # ALLOWED_HOSTS=brunoweel.ru,www.brunoweel.ru
   python manage.py migrate
   python manage.py createsuperuser
   ```

7. **Если Django требует более новый SQLite** («SQLite 3.31 or later is
   required») — на Python 3.10/Ubuntu 22.04 обычно не возникает; если
   всё же появится, нужен костыль с `pysqlite3` (см. официальную доку
   Timeweb по Django, ссылка ниже).

8. **Перезапустить приложение** — mod_wsgi подхватывает изменения по
   времени модификации `wsgi.py`:
   ```bash
   touch public_html/wsgi.py
   ```

9. **Включить SSL.** В разделе SSL-сертификатов панели подключить
   бесплатный Let's Encrypt для `brunoweel.ru` и `www.brunoweel.ru`.
   После этого в `.env` прописать:
   ```
   DJANGO_CSRF_TRUSTED_ORIGINS=https://brunoweel.ru,https://www.brunoweel.ru
   ```

## Нюансы

- **Статика:** `/static/...` отдаётся Apache напрямую из папки `static/`
  (правило `!-f` в `.htaccess`) — `collectstatic` для своих css/js не
  нужен.
- **Админка Django (`/admin/`)** будет работать, но без своих стилей —
  её статика не собрана. Если нужна красивая админка, потребуется
  отдельно настроить `collectstatic` + `Alias` в `.htaccess`.

## Источники

- [Размещение Django-проекта на хостинге — timeweb.com](https://timeweb.com/ru/docs/virtualnyj-hosting/prilozheniya-i-frejmvorki/django/)
- [Установка virtualenv для Python-проекта — timeweb.com](https://timeweb.com/ru/docs/virtualnyj-hosting/prilozheniya-i-frejmvorki/python-ustanovka-virtualenv/)
