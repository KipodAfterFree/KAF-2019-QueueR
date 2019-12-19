# QueueR

QueueR is an information security challenge in the miscellaneous category, and was presented to participants of [KAF CTF 2019](https://play.kaf.sh)

## Challenge story

I found that pcap file on the USB drive of a communist developer I know. Can you find out what he's trying to say?

## Challenge exploit

A

## Challenge solution

A

## Building and installing

[Clone](https://github.com/omerk2511/KAF-2019-QueueR/archive/master.zip) the repository, then type the following command to build the container:
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
KAF{k4r1_m4rx_15_7h3_b357}
```

## License
[MIT License](https://choosealicense.com/licenses/mit/)
