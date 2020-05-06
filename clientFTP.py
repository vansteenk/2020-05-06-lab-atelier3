#!/usr/bin/env python3

# -*- coding: utf-8 -*-

#Date : 06.05.2020
#Auteurs : Tayana / Sandrine / Maxime / Cyril
#Formation AJC Consultant Réseau - Atelier 3
#Création d'un client FTP

import ftplib
from getpass import getpass


#Fonction nanuel, pour aider avec les differentes commandes
def help: #lire le fichier help.txt
	with open("help.txt", "r") as fichier:
		print(fichier.read())

def creer (connect, chemin): #MKD (dossier)
	mkd=connect.mkd(chemin)
	print mkd

def renommer (connect, fromname, toname): #RNFR
	rename=connect.rename(fromname, toname)
	print rename

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

def localisation (connect): #PWD

	path=connect.pwd() #on retourne le chemin du dossier courant
	print (path)

def se_deplacer (connect, chemin): #CWD

	connect.cwd(chemin) # On se deplace dans le repertoire indiqué
	localisation(connect)

def deconnexion (connect):

	try:
		connect.quit() #On se deconnecte proprement

	except:
		connect.close() #si la deconnexion rencontre une erreur, on force la fermeture

def connexion()
statut=False
while statut!=True : #une boucle de connexion avec un "statut" retournant l'état de connexion (True/False)
	hostname="pc2" # Addresse du serveur FTP
	username="user"
	password=getpass()
	
	#tentative de connexion
	try:
		connect=ftplib.FTP(hostname,username,password) # connect est la variable de connexion
		statut=True
		bienvenue=connect.getwelcome() # on récupère le "message de bienvenue"
		print(bienvenue + "- Connexion à " + hostname + " établie")
	except:
		print("Erreur. Recommencez. ")
		statut=False
return (connect)


def main()

	connect=connexion()

	print("Que souhaitez vous faire ? Tapez HELP pour plus d'informations")
	commande=input(":>>")

	cmdsplit=commande.split() # On sépare les commandes des arguments potentiels
	cmd=cmdsplit[0]
	arg1=cmdsplit[1]
	arg2=cmdsplit[2]
	
	deconnexion(connect)



################################################################
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














