import socket
from threading import Thread


class Node:
    """
    if host is none, so it's me -> auto discover of my local ip address.
    """

    def __init__(self, host_=None):
        self.port = 5000
        self.my_socket = None

        if host_ is None:
            host_name = socket.gethostname()
            self.host = socket.gethostbyname(host_name)
            print("Creating a socket server", self.host, ":", self.port)
            self._init_node()
        else:
            self.host = host_  # Adresse du pc

    """
    Initialize the node as myself.
    """

    def _init_node(self):
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.my_socket.bind((self.host, self.port))

    def send(self, command_, node_, message_):
        server = (node_.host, node_.port)  # Server
        msg_to_send = (command_ + message_)
        print('send msg:', msg_to_send, 'to ',
              server, 'with socket', self.my_socket)
        self.my_socket.sendto(msg_to_send.encode(), server)
