import mysql.connector

from TestScreens_BACKUP import *


# cursor = mydb.cursor()
# from DatabaseHandler import DatabaseCommands as DB

TS = CreateTest()

class WheelTestGUI:
    def __init__(self, master):
        DB = database_stuff()
        serial = 12345
        orderno = 112233
        wheeltype = "Saturn"
        datecreate = time.strftime('%Y-%m-%d %H:%M:%S')
        dateupdate = time.strftime('%Y-%m-%d %H:%M:%S')
        # print(datecreate)
        # print(dateupdate)
        #print(mydb)
        # master.title
        self.master = master

        self.varentryserial = StringVar()
        self.labelserial = Label(master, text="Serial Search").grid(column=0, row=3)
        self.entryserial = Entry(master, textvariable=self.varentryserial).grid(column=1, row=3)
        button1 = Button(master, text="Show All Wheels", command=lambda: DB.sqlselect_all()).grid(column=1, row=1)
        button2 = Button(master, text="Insert Stuff", command=popupboxes.listbox).grid(column=2, row=1)
        self.button3 = Button(master, text="selectwhere", command=lambda: DB.selectserial(self.varentryserial.get()))
        self.button3.grid(column=3, row=3)
        self.button4 = Button(master, text="New Test", command=lambda: TS.new_test())
        self.button4.grid(column=0, row=4)
        self.button5 = Button(master, text="Create Tables", command=lambda: DB.create_tables())
        self.button5.grid(column=2, row=4)
        Button(master, text="CLOSE", command=master.destroy).grid(column=2, row=5)

class popupboxes:
    def popupmsg(msg):
        popup = Tk()
        popup.wm_title("!")
        print(msg)
        label = Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Okay", command=popup.destroy)
        B1.pack()
        popup.mainloop()

    def listbox(msg):
        listbox = Tk()
        listbox1 = Listbox(listbox, width=80)
        listbox1.pack()
        listbox1.insert(END, msg)
        B1 = Button(listbox, text="Okay", command=listbox.destroy)
        B1.pack()
        listbox.mainloop()

class database_stuff():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="TCSJHp37*",
            database="deantesting"
        )
        self.cursor = self.mydb.cursor(buffered=True)

    def selectserial(self, serialno):
        self.cursor.execute("SELECT * FROM wheelid WHERE serial=%s", (serialno,))
        rows = self.cursor.fetchall()
        if len(rows) == 0:
            print("BAD STUFF")
            print(serialno)
            popupboxes.popupmsg("SERIAL NOT FOUND: " + serialno)
            print("ERROR WITH SERIAL: " + serialno)
        else:
            for x in rows:
                print("Record Found: ")
                print(x)
                popupboxes.listbox(x)


    def add_results(self):
        print(TS.serialwheel.get(), TS.ordernumber.get(), TS.wheeltype.get(), TS.timenow.get(), TS.timenow.get())

    def sqlselect_all(self):
        self.cursor.execute("SELECT * FROM wheelid")
        for x in self.cursor:
            print(x)
            popupboxes.listbox(x)

    def insert_new_data(self, sqlcmd2):
        # self.cursor.execute("INSERT INTO wheelid (serial, orderno, wheeltype, datecreate, dateupdate) VALUES (%s,%s,%s,%s,%s)", (TS.serialwheel.get(), asasd , serial  , datecreate, dateupdate))
        self.cursor.execute(sqlcmd2)

    def create_tables(self):
        try:
            self.cursor.execute("SHOW TABLES")
            print(self.cursor.fetchall())
            self.cursor.execute("CREATE TABLE wheelid (id INT AUTO_INCREMENT PRIMARY KEY, serial INT(10), orderno INT(10), wheeltype VARCHAR(255), datecreate DATE, dateupdate DATE)")
        except mysql.connector.Error as err:
            self.cursor.execute("SHOW TABLES")
            print(self.cursor.fetchall())
            popupboxes.popupmsg(str(err))
        try:
            self.cursor.execute("CREATE TABLE section_1 (id INT AUTO_INCREMENT PRIMARY KEY, serial INT(10), CWLeft_0 "
                                "VARCHAR(255), CWRight_0 VARCHAR(255), CWCLeft_0 VARCHAR(255), CCWRight_0 VARCHAR("
                                "255), CWLeft_5 VARCHAR(255), CWRight_5 VARCHAR(255), CWCLeft_5 VARCHAR(255), "
                                "CCWRight_5 VARCHAR(255), CWLeft_9 VARCHAR(255), CWRight_9 VARCHAR(255), "
                                "CWCLeft_9 VARCHAR(255), CCWRight_9 VARCHAR(255), CWLeft_34 VARCHAR(255), CWRight_34 "
                                "VARCHAR(255), CWCLeft_34 VARCHAR(255), CCWRight_34 VARCHAR(255), CWLeft_22mm "
                                "VARCHAR(255), CWRight_22mm VARCHAR(255), CWCLeft_22mm VARCHAR(255), CCWRight_22mm "
                                "VARCHAR(255))")
        except mysql.connector.Error as err:
            self.cursor.execute("SHOW TABLES")
            print(self.cursor.fetchall())
            popupboxes.popupmsg(str(err))







root = Tk()
gui=WheelTestGUI(root)
root.mainloop()