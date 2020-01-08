import mysql.connector
import time
from tkinter import *
import WheelTest.CreateTest as CreateTest
# cursor = mydb.cursor()



class WheelTestGUI:
    def __init__(self, master):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="TCSJHp37*",
            database="deantesting"
        )
        self.cursor = self.mydb.cursor(buffered=True)

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

        self.entryserial = int()

        self.labelserial = Label(master, text="Serial Search")
        self.labelserial.grid(column=0, row=3)
        self.entryserial = Entry(master, textvariable=self.entryserial)
        self.entryserial.grid(column=1, row=3)
        button1 = Button(master, text="Show All Wheels", command=self.sqlselect_all)
        button1.grid(column=1, row=1)
        button2 = Button(master, text="Insert Stuff", command=self.listbox)
        button2.grid(column=2, row=1)
        self.button3 = Button(master, text="selectwhere", command= lambda: self.selectserial(self.entryserial.get()))
        self.button3.grid(column=3, row=3)
        self.button4 = Button(master, text="New Test", command=CreateTest.new_test)
        self.button4.grid(column=1, row=4)
        self.button4 = Button(master, text="Create Tables", command=self.create_tables)
        self.button4.grid(column=2, row=4)
        Button(master, text="CLOSE", command=master.destroy).grid(column=2, row=5)
        # cursor.execute("CREATE DATABASE deantesting")
        #cursor.execute("CREATE TABLE wheelid (id INT AUTO_INCREMENT PRIMARY KEY, serial INT(10), orderno INT(10), wheeltype VARCHAR(255), datecreate DATE, dateupdate DATE, customer VARCHAR(255))")
        #cursor.execute("SELECT * FROM wheelid")
        #cursor.execute("SHOW TABLES")
        # try:
        #   cursor.execute("INSERT INTO wheelid (serial, orderno, wheeltype, datecreate, dateupdate) VALUES (%s,%s,%s,%s,%s)", (serial, orderno, wheeltype, datecreate, dateupdate))
        # except mysql.connector.Error as err:
        #   print("***ERROR***: {}".format(err))
        # mydb.commit()
        # #cursor.execute()
        # cursor.execute("SELECT * FROM wheelid")
        #
        # for x in cursor:
        #   print(x)

    def create_tables(self):
        try:
            self.cursor.execute("CREATE TABLE wheelid (id INT AUTO_INCREMENT PRIMARY KEY, serial INT(10), orderno INT(10), wheeltype VARCHAR(255), datecreate DATE, dateupdate DATE)")
            self.cursor.execute("CREATE TABLE wheelid (id INT AUTO_INCREMENT PRIMARY KEY, serial INT(10), orderno INT(10), wheeltype VARCHAR(255), datecreate DATE, dateupdate DATE)")
        except mysql.connector.Error as err:
            self.popupmsg("ERROR CREATING TABLES: {}".format(err))

    def sqlselect_all(self):
        self.cursor.execute("SELECT * FROM wheelid")
        for x in self.cursor:
            print(x)
            self.listbox(x)

    def popupmsg(self,msg):
        popup = Tk()
        popup.wm_title("!")
        label = Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Okay", command=popup.destroy)
        B1.pack()
        popup.mainloop()

    def listbox(self, msg):
        listbox = Tk()
        listbox1 = Listbox(listbox, width=80)
        listbox1.pack()
        listbox1.insert(END, msg)
        B1 = Button(listbox, text="Okay", command=listbox.destroy)
        B1.pack()
        listbox.mainloop()

    def selectserial(self, serialno):
        self.cursor.execute("SELECT * FROM wheelid WHERE serial=%s", (serialno,))
        for x in self.cursor:
            if len(x) == len(serialno):
                self.popupmsg("ERROR with serial: " + serialno)
                print("ERROR WITH SERIAL: " + serialno)
            else:
                self.listbox(x)
        print(serialno)

    def add_results(self):
        try:
            self.cursor.execute("INSERT INTO wheelid (serial, orderno, wheeltype, datecreate, dateupdate) VALUES (%s,%s,%s,%s,%s)", (, orderno, wheeltype, datecreate, dateupdate))
        except Exception:
            self.popupmsg("COULD NOT SAVE")
            print("COULD NOT SAVE")




root = Tk()
gui=WheelTestGUI(root)
root.mainloop()