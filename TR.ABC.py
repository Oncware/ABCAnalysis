import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import threading
def grafik_ciz(toplam_fiyatlar_liste, kumulatif_toplam_liste, urun_adlari):
    plt.plot(toplam_fiyatlar_liste, label='Toplam Fiyatlar')
    plt.plot(kumulatif_toplam_liste, label='Kümülatif Toplam')
    plt.xlabel('Ürünler')
    plt.ylabel('Fiyat')
    plt.title('ABC Analizi')
    plt.legend()
    plt.xticks(range(len(urun_adlari)), urun_adlari)
    plt.show()
def satir_ekle():
    urun_adi = tk.StringVar()
    birim_fiyati = tk.StringVar()
    adet = tk.StringVar()
    toplam_fiyat = tk.StringVar()
    urunler.append([urun_adi, birim_fiyati, adet, toplam_fiyat])
    satir = len(urunler)
    ttk.Entry(mainframe, textvariable=urun_adi).grid(column=0, row=satir, sticky=(tk.W, tk.E))
    ttk.Entry(mainframe, textvariable=birim_fiyati).grid(column=1, row=satir, sticky=(tk.W, tk.E))
    ttk.Entry(mainframe, textvariable=adet).grid(column=2, row=satir, sticky=(tk.W, tk.E))
    ttk.Entry(mainframe, textvariable=toplam_fiyat).grid(column=3, row=satir, sticky=(tk.W, tk.E))
def hesapla():
    try:
        toplam_fiyatlar = [(float(urun[1].get()) * float(urun[2].get()), urun[0].get()) if urun[1].get() else (float(urun[3].get()), urun[0].get()) for urun in urunler]
        toplam_fiyatlar.sort(reverse=True)
        toplam = sum([fiyat for fiyat, ad in toplam_fiyatlar])
        kumulatif_toplam = 0
        veri = []
        toplam_fiyatlar_liste = []
        kumulatif_toplam_liste = []
        urun_adlari = []
        for fiyat, ad in toplam_fiyatlar:
            kumulatif_toplam += fiyat
            yuzde = (kumulatif_toplam / toplam) * 100
            if yuzde <= 80:
                grup = 'A'
            elif yuzde <= 95:
                grup = 'B'
            else:
                grup = 'C'
            veri.append([ad, fiyat, kumulatif_toplam, yuzde, grup])
            toplam_fiyatlar_liste.append(fiyat)
            kumulatif_toplam_liste.append(kumulatif_toplam)
            urun_adlari.append(ad)
        threading.Thread(target=grafik_ciz, args=(toplam_fiyatlar_liste, kumulatif_toplam_liste, urun_adlari)).start()
        df = pd.DataFrame(veri, columns=['Ürün Adı', 'Toplam Fiyat', 'Kümülatif Toplam', 'Kümülatif Yüzde', 'Grup'])
        yeni_pencere = tk.Toplevel()
        text = tk.Text(yeni_pencere)
        text.pack()
        text.insert(tk.END, df.to_string(index=False))
    except ValueError:
        print("Lütfen geçerli sayılar girin")
root = tk.Tk()
root.title("ABC Analizi")
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
ttk.Label(mainframe, text="Ürün Adı").grid(column=0, row=0, sticky=(tk.W, tk.E))
ttk.Label(mainframe, text="Birim Fiyatı").grid(column=1, row=0, sticky=(tk.W, tk.E))
ttk.Label(mainframe, text="Adet").grid(column=2, row=0, sticky=(tk.W, tk.E))
ttk.Label(mainframe, text="Toplam Fiyat").grid(column=3, row=0, sticky=(tk.W, tk.E))
urunler = []
ttk.Button(mainframe, text="Satır Ekle", command=satir_ekle).grid(column=0, row=100, sticky=(tk.W, tk.E))
ttk.Button(mainframe, text="Hesapla", command=hesapla).grid(column=3, row=100, sticky=(tk.W, tk.E))
satir_ekle()
root.mainloop()
