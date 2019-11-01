import socket
from threading import Thread

class Node:
	def __init__(self, host_):
		self.host = host_ #Adresse du pc
		self.port = 5000
		self.s = None

	def init_node(self):
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.s.bind((self.host, self.port))

	def ping(self, node_to_ping): 
		send("-p ", self.s, node_to_ping, "");


	def send(self, command_, s_, node_, message_):
		server = (node_.host, node_.port) #Server 
		self.s_.sendto(command_ + message_, servers)