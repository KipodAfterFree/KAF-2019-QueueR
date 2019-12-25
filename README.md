# QueueR

QueueR is an information security challenge in the miscellaneous category, and was presented to participants of [KAF CTF 2019](https://play.kaf.sh)

## Challenge story

I found that pcap file on the USB drive of a communist developer I know. Can you find out what he's trying to say?

## Challenge solution

Based on the pcap file, we can understand the protocol is like this: the server sends a PNG file that is a QR code. The QR code represents an ISBN number, that leads to a corresponding book, which the client responds to the server. We can create a script that does that and gets the flag eventually. [This](writeup.py) is a script that does that.

## Building and installing

[Clone](https://github.com/KipodAfterFree/KAF-2019-QueueR/archive/master.zip) the repository, then type the following command to build the container:
```bash
docker build . -t queuer
```

To run the challenge, execute the following command:
```bash
docker run --rm -d -p 6010:8000 queuer
```

## Usage

You may now access the challenge interface through netcat: `nc 127.0.0.1 8000`

## Flag

Flag is:
```flagscript
KAF{}
```

## License
[MIT License](https://choosealicense.com/licenses/mit/)
