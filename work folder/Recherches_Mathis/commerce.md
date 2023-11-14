MQTT (Message Queuing Telemetry Transport) est un protocole de communication léger et basé sur le modèle de publication/abonnement (pub/sub). Il a été développé à l'origine en 1999 par IBM et est largement utilisé dans l'Internet des objets (IoT), les systèmes de capteurs, la domotique et d'autres applications qui nécessitent une communication efficace entre de multiples appareils.

Voici quelques caractéristiques clés du protocole MQTT :

    Légèreté : MQTT est conçu pour être léger et minimiser la surcharge du réseau. Il utilise un en-tête réduit et un format binaire, ce qui le rend efficace pour les appareils ayant des ressources limitées en termes de bande passante et de puissance de calcul.

    Modèle de publication/abonnement : MQTT utilise un modèle de communication de type pub/sub. Dans ce modèle, les appareils (appelés clients MQTT) se connectent à un serveur MQTT, également connu sous le nom de courtier (broker). Les clients peuvent publier des messages sur des « sujets » et s'abonner à des sujets pour recevoir des messages. Le courtier sert d'intermédiaire pour distribuer les messages aux clients abonnés aux sujets pertinents.

    Qualité de service (QoS) : MQTT offre plusieurs niveaux de qualité de service pour garantir que les messages sont transmis de manière fiable entre les clients et le courtier. Il existe trois niveaux de QoS : 0 (au plus une fois), 1 (au moins une fois) et 2 (exactement une fois).

    Retrait et dernier message conservé : MQTT permet aux clients de s'abonner à un sujet spécifique et de recevoir le dernier message publié sur ce sujet. Il prend également en charge la rétention de messages, ce qui signifie que le courtier peut conserver le dernier message publié sur un sujet pour que les nouveaux abonnés le reçoivent dès leur inscription.

    Sécurité : MQTT peut être configuré pour utiliser des mécanismes de sécurité tels que TLS/SSL pour chiffrer les communications entre les clients et le courtier. Il offre également des mécanismes d'authentification pour garantir que seuls les clients autorisés peuvent publier ou s'abonner à des sujets.

    Diversité des applications : MQTT est utilisé dans une variété d'applications, notamment la surveillance à distance, la gestion de flottes de véhicules, la télémétrie, la domotique, le suivi d'actifs, les systèmes de contrôle, etc.

MQTT est largement adopté en raison de sa simplicité, de sa légèreté et de sa fiabilité, ce qui en fait un choix populaire pour les applications IoT et M2M (Machine-to-Machine). Il existe de nombreuses implémentations de serveurs MQTT open source et commerciales, ainsi que des bibliothèques clientes pour une variété de langages de programmation.


https://github.com/Koenkk/zigbee2mqtt

https://www.zigbee2mqtt.io/devices/ZB_A60_RGBCW.html

https://www.zigbee2mqtt.io/



# Connexion Zigbee2MQTT

Après le cours sur les IOT, j'ai demandé au prof de nous aider sur le sujet. 
Il m'a envoyé cette vidéo : [Tuto Zigbee to MQTT](https://www.youtube.com/watch?v=frwhcYQKElU).

Il m'a de plus indiqué un rapport d'anciens élèves sur un sujet un peu similaire. 

Nous savons maintenant comment connecter nos produits Zigbee a notre raspberry. 
Nous pouvons donc nous ataquer aux produits à acheter. 

- [Passerelle Zigbee](https://www.amazon.fr/SONOFF-EFR32MG21-Coordinator-Universelle-Passerelle/dp/B0B6P22YJC?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1J8B31DEB9NS3&keywords=sonoff+zigbee+3.0+usb&qid=1667371853&qu=eyJxc2MiOiIwLjQ5IiwicXNhIjoiMC41NyIsInFzcCI6IjAuNjUifQ%3D%3D&sprefix=sonoff+zigbee+3.0+us,aps,322&sr=8-6&linkCode=sl1&tag=aceinternet02-21&linkId=a271fdc1d9b58cecb783682fbb1df9af&language=fr_FR&ref_=as_li_ss_tl)

- [Capteur de température Zigbee](https://www.amazon.fr/Aqara-Temperatur-Luftfeuchtigkeits-Luftdrucksensor-Homekit/dp/B07D37FKGY/ref=sr_1_2_sspa?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=32H5YNFBFTYF1&keywords=capteur+xiaomi+zigbee&qid=1699609343&sprefix=capteur+xiaomi+zigbee%2Caps%2C69&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)

- 


