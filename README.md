# de-project-bibip

Установка виртуального пространства для разарботки

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Если вы не сталкивались с докером, просто проигнорируйте файлы `Dockerfile` и `docker-compose.yml`. Вы еще познакомитесь с докером, дальше на курсе.

Если вы предпочитаете разрабатывать в докере, то вам нужно выполнить следующие команды:
```bash
cd de-project-bibip
docker compose up -d --build
```

После завершения работы остановите контейнер:
```bash
docker compose down -v
```

