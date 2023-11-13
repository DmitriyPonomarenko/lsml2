FROM python:3.10

WORKDIR /app

RUN pip install torch==2.1.0 torchvision==0.16.0 --index-url https://download.pytorch.org/whl/cpu
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY food101_vit.py /app
RUN wget https://github.com/DmitriyPonomarenko/lsml2/releases/download/v1.0.0/pytorch_model.bin
RUN wget https://github.com/DmitriyPonomarenko/lsml2/releases/download/v1.0.0/config.json
RUN wget https://github.com/DmitriyPonomarenko/lsml2/releases/download/v1.0.0/preprocessor_config.json

EXPOSE 5000

ENV FLASK_APP=food101_vit.py
ENV FLASK_RUN_HOST=0.0.0.0

ENTRYPOINT ["flask", "run"]