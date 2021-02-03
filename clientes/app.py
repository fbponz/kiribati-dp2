import tweepy
import psycopg2
import json
import csv
import re

from kafka import KafkaConsumer

def extract(string, start='(', stop=')'):
    return string[string.index(start)+1:string.index(stop)]

def city_pick (beach, city, nature, party):
    data= {'Barcelona' : {'Beach': 3 , 'City' : 7, 'Nature' : 3, 'Party' : 6 },'Valencia': {'Beach': 5 , 'City' : 6, 'Nature' : 3, 'Party' : 5}, 'Sevilla': {'Beach': 1 , 'City' : 5, 'Nature' : 6, 'Party' : 6}, 'Bilbao': {'Beach': 4 , 'City' : 4, 'Nature' : 6, 'Party' : 5}, 'Oviedo' :{'Beach': 4 , 'City' : 3, 'Nature' : 7, 'Party' : 4}, 'Madrid': {'Beach': 0, 'City' : 7, 'Nature' : 5, 'Party' : 6}, 'Ibiza': {'Beach': 6 , 'City' : 2, 'Nature' : 4, 'Party' : 6}}
    lista_city = ['Barcelona', 'Valencia', 'Sevilla', 'Bilbao', 'Oviedo', 'Madrid', 'Ibiza']    
    ciudad_punt = lambda beach_rank, city_rank, nature_rank, party_rank, beach_sur, city_sur, nature_sur, party_sur: (beach_rank*beach_sur)+(city_rank*city_sur)+(nature_rank*nature_sur)+(party_rank*party_sur)
    res = 0
    res_prev = 0
    Ciudad = 'Barcelona'
    for act_city in lista_city:
        res = ciudad_punt(data[act_city]['Beach'],data[act_city]['City'],data[act_city]['Nature'],data[act_city]['Party'],beach,city,nature,party)
        if(res > res_prev):
            res_prev=res
            Ciudad = act_city
    return Ciudad

def selectData(dbCursor, text_query):
    sqlSelect = text_query;
    dbCursor.execute(sqlSelect);
    rows = dbCursor.fetchall();
    return rows

def respuesta_tweet(nombre,codigo_casa,ciudad,id_tweet_cliente,inAPIKEY,inAPISECRETKEY,inACCESSTOKEN,inACCESSTOKENSCRET):
    auth = tweepy.OAuthHandler(inAPIKEY,inAPISECRETKEY)
    auth.set_access_token(inACCESSTOKEN,inACCESSTOKENSCRET)
    api=tweepy.API(auth)
    web ={'Barcelona':'https://bit.ly/2MAsRwS','Valencia':'https://bit.ly/2McyTEe','Bilbao':'https://bit.ly/2MCMlkr','Oviedo':'https://bit.ly/2L7Xx8q', 'Madrid':'https://bit.ly/39vjSWP', 'Ibiza':'https://bit.ly/3oCO5Ye','Sevilla':'https://bit.ly/36zSapU'} 
    img ={'Barcelona':'barcelona.jpg','Valencia':'valencia.jpg','Sevilla':'sevilla.jpg','Bilbao':'bilbao.jpg','Oviedo':'oviedo.jpg', 'Madrid':'madrid.jpg', 'Ibiza':'ibiza.jpg'}
    media = api.media_upload(img[ciudad])
    api.update_status("Hola {}! Disponemos de tu nueva casa en {}, El ID de la casa: {}. Para +info /DM {}".format(nombre,ciudad,codigo_casa,web[ciudad]), in_reply_to_status_id = '{}'.format(id_tweet_cliente),media_ids=[media.media_id],auto_populate_reply_metadata=True)

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
            data = list(map(int, re.findall(r'\d+', string_list))) 
            #data[0]-> Salary, data[2]-> Family members, data[3]-> Playa, data[4]-> Ciudad, data[5]-> Naturaleza, data[6]-> Party.
            name = string_list[11:string_list.find(",")]
            
            city_name = city_pick(data[3],data[4],data[5],data[6])
            flat_info = selectData(dbCursor,"select * from casas WHERE city_name='{}' AND  number_rooms>={} AND (monthly_cost) <=(0.3*({}/12))ORDER BY monthly_cost DESC LIMIT 1".format(city_name,data[2],data[0]));
            respuesta_tweet(name,flat_info[0][4],flat_info[0][1],record["id"][0],'{}'.format(vAPIKEY),'{}'.format(vAPISECRETKEY),'{}'.format(vACCESSTOKEN),'{}'.format(vACCESSTOKENSECRET))