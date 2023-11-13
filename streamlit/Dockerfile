FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY ui.py /app
COPY background.jpg /app

EXPOSE 80

ENTRYPOINT ["streamlit", "run", "ui.py", "--server.port", "80"]