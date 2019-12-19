from threading import Lock, Thread
from socket import SO_REUSEADDR, SOCK_STREAM, socket, SOL_SOCKET, AF_INET
from io import BytesIO
import random
import qrcode

FLAG = 'KAF{k4r1_m4rx_15_7h3_b357}'

GOOD = 'Good!'
GOODBYE = 'Goodbye :('

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8000))

BOOKS = {
    '9781593272906': 'Practical Malware Analysis',
    '9781593279127': 'Practical Binary Analysis',
    '9781593278021': 'Practical Packet Analysis',
    '9781593271442': 'Hacking',
    '9781593277161': 'Rootkits and Bootkits',
    '9781118825099': 'The Art of Memory Forensics',
    '9781593278595': 'Malware Data Science',
    '9781118787311': 'Practical Reverse Engineering',
    '9780764574818': 'Reversing',
    '9780133591620': 'Modern Operating Systems',
    '9781985086593': 'Operating Systems',
    '9780262640688': 'The Elements of Computing Systems',
    '9780132126953': 'Computer Networks',
    '9780133594140': 'Computer Networking',
    '9781977593375': 'Windows Kernel Programming',
    '9780201633610': 'Design Patterns',
    '9780735684188': 'Windows Internals',
    '9781449626365': 'The Rootkit Arsenal',
    '9780321294319': 'Rootkits',
    '9780131103627': 'C Programming Language',
    '9781593278267': 'Serious Cryptography',
    '9781119096726': 'Applied Cryptography',
    '9781593270476': 'The TCP/IP Guide',
    '9780201633467': 'TCP/IP Illustrated',
    '9780470080238': 'The Shellcoder\'s Handbook',
    '9781118026472': 'The Web Application Hacker\'s Handbook',
    '9780321714114': 'C++ Primer',
    '9780134997834': 'A Tour of C++',
    '9781593276690': 'Game Hacking',
    '9781476734293': 'The Communist Manifesto',
}

threads = []

class ClientHandler(Thread):
    def __init__(self, address, port, socket):
        Thread.__init__(self)
        self.address = address
        self.port = port
        self.socket = socket

    def run(self):
        should_get_flag = True

        isbns = BOOKS.keys()
        random.shuffle(isbns)

        for isbn in isbns:
            fd = BytesIO()

            qr_img = qrcode.make(isbn).get_image()
            qr_img.save(fd, 'png')

            self.socket.send(fd.getvalue())

            data = self.socket.recv(4096).replace('\n', '').lower()
            book = BOOKS[isbn].lower()

            if book == data or book in data:
                self.socket.send(GOOD)
            else:
                should_get_flag = False
                break
            
        if should_get_flag:
            self.socket.send(FLAG)
        else:
            self.socket.send(GOODBYE)

        self.socket.close()

while 1:
    s.listen(1)
    
    sock, addr = s.accept()
    
    newThread = ClientHandler(addr[0], addr[1], sock)
    newThread.start()
    
    threads.append(newThread)
