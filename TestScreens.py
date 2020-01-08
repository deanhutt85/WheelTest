from tkinter import *
import time
from DatabaseHandler import *

#from WheelTestGUI import database_stuff

#VARIABLES
actualentries = []
expectedentries = []


class CreateTest:

    def new_test(self):
        newtestwindow = Toplevel()
        varPF = StringVar()
        choicePF = ("Pass", "Fail")
        choiceYN = ("Yes", "No", "N/A")
        choicewheel = ("Saturn", "Saturn GLO", "Saturn-Auto", "Other")
        choiceseparator = ("Standard", "Starburst", "Saturn-Auto", "Other")
        choicelayout = ("Europe0", "Europe00", "Europe000", "Europe0000", "US0", "US00", "US000", "US0000", "Macau", "Other")

        varPF0cwleft = StringVar(value='Not Selected')
        varPF0cwright = StringVar(value='Not Selected')
        varPF0ccwleft = StringVar(value='Not Selected')
        varPF0ccwright = StringVar(value='Not Selected')
        # 5
        varPF5cwleft = StringVar(value='Not Selected')
        varPF5cwright = StringVar(value='Not Selected')
        varPF5ccwleft = StringVar(value='Not Selected')
        varPF5ccwright = StringVar(value='Not Selected')
        # 9
        varPF9cwleft = StringVar(value='Not Selected')
        varPF9cwright = StringVar(value='Not Selected')
        varPF9ccwleft = StringVar(value='Not Selected')
        varPF9ccwright = StringVar(value='Not Selected')
        # 34
        varPF34cwleft = StringVar(value='Not Selected')
        varPF34cwright = StringVar(value='Not Selected')
        varPF34ccwleft = StringVar(value='Not Selected')
        varPF34ccwright = StringVar(value='Not Selected')
        # 22mm SLow Spin Variables
        varPFslowcwleft = StringVar(value='Not Selected')
        varPFslowcwright = StringVar(value='Not Selected')
        varPFslowccwleft = StringVar(value='Not Selected')
        varPFslowccwright = StringVar(value='Not Selected')

        ### SECTION 2 ###
        # THese are for the 30 tests
        cw1 = IntVar(value=None)
        cw2 = IntVar()
        cw3 = IntVar()
        cw4 = IntVar()
        cw5 = IntVar()
        cw6 = IntVar()
        cw7 = IntVar()
        cw8 = IntVar()
        cw9 = IntVar()
        cw10 = IntVar()
        cw11 = IntVar()
        cw12 = IntVar()
        cw13 = IntVar()
        cw14 = IntVar()
        cw15 = IntVar()
        ccw1 = IntVar()
        ccw2 = IntVar()
        ccw3 = IntVar()
        ccw4 = IntVar()
        ccw5 = IntVar()
        ccw6 = IntVar()
        ccw7 = IntVar()
        ccw8 = IntVar()
        ccw9 = IntVar()
        ccw10 = IntVar()
        ccw11 = IntVar()
        ccw12 = IntVar()
        ccw13 = IntVar()
        ccw14 = IntVar()
        ccw15 = IntVar()
        reccw1 = IntVar(value=None)
        reccw2 = IntVar()
        reccw3 = IntVar()
        reccw4 = IntVar()
        reccw5 = IntVar()
        reccw6 = IntVar()
        reccw7 = IntVar()
        reccw8 = IntVar()
        reccw9 = IntVar()
        reccw10 = IntVar()
        reccw11 = IntVar()
        reccw12 = IntVar()
        reccw13 = IntVar()
        reccw14 = IntVar()
        reccw15 = IntVar()
        recccw1 = IntVar()
        recccw2 = IntVar()
        recccw3 = IntVar()
        recccw4 = IntVar()
        recccw5 = IntVar()
        recccw6 = IntVar()
        recccw7 = IntVar()
        recccw8 = IntVar()
        recccw9 = IntVar()
        recccw10 = IntVar()
        recccw11 = IntVar()
        recccw12 = IntVar()
        recccw13 = IntVar()
        recccw14 = IntVar()
        recccw15 = IntVar()

        ### SECTION 3 ###
        phasered = IntVar()
        phaseblack = IntVar()
        s1cw = IntVar()
        s2cw = IntVar()
        s3cw = IntVar()
        s1ccw = IntVar()
        s2ccw = IntVar()
        s3ccw = IntVar()
        varYNearth = StringVar(value='Not Selected')
        varYNledtest = StringVar(value='Not Selected')
        varYNledcheck = StringVar(value='Not Selected')

        ### SECTION 4 ###
        ordernumber = IntVar()
        wheeltype = StringVar(value="Not Selected")
        separatortype = StringVar(value="Not Selected")
        layouttype = StringVar(value="Not Selected")
        serialwheel = IntVar()
        seriallogger = IntVar()
        serialasrim = IntVar()
        serials1 = IntVar()
        serials2 = IntVar()
        serials3 = IntVar()
        serialinclinometer = IntVar()
        incltested = StringVar(value="Not Selected")
        gfltested = StringVar(value="Not Selected")
        comtested = StringVar(value="Not Selected")
        softwareversion = StringVar()
        nametester = StringVar()
        wnd1cwavtual = IntVar()
        wnd1cwdisplayed = IntVar()
        wnd2cwavtual = IntVar()
        wnd2cwdisplayed = IntVar()
        wnd1ccwavtual = IntVar()
        wnd1ccwdisplayed = IntVar()
        wnd2ccwavtual = IntVar()
        wnd2ccwdisplayed = IntVar()
        retest = BooleanVar()
        timenow = time.strftime('%Y-%m-%d %H:%M:%S')
        #These are the variables for the dropdowns
        #0


        ### SECTION 1 ###

        #These are the tkinter widgets on the page. Might split in to several pages yet
        lblNumber = Label(newtestwindow, text="Number", relief="groove", width=15).grid(column=0, row=1)
        lblNumber0 = Label(newtestwindow, text="0", relief="groove", width=15).grid(column=0, row=2)
        lblNumber5 = Label(newtestwindow, text="5", relief="groove", width=15).grid(column=0, row=3)
        lblNumber9 = Label(newtestwindow, text="9", relief="groove", width=15).grid(column=0, row=4)
        lblNumber34 = Label(newtestwindow, text="34", relief="groove", width=15).grid(column=0, row=5)
        lbSlowZero = Label(newtestwindow, text="22mm Slow Zero", relief="groove", width=15).grid(column=0, row=7)
        lblcwleft = Label(newtestwindow, text="C/W Left", relief="groove", width=15).grid(column=1, row=1, columnspan=1)
        lblcwright = Label(newtestwindow, text="C/W Right", relief="groove", width=15).grid(column=2, row=1, columnspan=1)
        lblccwleft = Label(newtestwindow, text="CC/W Left", relief="groove", width=15).grid(column=3, row=1, columnspan=1)
        lblccwright = Label(newtestwindow, text="CC/W Right", relief="groove", width=15).grid(column=4, row=1, columnspan=1)
        lbl22mmzero = Label(newtestwindow, text="22mm Ball In Zero Test SLow Spin - 15RPM", relief="groove").grid(column=0, row=6, columnspan=3)
        #dropdowns for section 1
        #0
        OptionMenu(newtestwindow, varPF0cwleft, *choicePF).grid(column = 1, row = 2)
        OptionMenu(newtestwindow, varPF0cwright, *choicePF).grid(column = 2, row = 2)
        OptionMenu(newtestwindow, varPF0ccwleft, *choicePF).grid(column = 3, row = 2)
        OptionMenu(newtestwindow, varPF0ccwright, *choicePF).grid(column = 4, row = 2)
        #5
        OptionMenu(newtestwindow, varPF5cwleft, *choicePF).grid(column = 1, row = 3)
        OptionMenu(newtestwindow, varPF5cwright, *choicePF).grid(column = 2, row = 3)
        OptionMenu(newtestwindow, varPF5ccwleft, *choicePF).grid(column = 3, row = 3)
        OptionMenu(newtestwindow, varPF5ccwright, *choicePF).grid(column = 4, row = 3)
        #9
        OptionMenu(newtestwindow, varPF9cwleft, *choicePF).grid(column = 1, row = 4)
        OptionMenu(newtestwindow, varPF9cwright, *choicePF).grid(column = 2, row = 4)
        OptionMenu(newtestwindow, varPF9ccwleft, *choicePF).grid(column = 3, row = 4)
        OptionMenu(newtestwindow, varPF9ccwright, *choicePF).grid(column = 4, row = 4)
        #34
        OptionMenu(newtestwindow, varPF34cwleft, *choicePF).grid(column = 1, row = 5)
        OptionMenu(newtestwindow, varPF34cwright, *choicePF).grid(column = 2, row = 5)
        OptionMenu(newtestwindow, varPF34ccwleft, *choicePF).grid(column = 3, row = 5)
        OptionMenu(newtestwindow, varPF34ccwright, *choicePF).grid(column = 4, row = 5)
        #22mm Slow Spin Zero
        OptionMenu(newtestwindow, varPFslowcwleft, *choicePF).grid(column = 1, row = 7)
        OptionMenu(newtestwindow, varPFslowcwright, *choicePF).grid(column = 2, row = 7)
        OptionMenu(newtestwindow, varPFslowccwleft, *choicePF).grid(column = 3, row = 7)
        OptionMenu(newtestwindow, varPFslowccwright, *choicePF).grid(column = 4, row = 7)


        #Clockwise
        #lblgap2 = Label(newtestwindow, text="", width=15).grid(column=0, row=9)
        Label(newtestwindow, text="Number", relief="groove", width=15).grid(column=0, row=10, columnspan=1)
        Label(newtestwindow, text="Actual Number", relief="groove", width=15).grid(column=1, row=10, columnspan=1)
        Label(newtestwindow, text="Recorded Number", relief="groove", width=15).grid(column=2, row=10, columnspan=1)
        Label(newtestwindow, text="1 C/W", relief="groove", width=15).grid(column=0, row=11, columnspan=1)
        Label(newtestwindow, text="2 C/W", relief="groove", width=15).grid(column=0, row=12, columnspan=1)
        Label(newtestwindow, text="3 C/W", relief="groove", width=15).grid(column=0, row=13, columnspan=1)
        Label(newtestwindow, text="4 C/W", relief="groove", width=15).grid(column=0, row=14, columnspan=1)
        Label(newtestwindow, text="5 C/W", relief="groove", width=15).grid(column=0, row=15, columnspan=1)
        Label(newtestwindow, text="6 C/W", relief="groove", width=15).grid(column=0, row=16, columnspan=1)
        Label(newtestwindow, text="7 C/W", relief="groove", width=15).grid(column=0, row=17, columnspan=1)
        Label(newtestwindow, text="8 C/W", relief="groove", width=15).grid(column=0, row=18, columnspan=1)
        Label(newtestwindow, text="9 C/W", relief="groove", width=15).grid(column=0, row=19, columnspan=1)
        Label(newtestwindow, text="10 C/W", relief="groove", width=15).grid(column=0, row=20, columnspan=1)
        Label(newtestwindow, text="11 C/W", relief="groove", width=15).grid(column=0, row=21, columnspan=1)
        Label(newtestwindow, text="12 C/W", relief="groove", width=15).grid(column=0, row=22, columnspan=1)
        Label(newtestwindow, text="13 C/W", relief="groove", width=15).grid(column=0, row=23, columnspan=1)
        Label(newtestwindow, text="14 C/W", relief="groove", width=15).grid(column=0, row=24, columnspan=1)
        Label(newtestwindow, text="15 C/W", relief="groove", width=15).grid(column=0, row=25, columnspan=1)
        #Counter-clockwise
        Label(newtestwindow, text="Number", relief="groove", width=15).grid(column=0, row=26, columnspan=1)
        Label(newtestwindow, text="Actual Number", relief="groove", width=15).grid(column=1, row=26, columnspan=1)
        Label(newtestwindow, text="Recorded Number", relief="groove", width=15).grid(column=2, row=26, columnspan=1)
        Label(newtestwindow, text="1 CC/W", relief="groove", width=15).grid(column=0, row=27, columnspan=1)
        Label(newtestwindow, text="2 CC/W", relief="groove", width=15).grid(column=0, row=28, columnspan=1)
        Label(newtestwindow, text="3 CC/W", relief="groove", width=15).grid(column=0, row=29, columnspan=1)
        Label(newtestwindow, text="4 CC/W", relief="groove", width=15).grid(column=0, row=30, columnspan=1)
        Label(newtestwindow, text="5 CC/W", relief="groove", width=15).grid(column=0, row=31, columnspan=1)
        Label(newtestwindow, text="6 CC/W", relief="groove", width=15).grid(column=0, row=32, columnspan=1)
        Label(newtestwindow, text="7 CC/W", relief="groove", width=15).grid(column=0, row=33, columnspan=1)
        Label(newtestwindow, text="8 CC/W", relief="groove", width=15).grid(column=0, row=34, columnspan=1)
        Label(newtestwindow, text="9 CC/W", relief="groove", width=15).grid(column=0, row=35, columnspan=1)
        Label(newtestwindow, text="10 CC/W", relief="groove", width=15).grid(column=0, row=36, columnspan=1)
        Label(newtestwindow, text="11 CC/W", relief="groove", width=15).grid(column=0, row=37, columnspan=1)
        Label(newtestwindow, text="12 CC/W", relief="groove", width=15).grid(column=0, row=38, columnspan=1)
        Label(newtestwindow, text="13 CC/W", relief="groove", width=15).grid(column=0, row=39, columnspan=1)
        Label(newtestwindow, text="14 CC/W", relief="groove", width=15).grid(column=0, row=40, columnspan=1)
        Label(newtestwindow, text="15 CC/W", relief="groove", width=15).grid(column=0, row=41, columnspan=1)

        entrycw1 = Entry(newtestwindow, textvariable=cw1).grid(column=1, row=11)
        entrycw2 = Entry(newtestwindow, textvariable=cw2).grid(column=1, row=12)
        entrycw3 = Entry(newtestwindow, textvariable=cw3).grid(column=1, row=13)
        entrycw4 = Entry(newtestwindow, textvariable=cw4).grid(column=1, row=14)
        entrycw5 = Entry(newtestwindow, textvariable=cw5).grid(column=1, row=15)
        entrycw6 = Entry(newtestwindow, textvariable=cw6).grid(column=1, row=16)
        entrycw7 = Entry(newtestwindow, textvariable=cw7).grid(column=1, row=17)
        entrycw8 = Entry(newtestwindow, textvariable=cw8).grid(column=1, row=18)
        entrycw9 = Entry(newtestwindow, textvariable=cw9).grid(column=1, row=19)
        entrycw10 = Entry(newtestwindow, textvariable=cw10).grid(column=1, row=20)
        entrycw11 = Entry(newtestwindow, textvariable=cw11).grid(column=1, row=21)
        entrycw12 = Entry(newtestwindow, textvariable=cw12).grid(column=1, row=22)
        entrycw13 = Entry(newtestwindow, textvariable=cw13).grid(column=1, row=23)
        entrycw14 = Entry(newtestwindow, textvariable=cw14).grid(column=1, row=24)
        entrycw15 = Entry(newtestwindow, textvariable=cw15).grid(column=1, row=25)
        entryccw1 = Entry(newtestwindow, textvariable=ccw1).grid(column=1, row=27)
        entryccw2 = Entry(newtestwindow, textvariable=ccw2).grid(column=1, row=28)
        entryccw3 = Entry(newtestwindow, textvariable=ccw3).grid(column=1, row=29)
        entryccw4 = Entry(newtestwindow, textvariable=ccw4).grid(column=1, row=30)
        entryccw5 = Entry(newtestwindow, textvariable=ccw5).grid(column=1, row=31)
        entryccw6 = Entry(newtestwindow, textvariable=ccw6).grid(column=1, row=32)
        entryccw7 = Entry(newtestwindow, textvariable=ccw7).grid(column=1, row=33)
        entryccw8 = Entry(newtestwindow, textvariable=ccw8).grid(column=1, row=34)
        entryccw9 = Entry(newtestwindow, textvariable=ccw9).grid(column=1, row=35)
        entryccw10 = Entry(newtestwindow, textvariable=ccw10).grid(column=1, row=36)
        entryccw11 = Entry(newtestwindow, textvariable=ccw11).grid(column=1, row=37)
        entryccw12 = Entry(newtestwindow, textvariable=ccw12).grid(column=1, row=38)
        entryccw13 = Entry(newtestwindow, textvariable=ccw13).grid(column=1, row=39)
        entryccw14 = Entry(newtestwindow, textvariable=ccw14).grid(column=1, row=40)
        entryccw15 = Entry(newtestwindow, textvariable=ccw15).grid(column=1, row=41)

        entryreccw1 = Entry(newtestwindow, textvariable=reccw1).grid(column=2, row=11)
        entryreccw2 = Entry(newtestwindow, textvariable=reccw2).grid(column=2, row=12)
        entryreccw3 = Entry(newtestwindow, textvariable=reccw3).grid(column=2, row=13)
        entryreccw4 = Entry(newtestwindow, textvariable=reccw4).grid(column=2, row=14)
        entryreccw5 = Entry(newtestwindow, textvariable=reccw5).grid(column=2, row=15)
        entryreccw6 = Entry(newtestwindow, textvariable=reccw6).grid(column=2, row=16)
        entryreccw7 = Entry(newtestwindow, textvariable=reccw7).grid(column=2, row=17)
        entryreccw8 = Entry(newtestwindow, textvariable=reccw8).grid(column=2, row=18)
        entryreccw9 = Entry(newtestwindow, textvariable=reccw9).grid(column=2, row=19)
        entryreccw10 = Entry(newtestwindow, textvariable=reccw10).grid(column=2, row=20)
        entryreccw11 = Entry(newtestwindow, textvariable=reccw11).grid(column=2, row=21)
        entryreccw12 = Entry(newtestwindow, textvariable=reccw12).grid(column=2, row=22)
        entryreccw13 = Entry(newtestwindow, textvariable=reccw13).grid(column=2, row=23)
        entryreccw14 = Entry(newtestwindow, textvariable=reccw14).grid(column=2, row=24)
        entryreccw15 = Entry(newtestwindow, textvariable=reccw15).grid(column=2, row=25)
        entryrecccw1 = Entry(newtestwindow, textvariable=recccw1).grid(column=2, row=27)
        entryrecccw2 = Entry(newtestwindow, textvariable=recccw2).grid(column=2, row=28)
        entryrecccw3 = Entry(newtestwindow, textvariable=recccw3).grid(column=2, row=29)
        entryrecccw4 = Entry(newtestwindow, textvariable=recccw4).grid(column=2, row=30)
        entryrecccw5 = Entry(newtestwindow, textvariable=recccw5).grid(column=2, row=31)
        entryrecccw6 = Entry(newtestwindow, textvariable=recccw6).grid(column=2, row=32)
        entryrecccw7 = Entry(newtestwindow, textvariable=recccw7).grid(column=2, row=33)
        entryrecccw8 = Entry(newtestwindow, textvariable=recccw8).grid(column=2, row=34)
        entryrecccw9 = Entry(newtestwindow, textvariable=recccw9).grid(column=2, row=35)
        entryrecccw10 = Entry(newtestwindow, textvariable=recccw10).grid(column=2, row=36)
        entryrecccw11 = Entry(newtestwindow, textvariable=recccw11).grid(column=2, row=37)
        entryrecccw12 = Entry(newtestwindow, textvariable=recccw12).grid(column=2, row=38)
        entryrecccw13 = Entry(newtestwindow, textvariable=recccw13).grid(column=2, row=39)
        entryrecccw14 = Entry(newtestwindow, textvariable=recccw14).grid(column=2, row=40)
        entryrecccw15 = Entry(newtestwindow, textvariable=recccw15).grid(column=2, row=41)

        lblgap1 = Label(newtestwindow, text="", width=15).grid(column=6, row=1)
        lblsetwheel = Label(newtestwindow, text="Wheel Settings", relief="groove", width=15).grid(column=7, row=1)
        lblsetred = Label(newtestwindow, text="Red", relief="groove", width=15).grid(column=8, row=1)
        lblsetblack = Label(newtestwindow, text="Black", relief="groove", width=15).grid(column=9, row=1)
        lblsetphase = Label(newtestwindow, text="Ball Phase Settings", relief="groove", width=15).grid(column=7, row=2)
        lblsetcw = Label(newtestwindow, text="C/W", relief="groove", width=15).grid(column=8, row=3)
        lblsetccw = Label(newtestwindow, text="CC/W", relief="groove", width=15).grid(column=9, row=3)
        lblsensor1 = Label(newtestwindow, text="Sensor 1", relief="groove", width=15).grid(column=7, row=4)
        lblsensor2 = Label(newtestwindow, text="Sensor 2", relief="groove", width=15).grid(column=7, row=5)
        lblsensor3 = Label(newtestwindow, text="Sensor 3", relief="groove", width=15).grid(column=7, row=6)
        lblearth = Label(newtestwindow, text="Earth Wire Connected?", relief="groove",  width=25).grid(column=7, row=8, columnspan=2)
        lblledtest = Label(newtestwindow, text="LED's Tested? (glo wheel)", relief="groove", width=25).grid(column=7, row=10, columnspan=2)
        lblledcheck = Label(newtestwindow, text="LED Check (see below)", relief="groove", width=25).grid(column=7, row=11, columnspan=2)
        lblsensorledcheck = Label(newtestwindow, text="Check LED 1,2&3 for random flash for 2 mins", relief="groove", fg="Red", width=35).grid(column=7, row=12, columnspan=3)

        entrys1cw = Entry(newtestwindow, textvariable=s1cw).grid(column=8, row=4)
        entrys2cw = Entry(newtestwindow, textvariable=s2cw).grid(column=8, row=5)
        entrys3cw = Entry(newtestwindow, textvariable=s3cw).grid(column=8, row=6)
        entrys1ccw = Entry(newtestwindow, textvariable=s1ccw).grid(column=9, row=4)
        entrys2ccw = Entry(newtestwindow, textvariable=s2ccw).grid(column=9, row=5)
        entrys3ccw = Entry(newtestwindow, textvariable=s3ccw).grid(column=9, row=6)
        entryphasered = Entry(newtestwindow, textvariable=phasered).grid(column=8, row=2)
        entryphaseblack = Entry(newtestwindow, textvariable=phaseblack).grid(column=9, row=2)
        optearth = OptionMenu(newtestwindow, varYNearth, *choiceYN).grid(column=9, row=8)
        optLEDtest = OptionMenu(newtestwindow, varYNledtest, *choiceYN).grid(column=9, row=10)
        optLEDcheck = OptionMenu(newtestwindow, varYNledcheck, *choiceYN).grid(column=9, row=11)



        lblordernumber = Label(newtestwindow, text="Customer Order No:", relief="groove", width=25).grid(column=4, row=14, columnspan=2)
        lblseparatortype = Label(newtestwindow, text="Wheel Separator Type:", relief="groove", width=25).grid(column=4, row=15, columnspan=2)
        lbllayouttype = Label(newtestwindow, text="Wheel Layout Type:", relief="groove", width=25).grid(column=4, row=16, columnspan=2)
        lblwheelserial = Label(newtestwindow, text="Wheel Serial Number:", relief="groove", width=25).grid(column=4, row=17, columnspan=2)
        lblloggerserial = Label(newtestwindow, text="Data Logger Serial Number:", relief="groove", width=25).grid(column=4, row=18, columnspan=2)
        lblasrimserial = Label(newtestwindow, text="ASRIM Board Serial Number:", relief="groove", width=25).grid(column=4, row=19, columnspan=2)
        lbls1serial = Label(newtestwindow, text="Sensor 1 Serial Number:", relief="groove", width=25).grid(column=4, row=20, columnspan=2)
        lbls2serial = Label(newtestwindow, text="Sensor 2 Serial Number:", relief="groove", width=25).grid(column=4, row=21, columnspan=2)
        lbls3serial = Label(newtestwindow, text="Sensor 3 Serial Number:", relief="groove", width=25).grid(column=4, row=22, columnspan=2)
        lblincserial = Label(newtestwindow, text="Inclinometer Serial Number:", relief="groove", width=25).grid(column=7, row=14, columnspan=2)
        lblinctest = Label(newtestwindow, text="Inclinemeter Tested?", relief="groove", width=25).grid(column=7, row=15, columnspan=2)
        lblgfltest = Label(newtestwindow, text="GFL Tested?", relief="groove", width=25).grid(column=7, row=16, columnspan=2)
        lblcomtest = Label(newtestwindow, text="Com Port Test?", relief="groove", width=25).grid(column=7, row=17, columnspan=2)
        lblswversion = Label(newtestwindow, text="Software Version", relief="groove", width=25).grid(column=7, row=18, columnspan=2)
        lblsigndate = Label(newtestwindow, text="Date", relief="groove", width=25).grid(column=7, row=19, columnspan=2)
        lblsignname = Label(newtestwindow, text="Name Of Tester:", relief="groove", width=25).grid(column=7, row=20, columnspan=2)
        lblgap1 = Label(newtestwindow, text="", width=15).grid(column=7, row=27)

        lblendtest = Label(newtestwindow, text="WND v2 Protocol Test", relief="groove", width=35).grid(column=7, row=28, columnspan=3)
        lblwndnum = Label(newtestwindow, text="Number", width=15, relief="groove").grid(column=7, row=29)
        lblwndactual = Label(newtestwindow, text="Actual Numbr", width=15, relief="groove").grid(column=8, row=29)
        lblwnddisplayed = Label(newtestwindow, text="Number Displayed", width=15, relief="groove").grid(column=9, row=29)
        lblwndcw1 = Label(newtestwindow, text="1 C/W", width=15, relief="groove").grid(column=7, row=30)
        lblwndcw2 = Label(newtestwindow, text="2 C/W", width=15, relief="groove").grid(column=7, row=31)
        lblwndccw1 = Label(newtestwindow, text="1 CC/W", width=15, relief="groove").grid(column=7, row=32)
        lblwndccw2 = Label(newtestwindow, text="2 CC/W", width=15, relief="groove").grid(column=7, row=33)

        checkretest = Checkbutton(newtestwindow, text="Retest?", variable=retest).grid(column=6, row=12)
        optwheeltype = OptionMenu(newtestwindow, wheeltype, *choicewheel).grid(column=6, row=13)
        entryordernumber = Entry(newtestwindow, textvariable=ordernumber).grid(column=6, row=14)
        optseptype = OptionMenu(newtestwindow, separatortype, *choiceseparator).grid(column=6, row=15)
        optwheellayout = OptionMenu(newtestwindow, layouttype, *choicelayout).grid(column=6, row=16)
        entryserialwheel = Entry(newtestwindow, textvariable=serialwheel).grid(column=6, row=17)
        entryseriallogger = Entry(newtestwindow, textvariable=seriallogger).grid(column=6, row=18)
        entryserialasrim = Entry(newtestwindow, textvariable=serialasrim).grid(column=6, row=19)
        entryserials1 = Entry(newtestwindow, textvariable=serials1).grid(column=6, row=20)
        entryserials2 = Entry(newtestwindow, textvariable=serials2).grid(column=6, row=21)
        entryserials3 = Entry(newtestwindow, textvariable=serials3).grid(column=6, row=22)
        entryserialinc = Entry(newtestwindow, textvariable=serialinclinometer).grid(column=9, row=14)
        optinctest = OptionMenu(newtestwindow, incltested, *choiceYN).grid(column=9, row=15)
        optgfltest = OptionMenu(newtestwindow, gfltested, *choiceYN).grid(column=9, row=16)
        optcomtest = OptionMenu(newtestwindow, comtested, *choiceYN).grid(column=9, row=17)
        entryswversion = Entry(newtestwindow, textvariable=softwareversion).grid(column=9, row=18)
        lbldate = Label(newtestwindow, text=timenow).grid(column=9, row=19)
        entrytestername = Entry(newtestwindow, textvariable=nametester).grid(column=9, row=20)

        entrywndcw1act = Entry(newtestwindow, textvariable=wnd1cwavtual).grid(column=8, row=30)
        entrywndcw2act = Entry(newtestwindow, textvariable=wnd2cwavtual).grid(column=8, row=31)
        entrywndccw1act = Entry(newtestwindow, textvariable=wnd1ccwavtual).grid(column=8, row=32)
        entrywndccw2act = Entry(newtestwindow, textvariable=wnd2ccwavtual).grid(column=8, row=33)
        entrywndcw1disp = Entry(newtestwindow, textvariable=wnd1cwdisplayed).grid(column=9, row=30)
        entrywndcw2disp = Entry(newtestwindow, textvariable=wnd2cwdisplayed).grid(column=9, row=31)
        entrywndccw1disp = Entry(newtestwindow, textvariable=wnd1ccwdisplayed).grid(column=9, row=32)
        entrywndccw2disp = Entry(newtestwindow, textvariable=wnd2ccwdisplayed).grid(column=9, row=33)

        Button(newtestwindow, text="Print Entries", command=lambda:print(cw1.get(), cw2.get())).grid(column=5, row=32)
        Button(newtestwindow, text="CLOSE", command=newtestwindow.destroy).grid(column=5, row=30)
        Button(newtestwindow,text="SAVE").grid(column=5, row=33)

