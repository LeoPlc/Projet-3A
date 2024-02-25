# SMART HOME APPLICATION

Ce projet consiste à concevoir étape par étape une application permettant d'interconnecter divers objets connectés, existants sur le marché. Cette application est décortiquée et présentée dans ce répertoire GitHub, afin d'en comprendre les différents aspects et objectifs. 

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

### DIAGRAMME BÊTE A CORNE


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
- [ ] Connecter un appareil  
- [ ] Déconnecter un appareil  
- [ ] Envoyer une instruction à l'appareil

### Mineures

- [ ] Ajouter une collection (appareils personnels)  
- [ ] Supprimer une collection (appareils personnels)  
- [ ] Ajouter une tâche (allumer, éteindre, activer, désactiver)  
- [ ] Supprimer une tâche  
- [ ] Scripter les tâches (exemple ampoules RGB, modes de couleurs)


## 4-DESCRIPTION DES CODES PYTHON

Ici sont présentés les codes qui conçoivent l'application Web permettant de se connecter aux différents appareils. L'application a été développée en **python** à l'aide des bibliothèques **django**, **2**, et **3**. Le code s'articule de la manière suivante.

## 5- INSTALLATION ET UTILISATION DU BROKER MQTT 

### Installation sur raspberry pi

Dans un premier temps installer les librairies nécessaires pour utiliser le broker mqtt:

    sudo apt-get install mosquitto mosquitto-clients

Brancher le broker mqtt au raspberry et vérifier sa détection par la commande 

    lsusb

Normalement, si le broker est bien détecté, le terminal de commande devrait afficher une ligne similaire à celle-ci (dans notre cas, le broker utilisé est de la marque SONOFF)

    Bus 001 Device 002: ID 1a86:55d4 QinHeng Electronics SONOFF Zigbee 3.0 USB Dongle Plus V2

Pour continuer, il faut s'assurer d'avoir nodejs.

> une version compatible est celle présentée ci-dessous, mais si une version plus récente fonctionne, il est tout à fait possible de s'en servir. Le contexte présenté est un contexte fonctionnel au moment où ce projet a été mené.

La version visée de nodejs est la version 16.18.1. Pour installer la dernière version de nodejs, la commande est:

    sudo apt install -y nodejs

Il est possible de spécifier la version souhaitée via: 

    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash

Puis 

    nvm install 16.18.1

Ensuite 

    nvm use 16.18.1


Et enfin 

    nvm alias default 16.18.1

Cette méthode peut-être adapté aux autres versions souhaitées de nodejs.

Il faut aussi s'assurer de la présence de git, make, g++ et gcc via 

    sudo apt-get install git make g++ gcc

Une fois ces étapes passées, il faut configurer zigbee2mqtt de la manière suivante. Il faut tout d'abord créer un répertoire comme suit : 

    sudo mkdir /opt/zigbee2mqtt

Il faut faire en sorte de ne pas nécessiter l'utilisation de "sudo" à l'intérieur de ce répertoire afin de pouvoir plus tard y intéragir avec des scripts (qui serviront à lancer automatiquement le service zigbee2mqtt à l'allumage du raspberry pi). Il faut utiliser la commande telle quelle:

    sudo chown -R ${USER}: /opt/zigbee2mqtt


Il faut ensuite cloner le répertoire git suivant: 

    git clone --depth 1 https://github.com/Koenkk/zigbee2mqtt.git /opt/zigbee2mqtt

Il est ensuite nécessaire de se placer dans le répertoire en question :

    cd /opt/zigbee2mqtt

Vérifier la présence de npm et sa version via 

    npm -v

Si npm n'est pas installé il faut utiliser la commande 

    sudo apt-get install npm

Et effectuer la commande suivante: 

    npm ci


Une fois ceci-fait, il faut éditer le fichier de configuration placé dans le dossier /opt/zigbee2mqtt/data

    sudo nano data/configuration.yaml

et y inscrire ce qui suit. Il faut tout d'abord remplacer ce qui suit 'base_topic' par ce qui suit :

    zigbee

au lieu de 

    zigbee2mqtt

Il faut ensuite inscrire les lignes tout en bas, la dernière ligne étant 'port: /dev/ttyACM0' cela devrait ressembler à ce qui suit: 

        port: /dev/ttyACM0
        adapter: ezsp
    frontend: 
        port: 8080

Sauvegarder avec **ctrl + s** et quitter avec **ctrl + x**. Il faut ensuite lancer la commande suivante en étant placé dans le dossier /opt/zigbee2mqtt:

    npm start

Normalement, le terminal devrait afficher 


### Installation pour Mac

Installer la librairie mosquitto: 

    brew install mosquitto

Le fichier de configuration est stocké dans le dossier 

    /opt/homebrew/etc/mosquitto/mosquitto.conf

Pour lancer les services mosquitto:

    brew services start mosquitto

Une fois ces étapes effectuées on peut utiliser les fonctions mosquitto telles que:

    mosquitto_sub 

Permettant de s'abonner à un sujet (fait partie du protocole Zigbee)

### Test de la librairie mosquitto

Pour pouvoir tester le fonctionnement de mosquitto, on peut ouvrir deux terminaux de commande. 
Dans le premier terminal, écrire la commande: 

    mosquitto_sub -t topic/state

Dans le second écrire la commande: 

    mosquitto_pub -t topic/state -m "hello world"

Le texte **"Hello world"** devrait s'afficher dans le premier terminal.

### Liens utilisés :

- Lien vers un [article d'installation de mosquitto sur Mac](https://subscription.packtpub.com/book/iot-and-hardware/9781787287815/1/ch01lvl1sec12/installing-a-mosquitto-broker-on-macos).
- Deuxième [lien pour l'installation sur Mac](https://gist.github.com/KazChe/6bcafbaf29e10a7f309d3ca2e2a0f706)
- Version [vidéo pour Mac](https://www.youtube.com/watch?v=AD1YvjmRiR4).

## BIBLIOGRAPHIE / LIENS UTILES

#### "HOW TO CREATE AN IOT APP" 

https://waverleysoftware.com/blog/how-to-create-an-iot-app/

Structure de l'application selon ce site : 

![iotAppStructure](img/appStructure.png)

### WEB APPLICATION

#### ZIGBEE TO MQTT

https://www.youtube.com/watch?v=frwhcYQKElU
