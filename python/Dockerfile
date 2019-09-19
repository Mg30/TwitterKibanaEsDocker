FROM python:3.7
RUN apt-get update
COPY /file/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY /file/adaptaters.py ./
COPY /file/main.py ./
COPY /file/twitterListener.py ./
COPY /file/pipelines.py ./
COPY /file/tweetAnalyser.py ./



