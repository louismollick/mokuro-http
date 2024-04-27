# Mokuro with HTTP API

## Usage

```
curl http://127.0.0.1:8000/?src=https://www.mokuro.moe/manga/Dorohedoro/Dorohedoro%20v01/DH_01%20016.JPG
```

## Local development setup

1. `python -m venv venv`
2. `source venv/bin/activate`
3. `pip install --upgrade -r requirements.txt -r comic_text_detector/requirements.txt`
4. `flask run --port 8000 --debug` or `gunicorn --bind localhost:8000 app:app`

## Build docker image

1. `docker build -t mokuro .`
2. `docker run -p 8000:8000 -w /app -v "$(pwd):/app" mokuro`