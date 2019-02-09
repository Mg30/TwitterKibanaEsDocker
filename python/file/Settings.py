#----------------------------------------------------------------------------------------------------------------------
#                                               FICHIER DE CONFIGURATION
#-----------------------------------------------------------------------------------------------------------------------
#********************Twitter creditencials******************************************************************************
#---------------------ENTREZ ICI VOS INFORMATIONS API DEVELOPEUR
TWITTER_APP_KEY = "" # Consumer Key (API Key)
TWITTER_APP_SECRET = "" # Consumer Secret (API Secret)
TWITTER_KEY = "" # Access Token
TWITTER_SECRET = "" # Access Token Secret
#***********************************************************************************************************************
#*********************************CONFIGURATION ELASTICSEARCH***********************************************************
ES_HOST = {"host": "elasticsearch", "port": 9200} # NE PAS CHANGER
INDEX_NAME = "tweeter" #METTRE ICI LE NOM DE INDEX
DOC_TYPE = "tweet" #NOM DU DOCUEMENT DE LINDEX

#*****************************GEOCODAGE*********************************************************************************
#----------------------------CLE POUR GEOCODAGE-------------------------------------------------------------------------
api_key = '' # ENTREZ ICI VOTRE CLE
#*****************************CONFIGURATION DU FLUX STREAMING***********************************************************
TRACK_TERMS = "#FRAURU" #TERME 0 TRACKER DANS LE FLUX TWITTER


