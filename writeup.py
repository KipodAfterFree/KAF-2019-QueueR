from PIL import Image
from socket import SO_REUSEADDR, SOCK_STREAM, error, socket, SOL_SOCKET, AF_INET
from pyzbar.pyzbar import decode
import urllib
import json

sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

sock.connect(('127.0.0.1', 8000))

while True:
    data = sock.recv(4096)

    if 'KAF' in data or 'Goodbye' in data:
        print data
        break

    f = open('file.png', 'wb')
    f.write(data)
    f.close()

    qr_code = decode(Image.open('file.png'))[0].data
    response = urllib.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:' + qr_code)

    print qr_code

    data = json.loads(response.read())
    title = data['items'][0]['volumeInfo']['title']

    print title
    sock.send(title)

    res = sock.recv(4096)

    if 'KAF' in res or 'Goodbye' in res:
        print res
        break

sock.close()
