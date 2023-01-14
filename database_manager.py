import sqlite3
import sys

def addToDB(username, passhash):
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


def viewFromDB():
   try:
      # Connect to DB and create a cursor
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()
        selectQuery = "SELECT username, passhash FROM credentials"
        cursor.execute(selectQuery)
        result = cursor.fetchall()
        return result
   # Handle errors
   except sqlite3.Error as error:
      sys.stderr.write("Error occured with adding login {}".format(error)) 
   # Close DB Connection irrespective of success
   # or failure
   finally:
       if sqliteConnection:
           sqliteConnection.close()

def  masterStore(passhash):
    try:
      # Connect to DB and create a cursor
      sqliteConnection = sqlite3.connect('sql.db')
      cursor = sqliteConnection.cursor()

        ## create table if  not exist
      createQuery = "CREATE TABLE IF NOT EXISTS dontTouch (pass BLOB)"
      cursor.execute(createQuery)
       ## Insert master password sha256 hash
      insertQuery  = "INSERT INTO dontTouch VALUES (?)"
      cursor.execute(insertQuery,(bytes.fromhex(passhash),))
      sqliteConnection.commit()
    # Handle errors
    except sqlite3.Error as error:
       sys.stderr.write("Error occured with adding login {}".format(error)) 
   # Close DB Connection irrespective of success
   # or failure
    finally:
      if sqliteConnection:
         sqliteConnection.close()

def masterRetrieve():
   try:
      conn = sqlite3.connect("sql.db")
      cursor = conn.cursor()

# Retrieve the hex value from the 'data' column
      cursor.execute("SELECT HEX(pass) FROM dontTouch")
      result = cursor.fetchone()
      return result[0]
   # Handle errors
   except sqlite3.Error as error:
      sys.stderr.write("Error occured with adding login {}".format(error)) 
   # Close DB Connection irrespective of success
   # or failure
   finally:
      if conn:
         conn.close()
