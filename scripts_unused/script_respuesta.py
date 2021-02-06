# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:08:46 2021

@author: luisl
"""

import os


os.chdir("C:\\Users\\luisl\\Desktop\\dp2")


import tweepy



consumer_key='Y8eWq1BmLI4xbuw5Hf8z4p1EM',
consumer_secret='rauMvra1HiJUSlqfUxxA1YVRTuUZBxPLRAgs6HWejpmicuJf9W'
access_token='1346029085475172357-NYbkyxPGbkHVC6p6O2ENYHCyiCcgel'
access_token_secret='pbXCFU4UwsTZdaxC49Jfsfk211DEbauXtJQFRI6ZIIZ1J'

auth = tweepy.OAuthHandler('Y8eWq1BmLI4xbuw5Hf8z4p1EM','rauMvra1HiJUSlqfUxxA1YVRTuUZBxPLRAgs6HWejpmicuJf9W')
auth.set_access_token('1346029085475172357-NYbkyxPGbkHVC6p6O2ENYHCyiCcgel','pbXCFU4UwsTZdaxC49Jfsfk211DEbauXtJQFRI6ZIIZ1J')
api=tweepy.API(auth)


try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


api.update_status("respuesta_algoritmo", in_reply_to_status_id = '1353369862786179072',auto_populate_reply_metadata=True)

























