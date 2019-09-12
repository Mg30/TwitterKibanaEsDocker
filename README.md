# Docker_Kibana
POC qui permet d'initialiser un streaming à partir de l'API twitter et de visualiser avec kibana le tout sur un container docker

## Pré requis
- docker
- python 3.5
- Compte API developpeur sur twitter
 -Créer un compte sur une application de géocodage pa exemple ici : https://developer.mapquest.com/

## Utilisation 

1- Cloner le répo

2- Modifier le fichier Settings dans Streaming/python/file
  => Remplir les champs TWITTER_* avec les clés API de votre compte développeur.
  => Renseigner le TRACK_TERMS qui est le terme à rechercher pour le flux streaming.
  => Renseinger la clé d'API pour le geocodage
  

3-Ensuite placer vous dans le dossier docker_kibana en utilisant une console puis lancez la commande suivante :
  `docker-compose build`
  `docker-compose up`
  
6- Attendez un moment, puis tapez dans un navigateur internet http://localhost:5601/
  - Allez dans management
  - Index Patterns
  - Créer un nouveau index Pattern
  - Tapez tw*
  Vous pouvez désormais créer des visualisations en utilisant ce pattern
  
7- Pour arrêter l’application fermez la fenêtre d’où a été lancée l’application via docker-compose ou ctrl + C. 
  

  
