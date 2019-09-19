# Sentiment analysis using twitter streaming API

The purpose of this project is to use the streaming API of twitter to analyse tweets using python with tweepy and TextBlob librairie.
The tweets are stored in an ElasticSearch instance, and used by Kibana to display result in real time.
The project ship with a docker integration in order to ease the reusabilty for demo purpose.
# Dashboard example
Here is an example of a dashboard



# How to use the application



## Requirements

- Docker
- Docker compose
- A Twitter developper acount for token API key
- An API token from mapbox used for geocoding 

## Configuration
Once you have cloned the repo, you will have to edit the **api.env**. This file is used to inject variable to the program.
### Twitter keys
In order to connect to the steaming API you will need to fill the following env variables with your twitter keys that you can found in [your twitter app dashboard ](https://developer.twitter.com/en/apps):
- TWITTER_APP_KEY (API key)
- TWITTER_APP_SECRET (API secret key)
- TWITTER_KEY (Access token)
- TWITTER_SECRET (Access token secret)

### Geocode Token
In order to geolocate the tweets location, the python part of the app use geocoder package. Actually the app use mapbox as provider.  To activate the geolocation you need to fill the following env variable
 - GEOCODE_TOKEN


### Track terms
The **TRACK_TERMS** env variable defines the list of terms you want to track in your stream. It has to be in JSON array of strings.
*Example: ["your first term", "your second term"]*

### Defining the shape of the tweet 
You have to define the document that is going to be store in the elasticsearch instance. This is done by the following two step



### First select the attributs to be parsed
The **TWEETS_ATTRS** take a JSON array of attributs of status object, here is an example of tweet object collected through the streaming API, more info [here](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object).
 
  

       {
    "created_at": "Thu Apr 06 15:24:15 +0000 2017",
    "id_str": "850006245121695744",
    "text": " Today we are sharing our vision for the future of the Twitter API platform!\nhttps:\/\/t.co\/XweGngmxlP",
    "user": {
      "id": 2244994945,
      "name": "Twitter Dev",
      "screen_name": "TwitterDev",
      "location": "Paris",
      "url": "https:\/\/dev.twitter.com\/",
      "description": "Your official source for Twitter Platform news, updates & events. Need technical help? Visit https:\/\/twittercommunity.com\/ \u2328\ufe0f #TapIntoTwitter"
    },
    "place": {   
    },
    "entities": {
      "hashtags": [      
      ],
      "urls": [
        {
          "url": "https:\/\/t.co\/XweGngmxlP",
          "unwound": {
            "url": "https:\/\/cards.twitter.com\/cards\/18ce53wgo4h\/3xo1c",
            "title": "Building the Future of the Twitter API Platform"
          }
        }
      ],
      "user_mentions": [     
      ]
    }}

  **NB:**
  

 - To access nested attributs like user location it has to be a string in the following format `'user.attribut'`
 - sentiment attribut doesn't need to be included


### Then define the Elasticsearch mapping to fit the TWEETS_ATTRS

First you will need to define a INDEX_NAME
You will need to pass a JSON object defining you mapping to the INDEX_MAPPING en variable, here is the structure of the JSON object

TWEETS_ATTRS=["text","user.location"]

 INDEX_MAPPING=

    {"mappings": {"tweet":{"properties": {"sentiment":{"type": "keyword"},"text":{"type": "text"},"user.location":{"type": "geo_point"}}}}}


## Start the app

Once you have defined the configuration file:

1. Open a terminal and place you to the root directory
2. Run `docker-compose build`
3. Run `docker-compose up`
4. Open a browser, and go to [http://localhost:5601](http://localhost:5601/)
5. On left navigation drawer click on management
6. Define an index pattern that match your INDEX_NAME variable
7. You can now create and explore data by clicking on the left navigation drawer explore or visualize buttons