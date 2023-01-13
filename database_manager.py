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
       insertQuery  = "INSERT INTO credentials VALUES (?,?)"
       cursor.execute(insertQuery,(username,passhash))
       sqliteConnection.commit()
# Handle errors
   except sqlite3.Error as error:
      sys.stderr.write("Error occured with adding login {}".format(error)) 
   # Close DB Connection irrespective of success
   # or failure
   finally:
       if sqliteConnection:
           sqliteConnection.close()
