# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:18:53 2021

@author: marco
"""

#%%

def city_pick (beach, city, nature, party):
    
    data_ciudad = {'Barcelona' : {'Beach': 6 , 'City' : 7, 'Nature' : 3, 'Party' : 6 },'Valencia': {'Beach': 6 , 'City' : 6, 'Nature' : 3, 'Party' : 6}, 'Sevilla': {'Beach': 1 , 'City' : 5, 'Nature' : 3, 'Party' : 5}, 'Bilbao': {'Beach': 3 , 'City' : 4, 'Nature' : 6, 'Party' : 4}, 'Oviedo' :{'Beach': 3 , 'City' : 2, 'Nature' : 7, 'Party' : 3}, 'Madrid': {'Beach': 0, 'City' : 7, 'Nature' : 5, 'Party' : 6}, 'Ibiza': {'Beach': 6 , 'City' : 2, 'Nature' : 4, 'Party' : 7}}
    lista_ciudades = ["Barcelona", "Valencia", "Bilbao", "Oviedo" , "Madrid", "Ibiza"]
    cities_scores = []
    
    barcelona_score = data_ciudad['Barcelona']['Beach'] * beach + data_ciudad['Barcelona']['City'] * city + data_ciudad['Barcelona']['Nature'] * nature + data_ciudad['Barcelona']['Party']
    valencia_score = data_ciudad['Valencia']['Beach'] * beach + data_ciudad['Valencia']['City'] * city + data_ciudad['Valencia']['Nature'] * nature + data_ciudad['Valencia']['Party']
    bilbao_score = data_ciudad['Bilbao']['Beach'] * beach + data_ciudad['Bilbao']['City'] * city + data_ciudad['Bilbao']['Nature'] * nature + data_ciudad['Bilbao']['Party']
    oviedo_score = data_ciudad['Oviedo']['Beach'] * beach + data_ciudad['Oviedo']['City'] * city + data_ciudad['Oviedo']['Nature'] * nature + data_ciudad['Oviedo']['Party']
    madrid_score = data_ciudad['Madrid']['Beach'] * beach + data_ciudad['Madrid']['City'] * city + data_ciudad['Madrid']['Nature'] * nature + data_ciudad['Madrid']['Party']
    ibiza_score = data_ciudad['Ibiza']['Beach'] * beach + data_ciudad['Ibiza']['City'] * city + data_ciudad['Ibiza']['Nature'] * nature + data_ciudad['Ibiza']['Party']
    
    cities_scores.append(barcelona_score)
    cities_scores.append(valencia_score)
    cities_scores.append(bilbao_score)
    cities_scores.append(oviedo_score)
    cities_scores.append(madrid_score)
    cities_scores.append(ibiza_score)
    
    
    new_dict = dict(zip(lista_ciudades, cities_scores))
    max_key = max(new_dict, key=new_dict.get)

    
    return max_key
#%%

# PRUEBA AQUÍ CAMBIANDO LOS NÚMEROS

print(city_pick(3, 5, 9 ,9))

#%%

reset -f

#%%



    
