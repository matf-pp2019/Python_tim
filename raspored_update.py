import tkinter
from tkinter import *

window = Tk()
window.title("Raspored")
window.geometry("1100x300")


###  OKVIR ###

### DANI ###

predmet = Label(window, text= "Ime predmeta")
predmet.grid(column=0, row=0)

predmet1 = Entry(window, width=11)
predmet1.grid(column=1, row=0)


dan = Label(window, text= "Dan u nedelji")
dan.grid(column=0, row=1)

dan1 = Entry(window, width=11)
dan1.grid(column=1, row=1)


vrp = Label(window, text= "Vreme pocetka casa")
vrp.grid(column=0, row=2)

vrp1 = Entry(window, width=11)
vrp1.grid(column=1, row=2)


vrk = Label(window, text= "Vreme kraja casa")
vrk.grid(column=0, row=3)

vrk1 = Entry(window, width=11)
vrk1.grid(column=1, row=3)

for i in range(6,11):
    for j in range(1,14):
        l = Label(text=" ", relief=RIDGE)
        l.grid(row=i, column=j, sticky=NSEW)

for i in range(6,7):
    for j in range(1,2):
        l = Label(text="dsadsa", relief=RIDGE)
        l.grid(row=i, column=j, sticky=NSEW)

dv = Label(text="Dan \ Vreme", heigh=1, width=10, relief=RIDGE )
dv.grid(column=0, row=5)

pon = Label(text="Ponedeljak ", bg="silver",
            heigh=1, width=10, relief=RIDGE)
pon.grid(column=0, row=6)

ut = Label(text="Utorak ", bg="silver",
            heigh=1, width=10, relief=RIDGE)
ut.grid(column=0, row=7)

sreda = Label(text="Sreda ", bg="silver",
                heigh=1, width=10, relief=RIDGE)
sreda.grid(column=0, row=8)

cet = Label(text="Cetvrtak ", bg="silver",
                heigh=1, width=10, relief=RIDGE)
cet.grid(column=0, row=9)

petak = Label(text="Petak ", bg="silver",
                  heigh=1, width=10, relief=RIDGE)
petak.grid(column=0, row=10)

label1 = Label(text="08:00 - 09:00", relief=RIDGE)
label1.grid(column=1, row=5)

label2 = Label(text="09:00 - 10:00", relief=RIDGE)
label2.grid(column=2, row=5)

label3 = Label(text="10:00 - 11:00", relief=RIDGE)
label3.grid(column=3, row=5)

label4 = Label(text="11:00 - 12:00", relief=RIDGE)
label4.grid(column=4, row=5)

label5 = Label(text="12:00 - 13:00", relief=RIDGE)
label5.grid(column=5, row=5)

label6 = Label(text="13:00 - 14:00", relief=RIDGE)
label6.grid(column=6, row=5)

label7 = Label(text="14:00 - 15:00", relief=RIDGE)
label7.grid(column=7, row=5)

label8 = Label(text="15:00 - 16:00", relief=RIDGE)
label8.grid(column=8, row=5)

label9 = Label(text="16:00 - 17:00", relief=RIDGE)
label9.grid(column=9, row=5)

label10 = Label(text="17:00 - 18:00", relief=RIDGE)
label10.grid(column=10, row=5)

label11 = Label(text="18:00 - 19:00", relief=RIDGE)
label11.grid(column=11, row=5)

label12 = Label(text="19:00 - 20:00", relief=RIDGE)
label12.grid(column=12, row=5)

label13 = Label(text="20:00 - 21:00", relief=RIDGE)
label13.grid(column=13, row=5)



dodaj = Button(window, text="Upisi")
dodaj.grid(column=3, row = 2, sticky = NSEW)




window.mainloop()
