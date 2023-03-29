FROM python:3.10

WORKDIR /app/

COPY . .

RUN pip install --user --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]