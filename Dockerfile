FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY main .

EXPOSE 8000

CMD ["python", "-m", "main"]
