import mysql.connector
import time


datecreate = time.strftime('%Y-%m-%d %H:%M:%S')
dateupdate = time.strftime('%Y-%m-%d %H:%M:%S')


class DatabaseCommands:

    def __init__(self):
        self.cursor = mydb.cursor(buffered=True)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="TCSJHp37*",
        database="deantesting"
    )
    #cursor = mydb.cursor(buffered=True)


    def sqlselect_all(self):
        self.cursor.execute("SELECT * FROM wheelid")
        for x in self.cursor:
            print(x)
            popupboxes.listbox(x)

    def insert_new_data():

        self.cursor.execute("INSERT INTO wheelid (serial, orderno, wheeltype, datecreate, dateupdate) VALUES (%s,%s,%s,%s,%s)", (TS.serialwheel.get(), asasd , serial  , datecreate, dateupdate))

