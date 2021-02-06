# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:07:03 2021

@author: marco
"""


import json
import csv
import pandas as pd
import re



#%%

json_path = 'C:/DEV/kiribati-dp2/tweet_cliente.json'
with open(json_path) as json_file:
        json_data = json.load(json_file)

#%%
print(json_data)
print(type(json_data["extended_tweet"]["full_text"]))

#%%
print(json_data["extended_tweet"]["full_text"])

string_list = json_data["extended_tweet"]["full_text"]
words = string_list.split()
print(words)

print(len(words))

#%%

numeric_filter = filter(str.isdigit, words[8])
words[28] = "".join(numeric_filter)

words[28]

#%%

### FUNCIÓN EXTRAER NÚMEROS ###

def extract(string, start='(', stop=')'):
        return string[string.index(start)+1:string.index(stop)]

#%%

lista_tabla = ["name", "salary", "age", "family" , "hobby1_ score", "hobby2_score", "hobby3_score", "hobby4_score"]

datos_clientes = []


datos_clientes.append(str(words[3]))
datos_clientes.append(int(words[8]))
datos_clientes.append(int(words[13]))
datos_clientes.append(int(words[19]))



datos_clientes.append(int(extract(words[25])))
datos_clientes.append(int(extract(words[26])))
datos_clientes.append(int(extract(words[27])))
datos_clientes.append(int(extract(words[28])))




cliente_dict = dict(zip(lista_tabla, datos_clientes))


#%%

print(casa_dict)
        
        
