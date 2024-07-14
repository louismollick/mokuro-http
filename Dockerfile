FROM python:3.10
RUN apt-get update && apt-get -y install cmake ffmpeg libsm6 libxext6
WORKDIR /app
COPY ./requirements.txt requirements.txt
COPY ./comic_text_detector/requirements.txt requirements_comic_text_detector.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt -r requirements_comic_text_detector.txt
COPY . .

EXPOSE 3001
ENV PORT 3001

CMD celery -A mokuro.worker worker --loglevel INFO --pool threads -Q mokuro
# CMD gunicorn --bind 0.0.0.0:$PORT mokuro.http_api:app