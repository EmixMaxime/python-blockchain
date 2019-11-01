import socket
from threading import Thread
from Node import Node

class Network:
  
	def __init__(Node_):  
		self.node = node_
		self.nodes = []
		self.blockchain = None
		node.init_node()

	def set_blockchain(self, blockchain_): #Done
		self.blockchain = blockchain_

	def broadcast_transaction(self, str_transaction_): #Done
		for node in self.nodes:
			node.send("-t ", node.s, nodes, str_transaction_)
    
	def broadcast_block(self, str_block): #Done
		for node in self.nodes:
			node.send("-b ", node.s, nodes, str_transaction_)

	def receiv(self):
		print("ready to receiv")
    
		while True:
			data, addr = mode.s.recvfrom(1024)
			curentNode = node(str(addr))

			myData = str(data)

			if myData[:3] == "-c ":
				#retourne le JSON de la chain, manque la fonction de Max
				nodes.send("-ac", node.s, cureNode, None) #None le JSON

			elif myData[:3] == "-n ": #Done
				#Parcourir la liste de noeud et les envois à l'emmeteur
				for i in self.nodes:
					node.send("-an", node.s, cureNode, "") #None Le JSON

			elif myData[:3] == "-t ":
				#Reception d'une transaction, manque la fonction de Max
				for i in self.nodes:
					node.send("-t ", node.s, nodes, myData[3:lenth(myData)])

			elif myData[:3] == "-b ":
				#Reception d'un block, manque la fonction de max
				for i in self.nodes:
					node.send("-b ", node.s, nodes, myData[3:lenth(myData)])

			elif myData[:3] == "-p ": #Done
				#Envoie tous les nodes
				for i in self.nodes:
					node.send("-ap", node.s, cureNode, "")

			#Faire les codes retour -ac, -ap et -ac
		
		c.close()