# 2020-05-06-lab-atelier3
Lab Client FTP Python

**Contributeurs : Tayana / Sandrine / Maxime / Cyril**

##Fichiers code Python : clientftp.py
##Fichier annexe : help.txt

``Etat : le code est fonctionnel. Il pourrait sans doute être optimisé (et agrémenté d'autres fonctions)``

## Enoncé

#### 1- Mise en place d’un client FTP avec Python

Préparation d’une deuxième machine Debian, cette machine devra être sur le même réseau que la première. Une machine aura pour rôle le serveur FTP, tandis que la deuxième sera le client ftp. Réaliser un script python qui jouera le rôle de client ftp.

* Pouvoir se connecter, donc :
** Entrer le nom d’hôte
** Le nom d’utilisateur
** Et le mot de passe, très important !

* Pouvoir envoyer une commande (nous les listerons un peu plus bas)
* Pouvoir taper une commande, mais avec des arguments ! (Petite nuance)


On doit pouvoir :
* Créer
* Renommer
* Déplacer
* Supprimer des fichiers / dossiers
* Se déplacer entre les répertoires
* Lister leur contenu
* Envoyer un fichier sur notre serveur

En voici donc la liste :
* CWD *(change current directory) pour changer de répertoire de travail*
* DELE *(delete) pour supprimer un fichier / dossier*
* LIST *pour lister les fichiers et dossiers d’un répertoire (si vous n’en spécifiez pas, alors ce sera le répertoire courant qui sera listé)*
* MKD *(make directory) pour créer un répertoire*
* RMD *(remove directory) pour supprimer un répertoire*
* RNFR *(rename a file from (name …)) pour renommer un répertoire X en …*
* STOR *(store a file) pour envoyer un fichier sur le serveur.*

#### 2- Autre atelier en bonus
Comment, via python, envoyer des ordres (installer des packages , lister des fichiers…) sur la machine serveur, à partir de la machine cliente? Les scripts devront être déposés sur un dépôt GitHub en accès publique.
