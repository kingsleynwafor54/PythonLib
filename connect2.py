#connect to mysql database using python and retrieve some data


#import the needed  packages
import mysql.connector
from mysql.connector import Error

#define the connector function
def connect_fetch():
    '''function to connect and fetch rows in a database'''

    #create a variable for the connector object
    conn = None
    try:
      #  conn = mysql.connector.connect(host ='localhost',database ='cape_codd',user='King_chudi',password ="1234")
        conn = mysql.connector.connect(host ='localhost',database ='demo',user='root',password ="1234")
        print('Connecting to database server')
        if conn.is_connected:
            print("Connected to database server")

            #select Query
            sql_select_query= 'select * from human'
            cursor = conn.cursor()
            cursor.execute(sql_select_query)
            records=cursor.fetchall()
            print("Total numberof rows in Human is : ", cursor.rowcount)

            #display the output data
            print ("\n Printing each human record")
            for row in records:
                print("HumanId :", row[0])
                print("Name ",row[1])
                print("color:",row[2])
                print("gender:",row[3],"\n")

    except Error as e:
        print("Not connecting due to: ",e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Database shutdown")




     
connect_fetch()


