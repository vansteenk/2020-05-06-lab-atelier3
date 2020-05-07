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
	rep=connect.mkd(chemin)
	return (rep)

def renommer (connect, fromname, toname): #RNFR
	rep=connect.rename(fromname, toname)
	return (rep)

def supprimerFichier (connect, filename): #DELE 
	rep=connect.delete(filename) #fichier
	return (rep)

def supprimerDossier (connect, dirname): #RMD 
	rep=connect.rmd(dirname) #dossier
	return (rep)

def lister (connect, dirname): #LIST
	rep=connect.dir(dirname)
	return (rep)

def envoyer (connect, fichier): #STOR
	ouverture = open(fichier, 'rb') # on ouvre le fichier 
	rep=connect.storbinary('STOR '+fichier, ouverture) # ici (où connect est encore la variable de la connexion), on indique le fichier à envoyer
	ouverture.close() # on ferme le fichier
	return (rep)

def localisation (connect): #PWD
	rep=connect.pwd() #on retourne le chemin du dossier courant
	return (rep)

def se_deplacer (connect, chemin): #CWD
	rep=connect.cwd(chemin) # On se deplace dans le repertoire indiqué
	return (rep)

def deconnexion (connect):
	try:
		rep=connect.quit() #On se deconnecte proprement
	except:
		rep=connect.close() #si la deconnexion rencontre une erreur, on force la fermeture
	return (rep)
			
#def sendcommande (connect, cmd):
#	rep=connect.sendcmd(cmd)
#	return(rep)

def connexion() :
	statut=False
	while statut!=True : #une boucle de connexion avec un "statut" retournant l'état de connexion (True/False)
		hostname=input("Hostname : ") # Addresse du serveur FTP
		username=input("Username : ")
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
		'help': help,
		'scmd': sendcommande
		}
	return switcher.get(cmd, lambda: "no valid command")


cmd="help"
connect=connexion()
print("Que souhaitez vous faire ? Tapez HELP pour plus d'informations")

while cmd!="quit" :
		
	commande=input(":>>")

	cmdsplit=commande.split() # On sépare les commandes des arguments potentiels
		
	
	cmd=cmdsplit[0]
	cmd=cmd.lower()
	func = choix_cmd(cmd)

	try:
		if len(cmdsplit)==1: # Aucun argument input par l'utilisateur
			if cmd=="list":  # cas particulier où la commande "list" est input sans argument
				arg1=localisation(connect) # on recupère l'emplacement actuel
				retour=func(connect, arg1)
			else:
				retour=func(connect)
		
		elif len(cmdsplit)==2: # 1 seul argument en input
			arg1=cmdsplit[1]
			if arg1=="?":
				help(connect)
			else :
				retour=func(connect, arg1)
		
		elif len(cmdsplit)==3: # 2 arguments en input
			arg1=cmdsplit[1]
			arg2=cmdsplit[2]
			retour=func(connect, arg1, arg2)

		print(retour)

	except:
		print("Erreur. Tapez help.")














