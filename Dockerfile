FROM python:3.9
WORKDIR /opt/connect4
COPY . .
CMD python3 main.py