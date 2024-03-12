# CODES PYTHON

Ce dossier contient plusieurs versions du code Python permettant de mettre en œuvre l'application créée à la main. Avant d'exécuter ces codes, il faut s'assurer de la bonne installation sur votre machine des bibliothèques suivantes : 

- `paho-mqtt` (pour les messages MQTT afin d'interagir avec l'ampoule Zigbee)

- `rgbxy` (bibliothèque de conversion de format de codage des couleurs de RGB, format provenant de la roue des couleurs, à XY, format compris par l'ampoule Zigbee)

- `tkinter` (bibliothèque permettant de générer des interfaces graphiques, roues des couleurs, etc.)

Dans chacun de ces dossiers, le code Python à exécuter s'appelle 

    controller.py

Chaque code suit le principe du Modèle-Vue-Contrôleur (MVC) afin de structurer le logiciel de manière robuste à travers la programmation orientée objet, ce qui permet de standardiser les fonctions et objets nécessaires au développement de l'application.

Les différences entre les versions 1.0 - 1.1 et 1.2 - 1.2.1 de l'`IoT_app` sont que les deux premières versions ne contiennent pas la classe `ZigbeeToMQTT`, conçue plus tard afin d'implanter une standardisation des objets Zigbee (dans l'optique de pouvoir instancier plusieurs ampoules si nécessaire pour commencer...).

Les différentes versions ne contiennent pas de changement majeur à part l'apparition de la classe `ZigbeeToMQTT` dans les deux dernières. Elles ont plutôt pour but de constituer une sauvegarde afin de conserver une version fonctionnelle de l'application, pour pouvoir poursuivre le développement de cette dernière en toute sérénité.

La dernière version de l'application, située dans le dossier **IoT_App 1.2.1**, a été commentée afin de décrire le fonctionnement du code.
