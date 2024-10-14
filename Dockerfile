FROM python

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./main /app/main

EXPOSE 8000

CMD ["python", "-m", "app/main"]
