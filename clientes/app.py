import tweepy
import psycopg2
import json
import csv

from kafka import KafkaConsumer

def extract(string, start='(', stop=')'):
    return string[string.index(start)+1:string.index(stop)]

def city_pick (beach, city, nature, party):
    
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

def selectData(dbCursor, text_query):
    sqlSelect = text_query;
    dbCursor.execute(sqlSelect);
    rows = dbCursor.fetchall();
    return rows

def respuesta_tweet(nombre,codigo_casa,ciudad,id_tweet_cliente,inAPIKEY,inAPISECRETKEY,inACCESSTOKEN,inACCESSTOKENSCRET):
    auth = tweepy.OAuthHandler(inAPIKEY,inAPISECRETKEY)
    auth.set_access_token(inACCESSTOKEN,inACCESSTOKENSCRET)
    api=tweepy.API(auth)
    web ={'Barcelona':'https://bit.ly/2MAsRwS','Valencia':'https://bit.ly/2McyTEe','Bilbao':'https://bit.ly/2MCMlkr','Oviedo':'https://bit.ly/2L7Xx8q', 'Madrid':'https://bit.ly/39vjSWP', 'Ibiza':'https://bit.ly/3oCO5Ye'} 

    api.update_status("Hola {}, tenemos esta casa para ti en {}({}), el ID de la vivienda: {} ".format(nombre,ciudad,web[ciudad],codigo_casa), in_reply_to_status_id = '{}'.format(id_tweet_cliente),auto_populate_reply_metadata=True)

if __name__ == '__main__':

    vAPIKEY=''
    vAPISECRETKEY=''
    vACCESSTOKEN=''
    vACCESSTOKENSECRET=''

    with open('twitterkeys.csv', mode='r', ) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
    
        for row in csv_reader:
            vAPIKEY=row["APIKEY"]
            vAPISECRETKEY=row["APISECRETKEY"]
            vACCESSTOKEN=row["ACCESSTOKEN"]
            vACCESSTOKENSECRET=row["ACCESSTOKENSECRET"]

    dbSession = psycopg2.connect(user="kiriuser",
                                    password="kiripass",
                                    host="postgres",
                                    port="5432",
                                    database="kiritweet");
    
    dbCursor = dbSession.cursor(); 
    while True:
        consumer = KafkaConsumer('ClientesTK',bootstrap_servers=['broker:29092'])
        for msg in consumer:
            record = json.loads(msg.value)
            string_list = record["full_text"]
            words = string_list.split()
            numeric_filter = filter(str.isdigit, words[8])
            words[8] = "".join(numeric_filter)
            name = words[3]
            salary = words[8]
            num_family_members = words[19]
            hobby1 = int(extract(words[25]))
            hobby2 = int(extract(words[26]))
            hobby3 = int(extract(words[27]))
            hobby4 = int(extract(words[28]))
            
            city_name = city_pick(hobby1,hobby2,hobby3,hobby4)
            flat_info = selectData(dbCursor,"select * from casas WHERE city_name='{}' AND  number_rooms>={} AND (monthly_cost) <=(0.3*({}/12))ORDER BY monthly_cost DESC LIMIT 1".format(city_name,num_family_members,salary));
            respuesta_tweet(name,flat_info[0][4],flat_info[0][1],record["id"][0],'{}'.format(vAPIKEY),'{}'.format(vAPISECRETKEY),'{}'.format(vACCESSTOKEN),'{}'.format(vACCESSTOKENSECRET))