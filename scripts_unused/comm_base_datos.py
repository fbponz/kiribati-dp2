import psycopg2
 
dbSession = psycopg2.connect(user="kiriuser",
                                  password="kiripass",
                                  host="postgres",
                                  port="5432",
                                  database="kiritweet");

# Open a database cursor
 
dbCursor = dbSession.cursor(); 

def insertData(dbSession, dbCursor, text_query):
    sqlInsertRow1  = text_query; 
    # Insert statement
    dbCursor.execute(sqlInsertRow1);
    dbSession.commit()
    
def selectData(dbCursor, text_query):
    sqlSelect = text_query;
    dbCursor.execute(sqlSelect);
    rows = dbCursor.fetchall();
    return rows

    rows = dbCursor.fetchall();
# Insert statements
insertData(dbSession, dbCursor, "INSERT INTO casas (city_name, number_rooms, monthly_cost, code) values('New York City', 6, 514, 52643)") 

rows = selectData(dbCursor,"select * from casas WHERE city_name='New York City' ORDER BY id_casa DESC LIMIT 1");
print(rows[0][0])
print(rows[0][1])
print(rows[0][2])
print(rows[0][3])
print(rows[0][4])