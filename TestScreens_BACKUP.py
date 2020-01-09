from tkinter import *
import time
from DatabaseHandler import *
#from WheelTestGUI import database_stuff

#VARIABLES
actualentries = []
expectedentries = []


class CreateTest:


    def new_test(self):

        self.newtestwindow = Toplevel()
        self.varPF = StringVar()
        self.choicePF = ("Pass", "Fail")
        self.choiceYN = ("Yes", "No", "N/A")
        self.choicewheel = ("Saturn", "Saturn GLO", "Saturn-Auto", "Other")
        self.choiceseparator = ("Standard", "Starburst", "Saturn-Auto", "Other")
        self.choicelayout = ("Europe0", "Europe00", "Europe000", "Europe0000", "US0", "US00", "US000", "US0000", "Macau", "Other")

        self.varPF0cwleft = StringVar(value='Not Selected')
        self.varPF0cwright = StringVar(value='Not Selected')
        self.varPF0ccwleft = StringVar(value='Not Selected')
        self.varPF0ccwright = StringVar(value='Not Selected')
        # 5
        self.varPF5cwleft = StringVar(value='Not Selected')
        self.varPF5cwright = StringVar(value='Not Selected')
        self.varPF5ccwleft = StringVar(value='Not Selected')
        self.varPF5ccwright = StringVar(value='Not Selected')
        # 9
        self.varPF9cwleft = StringVar(value='Not Selected')
        self.varPF9cwright = StringVar(value='Not Selected')
        self.varPF9ccwleft = StringVar(value='Not Selected')
        self.varPF9ccwright = StringVar(value='Not Selected')
        # 34
        self.varPF34cwleft = StringVar(value='Not Selected')
        self.varPF34cwright = StringVar(value='Not Selected')
        self.varPF34ccwleft = StringVar(value='Not Selected')
        self.varPF34ccwright = StringVar(value='Not Selected')
        # 22mm SLow Spin Variables
        self.varPFslowcwleft = StringVar(value='Not Selected')
        self.varPFslowcwright = StringVar(value='Not Selected')
        self.varPFslowccwleft = StringVar(value='Not Selected')
        self.varPFslowccwright = StringVar(value='Not Selected')

        ### SECTION 3 ###
        self.phasered = IntVar()
        self.phaseblack = IntVar()
        self.s1cw = IntVar()
        self.s2cw = IntVar()
        self.s3cw = IntVar()
        self.s1ccw = IntVar()
        self.s2ccw = IntVar()
        self.s3ccw = IntVar()
        self.varYNearth = StringVar(value='Not Selected')
        self.varYNledtest = StringVar(value='Not Selected')
        self.varYNledcheck = StringVar(value='Not Selected')

        ### SECTION 4 ###
        self.ordernumber = IntVar()
        self.wheeltype = StringVar(value="Not Selected")
        self.separatortype = StringVar(value="Not Selected")
        self.layouttype = StringVar(value="Not Selected")
        self.serialwheel = IntVar()
        self.seriallogger = IntVar()
        self.serialasrim = IntVar()
        self.serials1 = IntVar()
        self.serials2 = IntVar()
        self.serials3 = IntVar()
        self.serialinclinometer = IntVar()
        self.incltested = StringVar(value="Not Selected")
        self.gfltested = StringVar(value="Not Selected")
        self.comtested = StringVar(value="Not Selected")
        self.softwareversion = StringVar()
        self.nametester = StringVar()
        self.wnd1cwavtual = IntVar()
        self.wnd1cwdisplayed = IntVar()
        self.wnd2cwavtual = IntVar()
        self.wnd2cwdisplayed = IntVar()
        self.wnd1ccwavtual = IntVar()
        self.wnd1ccwdisplayed = IntVar()
        self.wnd2ccwavtual = IntVar()
        self.wnd2ccwdisplayed = IntVar()
        self.retest = BooleanVar()
        self.timenow = time.strftime('%Y-%m-%d %H:%M:%S')

        ### SECTION 2 ###
        # THese are for the 30 tests
        #Clockwise Actual Column
        self.cwactvariables = []
        for i in range(15):
            self.cwactvariables.append(IntVar())

        self.cwactlabels = []
        self.cwactentrys = []
        for ii in range(15):
            self.char = ii + 1
            self.offset = self.char + 10
            self.cwactlabels.append(Label(self.newtestwindow, text = self.char))
            self.cwactlabels[-1].grid(row=self.offset, column=0)
            self.cwactentrys.append(Entry(self.newtestwindow, textvariable = self.cwactvariables[ii]))
            self.cwactentrys[-1].grid(row=self.offset, column=1)


        # Counter-Clockwise Actual Column
        self.ccwactvariables = []
        for i in range(15):
            self.ccwactvariables.append(IntVar())

        self.ccwactlabels = []
        self.ccwactentrys = []
        for ii in range(15):
            self.char = ii + 1
            self.offset = self.char + 26
            self.ccwactlabels.append(Label(self.newtestwindow, text=self.char))
            self.ccwactlabels[-1].grid(row=self.offset, column=0)
            self.ccwactentrys.append(Entry(self.newtestwindow, textvariable=self.ccwactvariables[ii]))
            self.ccwactentrys[-1].grid(row=self.offset, column=1)

        #Clockwise Recorded Column
        self.cwrecvariables = []
        for i in range(15):
            self.cwrecvariables.append(IntVar())

        self.cwrecentrys = []
        for ii in range(15):
            self.char = ii + 1
            self.offset = self.char + 10
            self.cwrecentrys.append(Entry(self.newtestwindow, textvariable = self.cwrecvariables[ii]))
            self.cwrecentrys[-1].grid(row=self.offset, column=2)

        # Counter-Clockwise Actual Column
        self.ccwrecvariables = []
        for i in range(15):
            self.ccwrecvariables.append(IntVar())

        self.ccwrecentrys = []
        for ii in range(15):
            self.char = ii + 1
            self.offset = self.char + 26
            self.ccwrecentrys.append(Entry(self.newtestwindow, textvariable=self.ccwrecvariables[ii]))
            self.ccwrecentrys[-1].grid(row=self.offset, column=2)

            #return self.cwactvariables, self.cwrecvariables, self.ccwactvariables, self.ccwrecvariables
        

        #These are the tkinter widgets on the page. Might split in to several pages yet
        self.lblNumber = Label(self.newtestwindow, text="Number", relief="groove", width=15).grid(column=0, row=1)
        self.lblNumber0 = Label(self.newtestwindow, text="0", relief="groove", width=15).grid(column=0, row=2)
        self.lblNumber5 = Label(self.newtestwindow, text="5", relief="groove", width=15).grid(column=0, row=3)
        self.lblNumber9 = Label(self.newtestwindow, text="9", relief="groove", width=15).grid(column=0, row=4)
        self.lblNumber34 = Label(self.newtestwindow, text="34", relief="groove", width=15).grid(column=0, row=5)
        self.lbSlowZero = Label(self.newtestwindow, text="22mm Slow Zero", relief="groove", width=15).grid(column=0, row=7)
        self.lblcwleft = Label(self.newtestwindow, text="C/W Left", relief="groove", width=15).grid(column=1, row=1, columnspan=1)
        self.lblcwright = Label(self.newtestwindow, text="C/W Right", relief="groove", width=15).grid(column=2, row=1, columnspan=1)
        self.lblccwleft = Label(self.newtestwindow, text="CC/W Left", relief="groove", width=15).grid(column=3, row=1, columnspan=1)
        self.lblccwright = Label(self.newtestwindow, text="CC/W Right", relief="groove", width=15).grid(column=4, row=1, columnspan=1)
        self.lbl22mmzero = Label(self.newtestwindow, text="22mm Ball In Zero Test SLow Spin - 15RPM", relief="groove").grid(column=0, row=6, columnspan=3)
        #dropdowns for section 1
        #0
        self.optPF0cwleft = OptionMenu(self.newtestwindow, self.varPF0cwleft, *self.choicePF).grid(column = 1, row = 2)
        self.optPF0cwright = OptionMenu(self.newtestwindow, self.varPF0cwright, *self.choicePF).grid(column = 2, row = 2)
        self.optPF0ccwleft = OptionMenu(self.newtestwindow, self.varPF0ccwleft, *self.choicePF).grid(column = 3, row = 2)
        self.optPF0ccwright = OptionMenu(self.newtestwindow, self.varPF0ccwright, *self.choicePF).grid(column = 4, row = 2)
        #5
        self.optPF5cwleft = OptionMenu(self.newtestwindow, self.varPF5cwleft, *self.choicePF).grid(column = 1, row = 3)
        self.optPF5cwright = OptionMenu(self.newtestwindow, self.varPF5cwright, *self.choicePF).grid(column = 2, row = 3)
        self.optPF5ccwleft = OptionMenu(self.newtestwindow, self.varPF5ccwleft, *self.choicePF).grid(column = 3, row = 3)
        self.optPF5ccwright = OptionMenu(self.newtestwindow, self.varPF5ccwright, *self.choicePF).grid(column = 4, row = 3)
        #9
        self.optPF9cwleft = OptionMenu(self.newtestwindow, self.varPF9cwleft, *self.choicePF).grid(column = 1, row = 4)
        self.optPF9cwright = OptionMenu(self.newtestwindow, self.varPF9cwright, *self.choicePF).grid(column = 2, row = 4)
        self.optPF9ccwleft = OptionMenu(self.newtestwindow, self.varPF9ccwleft, *self.choicePF).grid(column = 3, row = 4)
        self.optPF9ccwright = OptionMenu(self.newtestwindow, self.varPF9ccwright, *self.choicePF).grid(column = 4, row = 4)
        #34
        self.optPF34cwleft = OptionMenu(self.newtestwindow, self.varPF34cwleft, *self.choicePF).grid(column = 1, row = 5)
        self.optPF34cwright = OptionMenu(self.newtestwindow, self.varPF34cwright, *self.choicePF).grid(column = 2, row = 5)
        self.optPF34ccwleft = OptionMenu(self.newtestwindow, self.varPF34ccwleft, *self.choicePF).grid(column = 3, row = 5)
        self.optPF34ccwright = OptionMenu(self.newtestwindow, self.varPF34ccwright, *self.choicePF).grid(column = 4, row = 5)
        #22mm Slow Spin Zero
        self.optPFslowcwleft = OptionMenu(self.newtestwindow, self.varPFslowcwleft, *self.choicePF).grid(column = 1, row = 7)
        self.optPFslowcwright = OptionMenu(self.newtestwindow, self.varPFslowcwright, *self.choicePF).grid(column = 2, row = 7)
        self.optPFslowccwleft = OptionMenu(self.newtestwindow, self.varPFslowccwleft, *self.choicePF).grid(column = 3, row = 7)
        self.optPFslowccwright = OptionMenu(self.newtestwindow, self.varPFslowccwright, *self.choicePF).grid(column = 4, row = 7)


        #Clockwise
        lblgap2 = Label(self.newtestwindow, text="", width=15).grid(column=0, row=9)
        Label(self.newtestwindow, text="C/W Number", relief="groove", width=15).grid(column=0, row=10, columnspan=1)
        Label(self.newtestwindow, text="Actual Number", relief="groove", width=15).grid(column=1, row=10, columnspan=1)
        Label(self.newtestwindow, text="Recorded Number", relief="groove", width=15).grid(column=2, row=10, columnspan=1)
        Label(self.newtestwindow, text="CC/W Number", relief="groove", width=15).grid(column=0, row=26, columnspan=1)
        Label(self.newtestwindow, text="Actual Number", relief="groove", width=15).grid(column=1, row=26, columnspan=1)
        Label(self.newtestwindow, text="Recorded Number", relief="groove", width=15).grid(column=2, row=26, columnspan=1)



        self.lblgap1 = Label(self.newtestwindow, text="", width=15).grid(column=6, row=1)
        self.lblsetwheel = Label(self.newtestwindow, text="Wheel Settings", relief="groove", width=15).grid(column=7, row=1)
        self.lblsetred = Label(self.newtestwindow, text="Red", relief="groove", width=15).grid(column=8, row=1)
        self.lblsetblack = Label(self.newtestwindow, text="Black", relief="groove", width=15).grid(column=9, row=1)
        self.lblsetphase = Label(self.newtestwindow, text="Ball Phase Settings", relief="groove", width=15).grid(column=7, row=2)
        self.lblsetcw = Label(self.newtestwindow, text="C/W", relief="groove", width=15).grid(column=8, row=3)
        self.lblsetccw = Label(self.newtestwindow, text="CC/W", relief="groove", width=15).grid(column=9, row=3)
        self.lblsensor1 = Label(self.newtestwindow, text="Sensor 1", relief="groove", width=15).grid(column=7, row=4)
        self.lblsensor2 = Label(self.newtestwindow, text="Sensor 2", relief="groove", width=15).grid(column=7, row=5)
        self.lblsensor3 = Label(self.newtestwindow, text="Sensor 3", relief="groove", width=15).grid(column=7, row=6)
        self.lblearth = Label(self.newtestwindow, text="Earth Wire Connected?", relief="groove",  width=25).grid(column=7, row=8, columnspan=2)
        self.lblledtest = Label(self.newtestwindow, text="LED's Tested? (glo wheel)", relief="groove", width=25).grid(column=7, row=10, columnspan=2)
        self.lblledcheck = Label(self.newtestwindow, text="LED Check (see below)", relief="groove", width=25).grid(column=7, row=11, columnspan=2)
        self.lblsensorledcheck = Label(self.newtestwindow, text="Check LED 1,2&3 for random flash for 2 mins", relief="groove", fg="Red", width=35).grid(column=7, row=12, columnspan=3)

        self.entrys1cw = Entry(self.newtestwindow, textvariable=self.s1cw).grid(column=8, row=4)
        self.entrys2cw = Entry(self.newtestwindow, textvariable=self.s2cw).grid(column=8, row=5)
        self.entrys3cw = Entry(self.newtestwindow, textvariable=self.s3cw).grid(column=8, row=6)
        self.entrys1ccw = Entry(self.newtestwindow, textvariable=self.s1ccw).grid(column=9, row=4)
        self.entrys2ccw = Entry(self.newtestwindow, textvariable=self.s2ccw).grid(column=9, row=5)
        self.entrys3ccw = Entry(self.newtestwindow, textvariable=self.s3ccw).grid(column=9, row=6)
        self.entryphasered = Entry(self.newtestwindow, textvariable=self.phasered).grid(column=8, row=2)
        self.entryphaseblack = Entry(self.newtestwindow, textvariable=self.phaseblack).grid(column=9, row=2)
        self.optearth = OptionMenu(self.newtestwindow, self.varYNearth, *self.choiceYN).grid(column=9, row=8)
        self.optLEDtest = OptionMenu(self.newtestwindow, self.varYNledtest, *self.choiceYN).grid(column=9, row=10)
        self.optLEDcheck = OptionMenu(self.newtestwindow, self.varYNledcheck, *self.choiceYN).grid(column=9, row=11)



        self.lblordernumber = Label(self.newtestwindow, text="Customer Order No:", relief="groove", width=25).grid(column=4, row=14, columnspan=2)
        self.lblseparatortype = Label(self.newtestwindow, text="Wheel Separator Type:", relief="groove", width=25).grid(column=4, row=15, columnspan=2)
        self.lbllayouttype = Label(self.newtestwindow, text="Wheel Layout Type:", relief="groove", width=25).grid(column=4, row=16, columnspan=2)
        self.lblwheelserial = Label(self.newtestwindow, text="Wheel Serial Number:", relief="groove", width=25).grid(column=4, row=17, columnspan=2)
        self.lblloggerserial = Label(self.newtestwindow, text="Data Logger Serial Number:", relief="groove", width=25).grid(column=4, row=18, columnspan=2)
        self.lblasrimserial = Label(self.newtestwindow, text="ASRIM Board Serial Number:", relief="groove", width=25).grid(column=4, row=19, columnspan=2)
        self.lbls1serial = Label(self.newtestwindow, text="Sensor 1 Serial Number:", relief="groove", width=25).grid(column=4, row=20, columnspan=2)
        self.lbls2serial = Label(self.newtestwindow, text="Sensor 2 Serial Number:", relief="groove", width=25).grid(column=4, row=21, columnspan=2)
        self.lbls3serial = Label(self.newtestwindow, text="Sensor 3 Serial Number:", relief="groove", width=25).grid(column=4, row=22, columnspan=2)
        self.lblincserial = Label(self.newtestwindow, text="Inclinometer Serial Number:", relief="groove", width=25).grid(column=7, row=14, columnspan=2)
        self.lblinctest = Label(self.newtestwindow, text="Inclinemeter Tested?", relief="groove", width=25).grid(column=7, row=15, columnspan=2)
        self.lblgfltest = Label(self.newtestwindow, text="GFL Tested?", relief="groove", width=25).grid(column=7, row=16, columnspan=2)
        self.lblcomtest = Label(self.newtestwindow, text="Com Port Test?", relief="groove", width=25).grid(column=7, row=17, columnspan=2)
        self.lblswversion = Label(self.newtestwindow, text="Software Version", relief="groove", width=25).grid(column=7, row=18, columnspan=2)
        self.lblsigndate = Label(self.newtestwindow, text="Date", relief="groove", width=25).grid(column=7, row=19, columnspan=2)
        self.lblsignname = Label(self.newtestwindow, text="Name Of Tester:", relief="groove", width=25).grid(column=7, row=20, columnspan=2)
        self.lblgap1 = Label(self.newtestwindow, text="", width=15).grid(column=7, row=27)

        self.lblendtest = Label(self.newtestwindow, text="WND v2 Protocol Test", relief="groove", width=35).grid(column=7, row=28, columnspan=3)
        self.lblwndnum = Label(self.newtestwindow, text="Number", width=15, relief="groove").grid(column=7, row=29)
        self.lblwndactual = Label(self.newtestwindow, text="Actual Numbr", width=15, relief="groove").grid(column=8, row=29)
        self.lblwnddisplayed = Label(self.newtestwindow, text="Number Displayed", width=15, relief="groove").grid(column=9, row=29)
        self.lblwndcw1 = Label(self.newtestwindow, text="1 C/W", width=15, relief="groove").grid(column=7, row=30)
        self.lblwndcw2 = Label(self.newtestwindow, text="2 C/W", width=15, relief="groove").grid(column=7, row=31)
        self.lblwndccw1 = Label(self.newtestwindow, text="1 CC/W", width=15, relief="groove").grid(column=7, row=32)
        self.lblwndccw2 = Label(self.newtestwindow, text="2 CC/W", width=15, relief="groove").grid(column=7, row=33)

        self.checkretest = Checkbutton(self.newtestwindow, text="Retest?", variable=self.retest).grid(column=6, row=12)
        self.optwheeltype = OptionMenu(self.newtestwindow, self.wheeltype, *self.choicewheel).grid(column=6, row=13)
        self.entryordernumber = Entry(self.newtestwindow, textvariable=self.ordernumber).grid(column=6, row=14)
        self.optseptype = OptionMenu(self.newtestwindow, self.separatortype, *self.choiceseparator).grid(column=6, row=15)
        self.optwheellayout = OptionMenu(self.newtestwindow, self.layouttype, *self.choicelayout).grid(column=6, row=16)
        self.entryserialwheel = Entry(self.newtestwindow, textvariable=self.serialwheel).grid(column=6, row=17)
        self.entryseriallogger = Entry(self.newtestwindow, textvariable=self.seriallogger).grid(column=6, row=18)
        self.entryserialasrim = Entry(self.newtestwindow, textvariable=self.serialasrim).grid(column=6, row=19)
        self.entryserials1 = Entry(self.newtestwindow, textvariable=self.serials1).grid(column=6, row=20)
        self.entryserials2 = Entry(self.newtestwindow, textvariable=self.serials2).grid(column=6, row=21)
        self.entryserials3 = Entry(self.newtestwindow, textvariable=self.serials3).grid(column=6, row=22)
        self.entryserialinc = Entry(self.newtestwindow, textvariable=self.serialinclinometer).grid(column=9, row=14)
        self.optinctest = OptionMenu(self.newtestwindow, self.incltested, *self.choiceYN).grid(column=9, row=15)
        self.optgfltest = OptionMenu(self.newtestwindow, self.gfltested, *self.choiceYN).grid(column=9, row=16)
        self.optcomtest = OptionMenu(self.newtestwindow, self.comtested, *self.choiceYN).grid(column=9, row=17)
        self.entryswversion = Entry(self.newtestwindow, textvariable=self.softwareversion).grid(column=9, row=18)
        self.lbldate = Label(self.newtestwindow, text=self.timenow).grid(column=9, row=19)
        self.entrytestername = Entry(self.newtestwindow, textvariable=self.nametester).grid(column=9, row=20)

        self.entrywndcw1act = Entry(self.newtestwindow, textvariable=self.wnd1cwavtual).grid(column=8, row=30)
        self.entrywndcw2act = Entry(self.newtestwindow, textvariable=self.wnd2cwavtual).grid(column=8, row=31)
        self.entrywndccw1act = Entry(self.newtestwindow, textvariable=self.wnd1ccwavtual).grid(column=8, row=32)
        self.entrywndccw2act = Entry(self.newtestwindow, textvariable=self.wnd2ccwavtual).grid(column=8, row=33)
        self.entrywndcw1disp = Entry(self.newtestwindow, textvariable=self.wnd1cwdisplayed).grid(column=9, row=30)
        self.entrywndcw2disp = Entry(self.newtestwindow, textvariable=self.wnd2cwdisplayed).grid(column=9, row=31)
        self.entrywndccw1disp = Entry(self.newtestwindow, textvariable=self.wnd1ccwdisplayed).grid(column=9, row=32)
        self.entrywndccw2disp = Entry(self.newtestwindow, textvariable=self.wnd2ccwdisplayed).grid(column=9, row=33)

        Button(self.newtestwindow, text="Print Entries", command=lambda:print(self.cw1.get(), self.cw2.get())).grid(column=5, row=32)
        Button(self.newtestwindow, text="CLOSE", command=self.newtestwindow.destroy).grid(column=5, row=30)
        Button(self.newtestwindow,text="SAVE",command=lambda: self.printvar()).grid(column=5, row=33)

    def printvar(self):
        newvar = self.cwactvariables
        #print(newvar[2].get())
        print(self.cwactvariables[0].get())
        # for i in newvar:
        #     print(i.get())

    def savedata(self):
        print("Saving Data")




