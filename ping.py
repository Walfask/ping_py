import os, time, subprocess
from pythonping import ping
from sys import argv

os.system('mode 50,2')
os.system('color 2')

address = '8.8.8.8'

if len(argv) > 1:
    address = argv[1]

try:
    while True:
        response = ping(address, count=1)
        os.system('cls')
        print(f"Ping {address} : {response.rtt_avg_ms} ms")
        time.sleep(2)
except KeyboardInterrupt:
    print('terminated!')
    time.sleep(2)
