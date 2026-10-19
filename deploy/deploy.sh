#!/usr/bin/env bash
# Повторный деплой: запускать на сервере из ~/brunoweel.ru после `git pull`
# или просто вызвать `./deploy/deploy.sh`, он сам подтянет обновления.
set -euo pipefail
cd "$(dirname "$0")/.."

git pull

npm ci
npm run build:css

source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
deactivate

sudo systemctl restart gunicorn
