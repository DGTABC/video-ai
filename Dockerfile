FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg

CMD ["gunicorn", "-b", "0.0.0.0:3000", "app:app"]
