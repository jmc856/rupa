FROM python:3.10.0-slim

WORKDIR /rupa

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]