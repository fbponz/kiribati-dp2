# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 17:26:23 2021

@author: marco
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:41:25 2021

@author: marco
"""

import json
import csv
import pandas as pd



#%%

json_path = 'C:/DEV/kiribati-dp2/anuncio_casa.json'
with open(json_path) as json_file:
        json_data = json.load(json_file)

#%%
print(json_data)
print(type(json_data["text"]))


#%%

string_list = json_data["text"]
words = string_list.split()
print(words)

print(len(words))

#%%


numeric_filter = filter(str.isdigit, words[17])
words[17] = "".join(numeric_filter)

print(words[17])
#%%
lista_tabla = ["ciudad", "habitaciones", "coste", "code"]

datos_anuncio = []
ciudad=[]


datos_anuncio.append(str(words[3]))
datos_anuncio.append(int(words[9]))
datos_anuncio.append(int(words[17]))
datos_anuncio.append(str(words[20]))



#%%

print(casa_dict) 

"""
 Diccionario con los key y value correspondientes de hacer merge (zip) de 
 las listas anteriores
                 
"""

#%%

pd.DataFrame.from_dict(data=casa_dict, orient='index') \
   .to_csv('dict_tweet.csv', header=False)
