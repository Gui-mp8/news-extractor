FROM python:3.10

WORKDIR /app

COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS="./news-extraction.json"

RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements-prod.txt

CMD ["python3", "src/main.py"]