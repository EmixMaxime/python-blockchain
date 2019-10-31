import socket
from threading import Thread

class Node:
	def __init__(host_):
		host = host_ #AdressePc
		port = 5000
		s

	def init_node(node_):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind((node_.host, node_.port))

	def ping(): #A deplacer
		send("-p ", self.s, ?, ""); # ? destinataire à definir


	#def send_transation(transaction_): #A definir
		#Methode transaction

	#def send_block(block_): #A definir
		#Methode block

	def send(command_, s_, node_, message_):

		server = (node_.host, node_.port) #Adresse de l'autre pc
		s_.sendto(command_ + message_, servers)