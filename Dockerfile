FROM python:2.7

RUN pip install qrcode[pil]

WORKDIR /home
COPY server /home
EXPOSE 8000

CMD ["python", "server.py"]