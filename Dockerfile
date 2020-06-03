FROM python:2.7

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip \
      && pip install -r requirements.txt

EXPOSE 6000

CMD ["python", "main.py"]
