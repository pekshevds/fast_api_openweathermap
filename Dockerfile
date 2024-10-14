FROM python
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./main ./main

EXPOSE 8000

CMD ["python", "-m", "main"]
