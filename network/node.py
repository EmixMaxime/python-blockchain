import socket
from threading import Thread


class Node:
    """
    if host is none, so it's me -> auto discover of my local ip address.
    """

    def __init__(self, host_=None):

        if host_ is Node:
            host_name = socket.gethostname()
            self.host = socket.gethostbyname(host_name)
            self._init_node()
        else:
            self.host = host_  # Adresse du pc

        self.port = 5000
        self.s = None

    def _init_node(self):
    """
    Initialize the node as myself.
    """

    self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.s.bind((self.host, self.port))

    def ping(self, node_to_ping):
        send("-p ", self.s, node_to_ping, "")

    def send(self, command_, s_, node_, message_):
        server = (node_.host, node_.port)  # Server
        self.s_.sendto(command_ + message_, servers)
