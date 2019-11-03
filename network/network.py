import socket
import jsonpickle
from threading import Thread
from node import Node

class Network:
  
	def __init__(self, Node_):  
		self.node = node_
		self.nodes = []
		self.blockchain = None
		node.init_node()

	def set_blockchain(self, blockchain_): #Done
		self.blockchain = blockchain_

	def broadcast_transaction(self, str_transaction_): #Done
		for nodeList in self.nodes:
			self.node.send("-t ", node.s, nodeList, str_transaction_)
    
	def broadcast_block(self, str_block_): #Done
		for nodeList in self.nodes:
			self.node.send("-b ", node.s, nodeList, str_block_)

	def broadcast_ask_chain(self): #Done
		for nodeList in self.nodes:
			self.node.send("-c ", node.s, nodeList, "")

	#Une fonction pour broadcast ping 

	def receiv(self):
		print("ready to receiv")
    
		while True:
			data, addr = mode.s.recvfrom(1024)
			curentNode = node(str(addr))

			myData = str(data)

			if myData[:3] == "-c ": #Done
				#Retourne le JSON de la chaine
				self.node.send("-ac", node.s, cureNode, self.blockchain.chain_for_network)

			elif myData[:3] == "-n ": #Done
				#Parcourir la liste de noeud et les envois a l'emmeteur
				for nodeList in self.nodes:
					nodeToSend = jsonpickle.encode(nodeList)
					self.node.send("-an", node.s, cureNode, nodeToSend)

			elif myData[:3] == "-t ": #Done
				#Reception d'une transaction
				self.blockchain.submit_block(myData[3:length(myData)])

			elif myData[:3] == "-b ": #Done
				#Reception d'un block
				self.blockchain.submit_transaction(myData[3:length(myData)])

			elif myData[:3] == "-p ": #Done
				#Repond present 
				nodeToSend = jsonpickle.encode(self.node)
				self.node.send("-an", node, cureNode, nodeToSend)

			elif myData[:3] == "-ac": #En suspend
				some = None 

			elif myData[:3] == "-an": #Done
				node = jsonpickle.decode(myData[3:length(myData)])

				notFind = True
				for nodeList in self.nodes:
					if nodeList.host == node.host:
						notFind = False

				if notFind:
					self.nodes.append(node)
					notFind = False
		
		c.close()