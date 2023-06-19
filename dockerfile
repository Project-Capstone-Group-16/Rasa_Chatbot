FROM python:3.7-slim

RUN python -m pip install rasa && python -m pip install json

WORKDIR /app
ENV HOME=/app
COPY . .

RUN rasa train nlu

USER 1001

ENTRYPOINT ["rasa"]

CMD ["run", "--enable-api", "--port", "8080"]