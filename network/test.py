import socket
from threading import Thread

'''
Faire la fonction de broadcast
un tableau qui contiendra les IP des personnes du reseau et les gens qui ont deja ete connectes en p2p
'''

def Main():
    host = '192.168.1.82' #Adresse du pc
    port = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host,port))
    server = ('192.168.1.82',5001) #Adresse de l'autre pc

    t1 = Thread(target=receiv, args=("ready to receive", s))
    t1.start()

    t2 = Thread(target=send, args=("ready to send", s, server, ""))
    t2.start()

    t1._Thread__stop()

def receiv(a, s):
    
    print(a)
    while True:
        data, addr = s.recvfrom(1024)
        print (str(data))
    c.close()

def send(a_, s_, server_, message_):

    s_.sendto("recu : " + message_, server_)

if __name__ == '__main__':
    Main()