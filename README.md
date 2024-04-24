# Mokuro with REST API

## Local development setup

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install --upgrade -r requirements.txt -r comic_text_detector/requirements.txt`
4. `flask run --port 8000 --debug` or `gunicorn --bind localhost:8000 app:app`

## Build docker image

1. `docker build -t mokuro .`
2. `docker run -p 8000:8000 -w /app -v "$(pwd):/app" mokuro`