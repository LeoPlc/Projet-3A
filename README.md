# SMART HOME APPLICATION

Ce projet consiste à concevoir étape par étape une application permettant d'interconnecter divers objets connectés, existants sur le marché. Cette application est décortiquée et présentée dans ce répertoire GitHub, afin d'en comprendre les différents aspects et objectifs. 

Lien vers la vidéo explicative du projet: [cliquez ici](https://www.youtube.com/watch?v=c5vRu4_OLxM). Notre vidéo vient en complément de notre dépôt. N'hésitez donc pas à la visionner pour mieux comprendre notre projet. 

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

> Dossier [demo](demo) : Ce dossier permet de retrouver la partie démonstration de notre projet. Cela comprend donc l'explication de la réalisation de notre maquette.  

Afin d'éxécuter notre projet, vous pouvez donc vous rendre dans le dossier [work](work).