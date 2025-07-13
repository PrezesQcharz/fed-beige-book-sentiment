FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV OPENAI_API_KEY=""
ENV EMAIL_HOST=""
ENV EMAIL_PORT=465
ENV EMAIL_HOST_USER=""
ENV EMAIL_HOST_PASSWORD=""
ENV RECIPIENTS=""

CMD ["python", "main.py"]
