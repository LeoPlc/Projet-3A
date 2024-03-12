# CODES PYTHON

Ce dossier contient plusieurs versions du code python permettant de mettre en oeuvre l'application créée à la main. Avant d'exécuter ces codes, il faut s'assurer de la bonne installation sur votre machine des librairies suivantes : 

- paho-mqtt (messages MQTT pour intéragir avec l'ampoule Zigbee)

- rgbxy (librairie de conversion de format de codage de couleurs de rgb, format provenant de la roue de couleurs, à xy, format compris par l'ampoule Zigbee)

- tkinter (librairie permettant de générer des interfaces graphiques, roues de couleurs, etc.)

Dans chacun de ces dossiers, le code python à exécuter s'appelle 

    controller.py

Chaque code suit le principe de Model View controller afin de structurer le logiciel de manière robuste au travers de l'orienté objet, ce qui permet de standardiser les fonctions et objets nécessaires au développement de l'application.

Les différences entre les versions 1.0 - 1.1 et 1.2 - 1.2.1 de l'IoT_app est que les deux plus anciennes versions ne contiennent pas la classe ZigbeeToMQTT, conçue plus tard afin d'implanter une standardisation des objets Zigbee (dans l'optique de pouvoir instancier plusieurs ampoules si nécessaire pour commencer...)

Les différentes versions ne contiennent pas de changement majeur à part l'apparition de la classe ZigbeeToMQTT dans les deux dernières, elles ont plutôt un but de backup afin de conserver une version fonctionnelle de l'application, pour pouvoir poursuivre le développement de cette dernière en toute sérénité.

La dernière version de l'application située dans le dossier **IoT_App 1.2.1** a été commentée afin de décrire le fonctionnement du code.