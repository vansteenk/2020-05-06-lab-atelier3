#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import ftplib


statut=False
while statut!=True :
	hostname=input("Hostname : ") # Addresse du serveur FTP
	username="user"
	password="testtest"
	
	#tentative de connexion
	connect=ftplib.FTP('hostname','username','password') # connect est la variable de connexion
	statut=True
	bienvenue=connect.getwelcome() # on récupère le "message de bienvenue"
	print(bienvenue)
