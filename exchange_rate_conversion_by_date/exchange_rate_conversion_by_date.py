import tkinter as tk
from currency_converter import CurrencyConverter
from datetime import date

root=tk.Tk()
root.title("Exchange Yazılımı")
root.geometry("300x200")

c = CurrencyConverter(fallback_on_missing_rate=True, decimal=True)

def exchange():
    tutar = (tutar_entry.get())
    nereden = str(nereden_entry.get()).upper()
    nereye = str(nereye_entry.get()).upper()
    tarih = tarih_entry.get()
    
    tarih_liste = tarih.split("-")
    gun = int(tarih_liste[0])
    ay = int(tarih_liste[1])
    yil = int(tarih_liste[2])
    
    try:
        donusum = c.convert(tutar, nereden, nereye, date=date(yil, ay, gun))
        sonuc_label['text'] = f"{round(donusum, 2)} {nereye}"
    except:
        hata = "Hatalı değer girdiniz. Tekrar deneyin"
        sonuc_label['text'] = f"{hata}"
        
	
tutar_label = tk.Label(master=root, text = 'Tutar', font=('calibre',10, 'bold'))
tutar_entry = tk.Entry(master=root, font=('calibre',10,'normal'))

nereden_label = tk.Label(master=root, text = 'Hangi birimden', font = ('calibre',10,'bold'))
nereden_entry=tk.Entry(master=root, font = ('calibre',10,'normal'))

nereye_label = tk.Label(master=root, text = 'Hangi birime', font = ('calibre',10,'bold'))
nereye_entry=tk.Entry(master=root, font = ('calibre',10,'normal'))

tarih_label = tk.Label(master=root, text = 'Tarih', font = ('calibre',10,'bold'))
tarih_entry=tk.Entry(master=root, font = ('calibre',10,'normal'))

buton=tk.Button(master=root,text = 'Dönüştür', command = exchange)

sonuc_label = tk.Label(master=root, text = '0.00', font = ('calibre',10,'bold'))
#-----------------------------------------

tutar_label.grid(row=0,column=0)
tutar_entry.grid(row=0,column=1)

nereden_label.grid(row=1,column=0)
nereden_entry.grid(row=1,column=1)

nereye_label.grid(row=2,column=0)
nereye_entry.grid(row=2,column=1)

tarih_label.grid(row=3,column=0)
tarih_entry.grid(row=3,column=1)

buton.grid(row=4,column=1)

sonuc_label.grid(row=5, column=1)

root.mainloop()
