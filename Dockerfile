FROM python:3.12

RUN pip install -q -U google-generativeai

WORKDIR /gemini

CMD [ "tail", "-f", "/dev/null" ]
