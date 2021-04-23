#connect to a database and insert data


import mysql.connector
from mysql.connector import Error

def connect_insert():
    '''function to connect and insert a row in a database '''

#create a connection variable
conn = None

try:
    conn = mysql.connector.connect(host='localhost',database = 'demo',user='root',password ='1234')
    print("connecting to database")
    if conn.is_connected:
        print('connected to database server')

        db_cursor=conn.cursor()
        #create a list variable to contain the sqlto the executed 
        sql ="insert into Human (humanId,name,color,gender,bloodgroup) Values(%s,%s,%s,%s,%s)"



        #create a list variable to contain all the values we want to insert into the human table

        val = [
            ('1013','Hannah','White','Female','B-'),
            ('1014','Michael','brown','Male','O-'),
            ('1015','Sunday','black','female','B+') 
        ]

        #execute the query using the executemany function
        db_cursor.executemany(sql, val)
       
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

