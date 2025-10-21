import tkinter as tk
import random


# Ekran ayarları
window = tk.Tk()
window.title('Sayıyı Tahmin Et')
window.minsize(600, 400)
window.config(bg='gray')

# Label Ayarları
label1 = tk.Label(window, text='0 ile 20 arasındaki sayıyı tahmin et',font=('Arial',12,'bold'))
label1.config(bg='gray',fg='white')
#label1.place(x=50,y=120)
label1.pack_forget()

soruişareti=tk.Label(window, text="?",font=('Arial',25,'bold'))
soruişareti.config(bg='gray',fg='black')
#soruişareti.place(x=170,y=55)
soruişareti.pack_forget()

label_sonuc = tk.Label(window, text='',font=('Arial',18,'bold'))
label_sonuc.config(bg='gray',fg='red')
#label_sonuc.place(x=150,y=230)
label_sonuc.pack_forget()

label_sonuc2 = tk.Label(window, text='',font=('Arial',18,'bold'))
label_sonuc2.config(bg='gray',fg='green')
label_sonuc2.pack_forget()

label_name=tk.Label(window, text='Adınızı girin:',font=('Arial',14,'bold'))
label_name.config(bg='gray',fg='white')
label_name.pack_forget()

label_uyari=tk.Label(window, text='',font=('Arial',14,'bold'))
label_uyari.config(bg='gray',fg='white')
label_uyari.pack_forget()

# Fonksiyonlar
x = random.randint(0, 20)
skor = 0

def start():

    ##
    label_uyari.place(x=370,y=110)
    label_name.place(x=370, y=20)
    entry_name.place(x=370, y=50)
    button_name.place(x=400, y=80)
    label_uyari.place(x=370, y=135)
    button_start.config(state="disabled")
    skor_yazdir()

def tahmin_et():
    label_sonuc2.config(text="")
    global skor
    try:
        tahmin = int(entry1.get())
        skor += 1
    except ValueError:
        label_sonuc2.config(text="Geçerli birsayı girin")
        return

    if (tahmin == x):
        label_sonuc2.config(text=f"Tebrikler toplam {skor} tahminde bildiniz")
        label_sonuc.config(text="")
        skor_ekle()
        skor_yazdir()
    elif (tahmin > x):
        label_sonuc.config(text="Daha küçük")
        animasyon()
    elif (tahmin < x):
        label_sonuc.config(text="Daha büyük")
        animasyon()
    else:
        label_sonuc.config(text="Hatalı Tahmin")

def stop():
    global skor
    global x
    button_start.config(state="normal")
    soruişareti.place_forget()
    label_sonuc.place_forget()
    button_tahmin.place_forget()
    button_stop.place_forget()
    entry1.place_forget()
    label1.place_forget()
    label_sonuc2.place_forget()
    label_sonuc2.config(text="")
    entry1.delete(0, tk.END)
    label_sonuc2.config(text="")
    label_uyari.place_forget()
    label_uyari.config(text="")
    button_name.place_forget()
    entry_name.place_forget()
    label_name.place_forget()
    entry_name.delete(0, tk.END)
    skor = 0
    x = random.randint(0, 20)
    label_sonuc.config(text="")
    button_restart.place_forget()

def giriş_yap():
    name = entry_name.get().strip()
    if (name == ""):
        label_uyari.config(text="Lütfen isim giriniz")
    else:
        label_uyari.config(text= {name})
        soruişareti.place(x=170, y=55)
        label1.place(x=50, y=120)
        label_sonuc.place(x=130, y=230)
        button_tahmin.place(x=100, y=180)
        button_stop.place(x=550, y=0)
        entry1.place(x=82, y=150)
        label_sonuc2.place(x=130, y=290)
        button_restart.place(x=220, y=180)

def restart():
    global x
    global skor
    skor = 0
    label_sonuc2.config(text="")
    label_sonuc.config(text="")
    entry1.delete(0, tk.END)
    x = random.randint(0, 20)

def animasyon():
    renk = label_sonuc.cget("foreground")
    if renk == "red":
        label_sonuc.config(fg="pink")
    else:
        label_sonuc.config(fg="red")

def skor_ekle():
    name = entry_name.get().strip()
    with open("skorlar.txt","a") as dosya:
        dosya.write(f"{name} - {skor}  \n")

def skor_yazdir():
    list_skor.delete(0, tk.END)
    global a
    name = entry_name.get().strip()
    skorlar = []
    with open ("skorlar.txt","r") as dosya:
        for satir in dosya:
            satir = satir.strip()
            if satir:
                isim , skor = satir.split("-")
                skor = int(skor)
                isim = isim
                if skor<6:
                    skorlar.append((isim , int(skor)))
    skorlar.sort(key= lambda x :x[1])
    for isim , skor in skorlar:
        list_skor.insert(tk.END, f" {isim} - {skor} ")

# button ayarları
button_start=tk.Button(text="Oyunu Başlat",command=start)
button_start.config(bg='red',fg='white')
button_start.config(bg='green',fg='white')
button_start.config(height=3,width=40)
button_start.place(x=50,y=5)

button_tahmin=tk.Button(text="Tahmin Et", command=tahmin_et)
button_tahmin.config(bg='yellow', fg='black')
button_tahmin.config(height=2, width=15)
#button1.place(x=100,y=180)
button_tahmin.pack_forget()

button_stop=tk.Button(text="X",command=stop)
button_stop.config(bg='red',fg='white')
button_stop.config(width=5,height=2)
#button_stop.place(x=550,y=0)
button_stop.pack_forget()

button_name=tk.Button(text="Giriş Yap",command=giriş_yap)
button_name.config(bg='blue',fg='black')
button_name.config(width=6,height=2)
button_name.pack_forget()

button_restart=tk.Button(text="Restart",command= restart)
button_restart.config(bg='red',fg='white')
button_restart.config(width=5,height=2)
button_restart.place_forget()

# Entry ayarları
entry1 = tk.Entry(width=30)
#entry1.place(x=82,y=150)
entry1.pack_forget()

entry_name=tk.Entry(width=20)
entry_name.place_forget()

#Listbox ayarları
list_skor=tk.Listbox(height=8,width=40)
list_skor.config(background='aqua')
list_skor.pack(side=tk.RIGHT)

window.bind("<Return>",lambda event:tahmin_et()) # Entere basınca Tahmin et butonu çalışıyor
window.mainloop()