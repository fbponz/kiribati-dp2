# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:08:46 2021

@author: luisl
"""


import tweepy


auth = tweepy.OAuthHandler('Y8eWq1BmLI4xbuw5Hf8z4p1EM','rauMvra1HiJUSlqfUxxA1YVRTuUZBxPLRAgs6HWejpmicuJf9W')
auth.set_access_token('1346029085475172357-NYbkyxPGbkHVC6p6O2ENYHCyiCcgel','pbXCFU4UwsTZdaxC49Jfsfk211DEbauXtJQFRI6ZIIZ1J')
api=tweepy.API(auth)

id_tweet_cliente=1355197512638984192
nombre='Luis'
codigo_casa=6969
ciudad= 'Maguncia'


def respuesta_tweet(nombre,codigo_casa,ciudad,id_tweet_cliente):
    api.update_status("Hola {}, tenemos esta casa para ti {} en {}".format(nombre,codigo_casa,ciudad), in_reply_to_status_id = '{}'.format(id_tweet_cliente),auto_populate_reply_metadata=True)
    

respuesta_tweet(nombre,codigo_casa,ciudad,id_tweet_cliente)




















