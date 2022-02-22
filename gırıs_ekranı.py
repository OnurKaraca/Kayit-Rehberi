
import sqlite3
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk 
#github
ekran=Tk()

ekran.geometry('380x445')
ekran.configure(bg='#ba161e')
ekran.title("GIRIS EKRANI")

def gor():
    os.system('projem.db')


def acılırp():
    pencere =Toplevel()

    tel =0
    rehber=[]

    def yaz(x):
        c=len(numara.get())
        numara.insert(c,str(x))
        #print(x)

    def delete():
        #global numara
        numara.delete(0,END)


    pencere.resizable(width="FALSE", height="FALSE")
    pencere.configure(bg='black')
    pencere.geometry("330x450")
    pencere.title("NUMARA GIRIS")

    etiket=Label(pencere,text="TELEFON", fg="green",bg='black', font="Verdana 12 bold")
    etiket.pack()

    sil= Button(pencere,text='Del\n ✘',font='Verdana 13',fg='red',bg='black',width=3,justify=LEFT,command=delete)
    sil.place(x=250,y=89,height=267)

    numara = Entry(pencere,font="Verdana 15 bold",fg='white',bg='black',relief=SUNKEN,width=18,justify=CENTER)
    numara.place(x=40,y=50)

    resim=ImageTk.PhotoImage(Image.open('logo.png'))

    logo=Label(pencere,image=resim,bg='black',relief=FLAT)
    logo.place(x=250,y=365)

    a=[]
    for i in range(1,10):
        a.append(Button(pencere,text=str(i),font="Verdana 20 bold",bg='black',fg='white',command=lambda x=i:yaz(x)))
    sayac=0
    for i in range(0,3):
        for j in range(0,3):
            a[sayac].place(x=50+j*70,y=90+i*70)
            sayac+=1

    yb= Button(pencere,text='*',font='Verdana 20 bold',bg='black',fg='white',command=lambda x='*':yaz(x))
    yb.place(x=50,y=300)

    sb= Button(pencere,text='0',font='Verdana 20 bold',bg='black',fg='white',command=lambda x='0':yaz(x))
    sb.place(x=120,y=300)

    kb= Button(pencere,text='#',font='Verdana 20 bold',bg='black',fg='white',command=lambda x='#'  :yaz(x))
    kb.place(x=190,y=300)

    def thing():
        global tel
        tel = numara.get()
        if tel=='':
            messagebox.showinfo("UYARI!","Bu Alan Boş Bırakılamaz!")
        else:  
            rehber.append(tel)
            print(rehber)
            numara.delete(0,END)
            ekran2=Toplevel()
        

        def add():
            grsi = isimg.get()
            grss = soyig.get()
            if grsi=='' and grss=='':
                messagebox.showinfo("UYARI!","Bu Alan Boş Bırakılamaz!")
            else:
                rehber.append(grsi)
                rehber.append(grss)
                messagebox.showinfo("BILGI!","ISIM KAYDEDILDI")
                isimg.delete(0,END)
                soyig.delete(0,END)

                veriler = [(grsi,grss,tel)]

                vert = sqlite3.connect("projem.db")
                imlc = vert.cursor()

                imlc.execute("CREATE TABLE IF NOT EXISTS REHBER (ISIM TEXT, SOYISIM TEXT, NUMARA INT)")
                
                for i in veriler:
                    imlc.execute("insert into REHBER VALUES(?,?,?)",(i))

                vert.commit()
                vert.close()
                print(rehber)

        ekran2.resizable(width=False,height=False)
        ekran2.geometry('330x350')
        ekran2.configure(bg='#222222')
        ekran2.title("ISIM EKLE")

        isimg = Entry(ekran2,font="Verdana 15 bold",fg='white',bg='#555555',relief=FLAT,width=5,justify=LEFT)
        isimg.place(relx=0,rely=0.25,relwidth=1,relheight=0.10)

        isiml = Label(ekran2,text="ISIM GIRINIZ :", fg="green",bg='#222222', font="Verdana 12 bold")
        isiml.place(relx=0.01,rely=0.18)

        soyig = Entry(ekran2,font="Verdana 15 bold",fg='white',bg='#555555',relief=FLAT,width=5,justify=LEFT)
        soyig.place(relx=0,rely=0.47,relwidth=1,relheight=0.10)

        soyil = Label(ekran2,text="SOYAD GIRINIZ :", fg="green",bg='#222222', font="Verdana 12 bold")
        soyil.place(relx=0.01,rely=0.40)

        kayit = Button(ekran2,text="KAYDET ✓",font="Verdana 20 bold",fg="green",bg='#222222',command=add,relief=RAISED,justify=CENTER,width=10)
        kayit.place(x=65,y=250)


        ekran2.mainloop()

    kayit = Button(pencere, text="KAYDET ✓" ,fg='dark green',bg='black',cursor="hand2",command=thing,font="Verdana 13 bold")
    kayit.place(x=50,y=370,width=188)
    pencere.mainloop()


made = Label(text='O.K.',font="Papyrus 10",relief=FLAT,cursor="gumby",bg='#ba161e',fg='white')
made.place(relx=0.89,rely=0.94)

baslık = Label(text='REHBER',font="Playbill 100",relief=FLAT,bg='#ba161e')
baslık.place(relx=0,rely=0,relwidth=1)

simge1=PhotoImage(file="ekle1.png")
simge2=PhotoImage(file="kisi.png")

ekle = Button(text='  Yeni Numara Ekleme',font="Rockwell 15 bold",image=simge1,compound="left",relief=RAISED,cursor="hand2",bg='#ba161e',command=acılırp)
ekle.place(relx=0,rely=0.39,relwidth=1.0,relheight=0.2)

guncelle = Button(text='  Kişiyi Görüntüle', font="Rockwell 15 bold",image=simge2,compound="left",relief=RAISED,cursor="hand2",bg='#ba161e',command=gor)
guncelle.place(relx=0,rely=0.6,relwidth=1.0,relheight=0.2)




ekran.mainloop()