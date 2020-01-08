import mysql.connector
from WheelTestGUI import *


#cursor = mydb.cursor(buffered=True)
def insert_new_test():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="TCSJHp37*",
        database="deantesting"
    )
    cursor = mydb.cursor(buffered=True)

    serial = 12345
    orderno = 112233
    wheeltype = "Saturn"
    datecreate = time.strftime('%Y-%m-%d %H:%M:%S')
    dateupdate = time.strftime('%Y-%m-%d %H:%M:%S')
    # print(datecreate)
    # print(dateupdate)
    # print(mydb)

def sqlselect_all():
    WHeelTestGUI.cursor.execute("SELECT * FROM wheelid")
    for x in WheelTestGUI.cursor:
        print(x)
        WheelTestGui.list_box(x)