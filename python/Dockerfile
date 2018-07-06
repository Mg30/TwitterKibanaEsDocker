FROM python:3.6
RUN apt-get update
COPY /file/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY /file/ElasticApi.py ./
COPY /file/Main.py ./
COPY /file/Settings.py ./



