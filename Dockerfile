FROM python:3

WORKDIR /app

COPY . .

RUN pip3 install -r requirement.txt

CMD ["python3","./main.py"]