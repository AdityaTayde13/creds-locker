import sqllite3
import sys

def add(username, passhash):
    try:
       # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()

        ## create table if  not exist

       createQuery = "CREATE TABLE IF NOT EXISTS credentials (username TEXT , passhash TEXT)"
       cursor.execute(createQuery)

       ## Insert encrypted username and password in the DB
       
