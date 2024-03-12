# INSTALLATION ET UTILISATION DU BROKER MQTT 

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