import socket
from threading import Thread
from Node import Node

class Network:
  
	def __init__(Node_):  
		self.node = node_
		self.nodes = []
		self.blockchain = None
		node.init_node()

	def broadcast_transaction(self, str_transaction): 
		for node in self.nodes:
			node.send("-t ", node.s, nodes, str_transaction)
    
	def broadcast_block(self, str_block): 
		for node in self.nodes:
			node.send("-b ", node.s, nodes, str_transaction)

	def receiv(self):
		print("ready to receiv")
    
		while True:
			data, addr = mode.s.recvfrom(1024)
			curentNode = node(str(addr))

			myData = str(data)

			if myData[:3] == "-c ":
				#retourne le JSON de la chain
				nodes.send("-ac", node.s, cureNode, None) #None le JSON

			elif myData[:3] == "-n ": #Done
				#Parcourir la liste de noeud et les envois à l'emmeteur
				for i in self.nodes:
					node.send("-an", node.s, cureNode, None) #None Le JSON

			elif myData[:3] == "-t ":
				#Reception d'une transaction
				for i in self.nodes:
					node.send("-t ", node.s, nodes, myData[3:lenth(myData)])

			elif myData[:3] == "-b ":
				#Reception d'un block
				for i in self.nodes:
					node.send("-b ", node.s, nodes, myData[3:lenth(myData)])

			elif myData[:3] == "-p ": #Done
				#Envoie tous les nodes
				for i in self.nodes:
					node.send("-ap", node.s, cureNode, "")

			#Faire les codes retour -ac, -ap et -ac
		
		c.close()