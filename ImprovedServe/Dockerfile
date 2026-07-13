
FROM python:3.12.0

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn","main:app","--host", "0.0.0.0", "--port", "8000"]

# defining this host and ip is necessary otherwise by default ip port could be accessed from 
# inside the container only