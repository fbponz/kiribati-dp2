#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 01:01:31 2021

@author: franciscodeborjaponz
"""

def city_pick (beach, city, nature, party):
    #data_ciudad = {'Barcelona' : {'Beach': 1 , 'City' : 6, 'Nature' : 2, 'Party' : 4},'Valencia': {'Beach': 1 , 'City' : 5, 'Nature' : 4, 'Party' : 4}, 'Sevilla': {'Beach': 0 , 'City' : 5, 'Nature' : 3, 'Party' : 5}, 'Bilbao': {'Beach': 1 , 'City' : 2, 'Nature' : 6, 'Party' : 2}, 'Oviedo' :{'Beach': 1 , 'City' : 2, 'Nature' : 7, 'Party' : 1}, 'Madrid': {'Beach': 0, 'City' : 7, 'Nature' : 3, 'Party' : 4}, 'Ibiza': {'Beach': 1 , 'City' : 0, 'Nature' : 5, 'Party' : 7}}
    
    data_ciudad = {'Barcelona' : {'Beach': 4 , 'City' : 7, 'Nature' : 3, 'Party' : 5 },'Valencia': {'Beach': 5 , 'City' : 6, 'Nature' : 3, 'Party' : 5}, 'Sevilla': {'Beach': 1 , 'City' : 5, 'Nature' : 3, 'Party' : 5}, 'Bilbao': {'Beach': 3 , 'City' : 4, 'Nature' : 6, 'Party' : 5}, 'Oviedo' :{'Beach': 3 , 'City' : 2, 'Nature' : 7, 'Party' : 3}, 'Madrid': {'Beach': 0, 'City' : 7, 'Nature' : 5, 'Party' : 5}, 'Ibiza': {'Beach': 6 , 'City' : 2, 'Nature' : 4, 'Party' : 6}}
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

Bcn=0
Vlc=0
Blb=0
Ovd=0
Mdr=0
Ibz=0
Inv=0
total=0

for beachr in range(0,11):
    for cityr in range(0,11):
        for naturer in range(0,11):
            for partyr in range(0,11):
                res = city_pick(beachr, cityr, naturer, partyr)
                if res == "Barcelona":
                    Bcn+=1
                elif res == "Valencia":
                    Vlc+=1
                elif res == "Bilbao":
                    Blb+=1
                elif res == "Oviedo":
                    Ovd+=1
                elif res == "Madrid":
                    Mdr+=1
                elif res == "Ibiza":
                    Ibz+=1
                else:
                    Inv+=1
                total+=1

print(Bcn)
print(Vlc)
print(Blb)
print(Ovd)
print(Mdr)
print(Ibz)
print(Inv)
print(total)







