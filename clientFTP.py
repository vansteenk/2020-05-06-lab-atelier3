#!/usr/bin/env python3

# -*- coding: utf-8 -*-

#Date : 06.05.2020
#Auteurs : Tayana / Sandrine / Maxime / Cyril
#Formation AJC Consultant Réseau - Atelier 3
#Création d'un client FTP

import ftplib
from getpass import getpass


#Fonction nanuel, pour aider avec les differentes commandes
def help (connect): #lire le fichier help.txt
	with open("help.txt", "r") as fichier:
		print(fichier.read())

def creer (connect, chemin): #MKD (dossier)
	mkd=connect.mkd(chemin)
	print (mkd)

def renommer (connect, fromname, toname): #RNFR
	rename=connect.rename(fromname, toname)
	print (rename)

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
	localisation(connect,0,0)

def deconnexion (connect):

	try:
		connect.quit() #On se deconnecte proprement

	except:
		connect.close() #si la deconnexion rencontre une erreur, on force la fermeture

	
	
			
def connexion() :
	statut=False
	while statut!=True : #une boucle de connexion avec un "statut" retournant l'état de connexion (True/False)
		hostname="pc2" # Addresse du serveur FTP
		username="user"
		password="testtest"
	
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

def choix_cmd (cmd):
	switcher = {
		'mkd': creer,
		'rnfr': renommer,
		'dele': supprimerFichier,
		'rmd': supprimerDossier,
		'list': lister,
		'stor': envoyer,
		'pwd': localisation,
		'cwd': se_deplacer,
		'quit': deconnexion,
		'help': help
		}
	return switcher.get(cmd, lambda: "no valid command")


cmd="help"
connect=connexion()
while cmd!="quit" :
		
	print("Que souhaitez vous faire ? Tapez HELP pour plus d'informations")
	commande=input(":>>")

	cmdsplit=commande.split() # On sépare les commandes des arguments potentiels
		
	try:
		cmd=cmdsplit[0]
		cmd=cmd.lower()
		elif len(cmdsplit)==1: # Aucun argument input par l'utilisateur
			func = choix_cmd(cmd)
			func(connect)
		
		elif len(cmdsplit)==2: # 1 seul argument en input
			arg1=cmdsplit[1]
			func = choix_cmd(cmd)
			func(connect, arg1)
		
		elif len(cmdsplit)==3: # 2 arguments en input
			arg1=cmdsplit[1]
			arg2=cmdsplit[2]
			func = choix_cmd(cmd)
			func(connect, arg1, arg2)
	except:
		print("Erreur. Tapez help.")














