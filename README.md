-# Docker_Kibana
POC qui permet d'initialiser un streaming à partir de l'API twitter et de visualiser avec kibana le tout sur un container docker


1- Installer docker

2- Créer un compte API developpeur sur twitter
  Créer un compte sur une application de géocodage pa exemple ici : https://developer.mapquest.com/


3- Copier le repository

4- Modifier le fichier Settings dans Streaming/python/file
  Remplir les champs TWITTER_* avec les clés API de votre compte développeur.
  Renseigner le TRACK_TERMS qui est le terme à rechercher pour le flux streaming.
  renseinger la clé api pour le geocodage
  

5-Ensuite placer vous dans le dossier docker_kibana en utilisant une console puis lancez la commande suivante :
  docker-compose build
  puis
  docker-compose up
  
6- Attendez un moment, puis tapez dans un navigateur internet http://localhost:5601/
  - Allez dans management
  - Index Patterns
  - Créer un nouveau index Pattern
  - Tapez tw*
  Vous pouvez désormais créer des visualisations en utilisant ce pattern
  
7- Pour arrêter l’application fermez la fenêtre d’où a été lancée l’application via docker-compose ou ctrl + C. 
  

  
