FROM python:latest

WORKDIR /usr/app
COPY requirements.txt /usr/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY src /usr/app/src

CMD ["python", "src/app.py"]
