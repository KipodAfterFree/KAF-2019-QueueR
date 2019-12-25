from PIL import Image
from socket import SO_REUSEADDR, SOCK_STREAM, error, socket, SOL_SOCKET, AF_INET
from pyzbar.pyzbar import decode
import urllib
import io
import json

sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

sock.connect(('ctf.kaf.sh', 6010))

while True:
    data = sock.recv(4096)

    if 'KAF' in data:
        print data
        break

    f = io.BytesIO()
    f.write(data)

    qr_code = decode(Image.open(f))[0].data
    response = urllib.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:' + qr_code)

    print qr_code

    data = json.loads(response.read())
    title = data['items'][0]['volumeInfo']['title']

    print title
    sock.send(title)

    res = sock.recv(4096)

    if 'Goodbye' in res:
        print res
        break

sock.close()
