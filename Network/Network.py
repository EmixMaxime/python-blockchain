import socket
import jsonpickle
from threading import Thread
from Node import Node

class Network:
  
	def __init__(self, Node_):  
		self.node = node_
		self.nodes = []
		self.blockchain = None
		node.init_node()

	def set_blockchain(self, blockchain_): #Done
		self.blockchain = blockchain_

	def broadcast_transaction(self, str_transaction_): #Done
		for node in self.nodes:
			node.send("-t ", node.s, nodes, str_transaction_)
    
	def broadcast_block(self, str_block_): #Done
		for node in self.nodes:
			node.send("-b ", node.s, nodes, str_block_)

	def broadcast_ask_chain(self): #Done
		for node in self.nodes:
			node.send("-c ", node.s, nodes, "")

	#Une fonction pour broadcast ping 

	def receiv(self):
		print("ready to receiv")
    
		while True:
			data, addr = mode.s.recvfrom(1024)
			curentNode = node(str(addr))

			myData = str(data)

			if myData[:3] == "-c ": #Done
				#Retourne le JSON de la chain, manque la fonction de Max
				nodes.send("-ac", node.s, cureNode, self.blockchain.chain_for_network)

			elif myData[:3] == "-n ": #Done
				#Parcourir la liste de noeud et les envois a l'emmeteur
				for i in self.nodes:
					nodeToSend = jsonpickle.encode(nodes)
					node.send("-an", node.s, cureNode, nodeToSend)

			elif myData[:3] == "-t ": #Done
				#Reception d'une transaction, manque la fonction de Max
				self.blockchain.submit_block(myData[3:length(myData)])

			elif myData[:3] == "-b ": #Done
				#Reception d'un block, manque la fonction de max
				self.blockchain.submit_transaction(myData[3:length(myData)])

			elif myData[:3] == "-p ": #Done
				#Repond present 
				nodeToSend = jsonpickle.encode(self.node)
				node.send("-an", node, cureNode, nodeToSend)

			elif myData[:3] == "-ac": #En suspend
				#Manque la fonction de Max
				some = None 

			elif myData[:3] == "-an":
				#Manque la fonction de Moi
				some = None #Fonction pour ajouter un noeud
		
		c.close()