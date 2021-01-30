import psycopg2
import json

from kafka import KafkaConsumer



def insertData(dbSession, dbCursor, text_query,v1,v2,v3,v4):
    sqlInsertRow1  = text_query; 
    # Insert statement
    dbCursor.execute(sqlInsertRow1,(v1,v2,v3,v4));
    dbSession.commit()

if __name__ == '__main__':

    dbSession = psycopg2.connect(user="kiriuser",
                                    password="kiripass",
                                    host="postgres",
                                    port="5432",
                                    database="kiritweet");
    dbCursor = dbSession.cursor(); 
    while True:
        consumer = KafkaConsumer('CasasTK',bootstrap_servers=['broker:29092'])
        for msg in consumer:
            
            record = json.loads(msg.value)
            string_list = record["text"]
            
            words = string_list.split()
            numeric_filter = filter(str.isdigit, words[17])
            words[17] = "".join(numeric_filter)
        
            insertData(dbSession, dbCursor, "INSERT INTO casas (city_name, number_rooms, monthly_cost, code) values(%s, %s, %s, %s)",words[3],words[9],words[17],words[20]) 
        