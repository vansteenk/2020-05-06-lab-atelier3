#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import ftplib
from getpass import getpass

statut=False
while statut!=True :
	hostname="pc2" # Addresse du serveur FTP
	username="user"
	password=getpass()
	
	#tentative de connexion
	try:
		connect=ftplib.FTP(hostname) # connect est la variable de connexion
		connect.login(username,password)
		statut=True
		bienvenue=connect.getwelcome() # on récupère le "message de bienvenue"
		print(bienvenue + "- Connexion à " + hostname + " établie")
	except:
		print("Erreur. Recommencez. ")
		statut=False

