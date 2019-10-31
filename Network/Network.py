import socket
from threading import Thread
from Node import Node

class Network:
  
	def __init__(Node_):  
		node = node_
		nodes = []
		node.init_node()

	#def broadcast_transaction(): #A definir
    
    
	#def broadcast_block(): #A definir


	def receiv():
		print("ready to receiv")
    
		while True:
			data, addr = mode.s.recvfrom(1024)
			cureNode = node(str(addr))

			if (str(data)) == "-c ":
				#Appel de la fonction qui retourne le JSON de la blockchain

			elif (str(data)) == "-n ":
				#Parcourir la liste de noeud et les envois à l'emmeteur
				for i in range(len(nodes)):
					nodes[i].send("-an", node.s, cureNode, ?); # ? Le JSON

			elif (str(data)) == "-t ":
				#Appel de la fonction qui ajoutera une transaction

			elif (str(data)) == "-b ";
				#appel de la fonction qui ajoutera un block

			elif (str(data)) == "-p ":
				#Envoie tous les nodes connu
				for i in range(len(nodes)):
					nodes[i].send("-ap", node.s, cureNode, "");

			#Faire les codes retour -an et -ap
		
		c.close()