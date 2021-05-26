


import mysql.connector
from mysql.connector import Error

def connect_insert():
    '''function to connect and insert a row in a database '''

#create a connection variable
conn = None

try:
    conn = mysql.connector.connect(host='localhost',database = 'king2db',user='root',password ='1234')
    print("connecting to database")
    if conn.is_connected:
        print('connected to database server')

        db_cursor=conn.cursor()
        #create a list variable to contain the sqlto the executed 
        sql="insert into movies(title,release_year,genre,collections_in_mill)values(%s,%s,%s,%s)"
        
            
        #create a list variable to contain all the values we want to insert into the human table
       
        var=[]
        for counter in range(1):
            title=input("enter the movie title")
            release_year=input("enter the release_year")
            genre=input("enter genre")
            collections_in_mill= input("enter collections_in_mill")
            var.append((title,release_year,genre,collections_in_mill))


          

        #execute the query using the executemany function
        db_cursor.executemany(sql, var)
       
        #print a success messag
        conn.commit()

        #print a success message
        print(db_cursor.rowcount, 'rows was inserted')
        
     
    
        #close the cursor
        db_cursor.close 

except Error as e:
         print("Connecting failed due to the following",e)
finally:
    if conn is not None and conn.is_connected:
            conn.close
            print("Disconnected from the database")

#call the function
            connect_insert()


