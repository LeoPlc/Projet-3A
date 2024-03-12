# SMART HOME APPLICATION

Ce projet consiste à concevoir étape par étape une application permettant d'interconnecter divers objets connectés, existants sur le marché. Cette application est décortiquée et présentée dans ce répertoire GitHub, afin d'en comprendre les différents aspects et objectifs. 

Lien vers la vidéo explicative du projet: [cliquez ici](https://www.youtube.com/watch?v=c5vRu4_OLxM)

## 1- INTRODUCTION

### DESCRIPTION DU PROJET

En premier lieu, il faut se poser la question suivante: **comment fonctionnent les objets connectés ?** Cette question rassemble non seulement les différents types d'objets connectés existants et leurs différents domaines d'application, mais aussi les protocoles de communication mis en oeuvre selon ces domaines. Dans notre cas, il s'agit d'une maison connectée. Nous pouvons donc avoir affaire aux objets **connectés** suivants *(liste non exhaustive)*:

- Ampoules RGB 
- Prises
- Chauffage
- Volets roulants
- Système de sécurité *(caméra(s), alarme(s), capteur(s) de mouvement,...)*
- etc.

Dans notre cas, nous allons vous présenter quelques uns de ces objets au travers de ce projet, et nous allons couvrir plusieurs protocoles de communication connus, comme:

- WiFi
- Bluetooth
- Zigbee
- Xbee
- etc.

En fonction des protocoles de communication mis en place, il n'y a pas seulement l'objet et l'application à prendre en compte, mais aussi parfois une passerelle permettant de transmettre les informations de l'application vers l'objet connecté (par exemple en Zigbee, une passerelle est connectée à une box WiFi - *ou partage de connexion* - et transmets les requêtes en Zigbee jusqu'aux objets concernés).

Ainsi ce projet permettra de décrire comment concevoir une application permettant de se connecter à divers appareils connectés via différents protocoles et différentes installations.

Ce projet nous servira également à expliquer notre utilisation de Home Assistant ainsi que de OpenHab. 

Pour finir, vous trouverez également une partie explicative de notre maquette de présentation ainsi que notre vidéo de présentation de notre projet.


## 2- Architecture du dépôt

Notre dépôt possède 3 gros dossiers à savoir [work](work), [softs](softs), [demo](demo).

> Dossier [work](work) : Ce dossier permet de retrouver les différentes versions de notre application python. Vous y trouverez également un README expliquant notre code ainsi que ses différentes versions. 

> Dossier [softs](softs) : Ce dossier permet de retrouver deux sous dossier, un pour Home assistant et un pour OpenHab. Dans chaque dossier se trouve un fichier README permettant d'expliquer notre utilisation de l'OS.

> Dossier [demo](demo) : Ce dossier permet de retrouver la partie démonstration de notre projet. Premièrement, vous trouverez un dossier maquette contenant un README expliquant comment nous avons réalisé notre maquette. Deuxièmement vous retrouverez un dossier presentation contenant notre vidéo de présentation ainsi que notre diaporama. 

## 2- ARCHITECTURE DE L'APPLICATION

Avant de commencer toute activité, il faut décider de l'architecture de l'application, car cette dernière devra non seulement permettre la communication avec différents appareils connectés, mais devra aussi traiter les données provenant de ces objets *(capteurs de température, de mouvement, flux vidéo,...)* afin d'en retirer un comportement voulu *(monter la température, fermer un volet, alerter le propriétaire d'un mouvement inhabituel,...)*.

L'application doit donc permettre les choses suivantes:
- La collection de données
- Le traitement de ces données
- Une interface utilisateur
- Le contrôle des objets 
- La sauvegarde de ces données en mémoire 
- Une sécurité 
- Des entrées utilisateurs *(envoyer des commandes de température, de couleur, d'actions particulières,...)*

L'application mettra donc en oeuvre des concepts de matériel, de protocoles de transmission, mais aussi de base de donnée, de front-end / back-end afin de parvenir à piloter une maison connectée. 


### Modèles

- Collection (organisation des tâches en différentes catégories)
    - Nom
    - "Slug"
- Tâche
    - Description
    - Collection d'appartenance (clé d'appartenance à une collection)

## 3-Fonctionalités 

Ces fonctionnalités vont permettre la mise en oeuvre du POC, ou Proof of Concept, permettant de valider ou non le cahier des charges initial (fonctionnalités demandées, ici le fait de pouvoir se connecter à distance à un appareil connecté comme une ampoule RGB).

Le POC consiste donc pour nous à mettre en oeuvre les fonctionnalités minimales représentant le projet: se connecter/se déconnecter d'un appareil. Si ces fonctionnalités sont opérationnelles, il faut ensuite pouvoir envoyer une instruction/une commande à cet appareil.

C'est seulement ensuite qu'intervient la personnalisation de l'application Web, une fois que ces fonctionnalités **fondation** sont opérationnelles (créer des listes d'appareils, des scripts permettant d'enchaîner les instructions à la demande...)

### Majeures

- [ ] Chercher un appareil  
> Cette fonctionnalité n'est pas considérée comme acquise car le topic MQTT de l'objet doit être rentrée en dur dans le code python afin de pouvoir y transmettre des informations. Si jamais vous aviez à disposition une ampoule Zigbee dont vous connaissez le topic MQTT, vous pouvez tout à fait remplacer celui du code par le votre, et cela devrait fonctionner. 
- [x] Connecter un appareil  
- [x] Déconnecter un appareil  
- [x] Envoyer une instruction à l'appareil

### Mineures

- [ ] Ajouter une collection (appareils personnels)  
- [ ] Supprimer une collection (appareils personnels)  
- [ ] Ajouter une tâche (allumer, éteindre, activer, désactiver)  
- [ ] Supprimer une tâche  
- [ ] Scripter les tâches (exemple ampoules RGB, modes de couleurs)

