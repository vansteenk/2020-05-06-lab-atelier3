#!/usr/bin/env python3

# -*- coding: utf-8 -*-

#Date : 31/03/2020
#Auteur : Cyril AUREJAC
#Formation AJC Consultant Réseau - Module Python
#Atelier Python : Création d'un client FTP

import ftplib
from getpass import getpass


#Fonction nanuel, pour aider avec les differentes commandes
def help: #lire le fichier help.txt
	with open("help.txt", "r") as fichier:
		print(fichier.read())

def creer (connect, chemin): #MKD (dossier)
	connect.mkd(chemin)

def renommer (connect, fromname, toname): #RNFR
	connect.rename(fromname, toname)

def deplacer (connect, old_chemin, new_chemin): #MV
	connect.mk

def supprimerFichier (connect, filename): #DELE 
	
	connect.delete(filename) #fichier

def supprimerDossier (connect, dirname): #RMD 
	
	connect.rmd(dirname) #dossier

def lister (connect, dirname): #LIST
	rep=connect.dir(dirname)
	print (rep)


def envoyer (connect, fichier): #STOR

	ouverture = open(fichier, 'rb') # on ouvre le fichier 
	connect.storbinary('STOR '+fichier, ouverture) # ici (où connect est encore la variable de la connexion), on indique le fichier à envoyer
	ouverture.close() # on ferme le fichier


def se_deplacer: #CWD

# Quit
# PWD

#Programme principal

#une boucle de connexion avec un "statut" retournant l'état de connexion (True/False)
statut=False
while statut!=True :

	#Demande hostname, username et pwd
	hostname=input("Hostname : ") # Addresse du serveur FTP
	username="root"
	password=getpass()

	#tentative de connexion
	try:
		connect=ftplib.FTP('hostname','username','password') # connect est la variable de connexion
		statut=True
		bienvenue=connect.getwelcome() # on récupère le "message de bienvenue"
		print(bienvenue)
	except:
		print("Erreur. Recommencez. ")
		statut=False


#boucle MAIN à rajouter
print("Que souhaitez vous faire ? Tapez HELP pour plus d'informations")
commande=input(":>>")

#On teste si la cmd est MV
if commande.lower[0:1]=="mv":
	#On cherche l'espace censé séparer les 2 arguments(chemins des dossiers/fichier)
	i=0
	for elt in commande[3:-1]:
		if elt==" ":
			argument1=commande[3:(i-1)]
			argument2=commande[(i+1):-1]
			break
		i++
	#Si on a trouvé un espace, on envoie les arguments dans la fonction
	if i < len(commande[3:-1]):
		deplacer(argument1, argument1)
	#Sinon on revient au debut de la boucle MAIN
	else:
		print ("Erreur de syntaxe. Référez vous à help. ")
		continue

elif commande.lower[0:2]=="cwd":

elif commande.lower[0:2]=="rmd":

elif commande.lower[0:2]=="mkd":

elif commande.lower[0:3]=="stor":

elif commande.lower[0:3]=="list":

elif commande.lower[0:3]=="dele":

elif commande.lower[0:3]=="rnfr":

elif commande.lower[0:3]=="help":

else:
	print("Commande inconnue.")
	continue














