# 2020-05-06-lab-atelier3
Lab Client FTP Python

**Contributeurs : Tayana / Sandrine / Maxime / Cyril**

```
Fichiers code Python : clientftp.py
Fichier annexe : help.txt
```

** patch-1 branch : **

> Optimisation de *clientFTP.py* 
>   - [x] suppression des arguments inutiles des fonctions
>   - [x] mise en conditions de l'utilisation du switcher en fonction des arguments

> Mise en forme help.txt

> Etat : le code est fonctionnel. Il pourrait sans doute être optimisé (et agrémenté d'autres fonctions)

## Enoncé

#### 1- Mise en place d’un client FTP avec Python

Préparation d’une deuxième machine Debian, cette machine devra être sur le même réseau que la première. Une machine aura pour rôle le serveur FTP, tandis que la deuxième sera le client ftp. Réaliser un script python qui jouera le rôle de client ftp.

- [x] Pouvoir se connecter, donc :
  - [x] Entrer le nom d’hôte
  - [x] Le nom d’utilisateur
  - [x] Et le mot de passe, très important !

- [x] Pouvoir envoyer une commande (nous les listerons un peu plus bas)
- [x] Pouvoir taper une commande, mais avec des arguments ! (Petite nuance)


On doit pouvoir :
- [x] Créer
- [x] Renommer
- [ ] Déplacer
- [x] Supprimer des fichiers / dossiers
- [x] Se déplacer entre les répertoires
- [x] Lister leur contenu
- [x] Envoyer un fichier sur notre serveur

En voici donc la liste :
- [x] CWD *(change current directory) pour changer de répertoire de travail*
- [x] DELE *(delete) pour supprimer un fichier / dossier*
- [x] LIST *pour lister les fichiers et dossiers d’un répertoire (si vous n’en spécifiez pas, alors ce sera le répertoire courant qui sera listé)*
- [x] MKD *(make directory) pour créer un répertoire*
- [x] RMD *(remove directory) pour supprimer un répertoire*
- [x] RNFR *(rename a file from (name …)) pour renommer un répertoire X en …*
- [x] STOR *(store a file) pour envoyer un fichier sur le serveur.*

#### 2- Autre atelier en bonus

Comment, via python, envoyer des ordres (installer des packages , lister des fichiers…) sur la machine serveur, à partir de la machine cliente? Les scripts devront être déposés sur un dépôt GitHub en accès publique.



