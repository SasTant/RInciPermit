import Rinci_Permit as RP
import tkinter as teka

cen_ut = teka.Tk() #cendela utama

def pencet_hs():
    e.delete(0, teka.END)
    sem2 =  str(RP.hitung_sel())
    e.insert(0, sem2)
    # label2 = teka.Label(cen_ut, text = sem2 )
    # label2.pack()


def kosong():
    e.delete( 0,'end')


def sal_in(): #salah input
    e.insert(0, 'Masukan salah,Ulangi dengan nilai Indeks yang sesuai! ')


def tan_exp(): #tangkap expiry
    e.delete(0, teka.END)
    angka = angk.get()
    if angka.isnumeric(): # == True:
        angka_i = int(angka)
        if angka_i < len(RP.hitung_exp()) and angka_i > -1:
            sem = RP.hitung_sel_exp(angka_i)
            e.insert(0,str(sem))
        else:
            sal_in()
    else:
        sal_in()
        # sem = RP.hitung_sel_exp(0)
        # e.insert(0,str(sem))


e = teka.Entry(cen_ut, width=90, borderwidth=5, fg='blue')
e.pack()
# e.insert(0,"0")

angk = teka.Entry(cen_ut, width=5, borderwidth=5, fg='blue')
angk.pack()
angk.insert(0,"0")


label = teka.Label(cen_ut, text="TES \n Progran Rinci Permit")
label.pack()

# label2 = teka.Label(cen_ut, text=str(RP.hitung_exp()) + "\n Indeks expiry mulai dr [0, 1, 2, ...dst]")
label2 = teka.Label(cen_ut, text=str(RP.cetak_basi()))
label2.pack()

tombol= teka.Button(cen_ut, text="Rinci kode sel & Jumlah", command = pencet_hs, fg="green")
tombol.pack()

tombol2 = teka.Button(cen_ut,text="Masukkan Indeks Expiry", command = tan_exp )
tombol2.pack()

tombol3 = teka.Button(cen_ut,text="Kosongkan Display", command = kosong )
tombol3.pack()

cen_ut.mainloop()
