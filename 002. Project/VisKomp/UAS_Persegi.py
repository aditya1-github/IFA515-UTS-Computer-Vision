#Program Untuk Titik dan Garis
print("\033c")         #To Close All
import numpy as np
import matplotlib.pyplot as plt
from LibCreateLine import buat_garis

#setting the size of the canvas
row = int(800)
col = int(800)
print('row, col =', row, ',' , col)

## MAIN PROGRAM
# # Point diameter and color (RGB Kuning 255;255;0)
pd = int(4); pr = 255; pg = 255; pb = 0
# # The user decide the line width and color (RGB Kuning 255;255;0)
lw = int(4); lr = 255; lg = 255; lb = 0
hd = int(pd/2)                          #Calculate the half point diameter
hw = int(lw/2)                          #Calculate the half line width

#MEMBUAT GARIS OBJEK HEXAGON
Gambar = np.zeros(shape=(row, col, 3),dtype=np.uint8) #latar hitam
Gambar[:, :, :] = 0

#KOORDINAT GARIS
cordinate_y = [200, 200, 400, 400, 300, 200]
cordinate_x = [500, 200, 200, 500, 400, 500]

# METHOD MEMBUAT TITIK DAN GARIS
def create_line_hexagon(Gambar, cordinate_x, cordinate_y):#param
    for i in range(0, len(cordinate_y)-1): # perulangan sebanyak koordinat y
        if cordinate_x[i+1] < cordinate_x[i]: #kondisi membuat garis dari kiri ke kanan
                hasil = buat_garis(Gambar, cordinate_y[i+1], cordinate_x[i+1], cordinate_y[i], cordinate_x[i], hd, hw,pr, pb, pg, lr, lg, lb)
                Gambar = hasil
        else:
                hasil = buat_garis(Gambar, cordinate_y[i], cordinate_x[i], cordinate_y[i+1], cordinate_x[i+1], hd, hw, pr, pb, pg, lr, lg, lb)
                Gambar = hasil
        #print hasil
        plt.figure("Persegi dan Segitiga Siku")
        plt.imshow(hasil)
        plt.show()
        # print hasil

    # DI AKHIR MEMBUAT GARIS VERTIKAL UNTUK SEGITIGA SIKU
    #       buat_garis(Gambar,  y1,  x1,  y2,  x2, hd, hw, pr,pb, pg, lr, lg, lb)
    hasil = buat_garis(Gambar, 200, 400, 400, 400, hd, hw, pr, pb, pg, lr, lg, lb)
    plt.figure("Persegi dan Segitiga Siku")
    plt.imshow(hasil)
    plt.show()

    return hasil

# METHOD MEMBERI WARNA PADA GARIS PADA PERSEGI
def fill_in(Gambar, cordinate_x, cordinate_y):
    i = 1
    while i <= cordinate_x[1]:
        #       buat_garis(Gambar,  y1,  x1,  y2,  x2, hd, hw, pr,pb, pg, lr, lg, lb)
        hasil = buat_garis(Gambar, cordinate_y[1] + i, cordinate_x[1], cordinate_y[1] + i, cordinate_x[4], hd, hw, pr, pb, pg, lr, lg, lb)
        Gambar = hasil
        i += 1

    plt.figure("Persegi dan Segitiga Siku")
    plt.imshow(hasil)
    plt.show()

    return hasil

# ================= MAIN PROGRAM =================
# MEMBUAT TITIK DAN GARIS PERSEGI DAN SEGITIGA SIKU
hasil = create_line_hexagon(Gambar, cordinate_x, cordinate_y)

# MEWARNAI PERSEGI DENGAN WARNA MERAH
hasil = fill_in(Gambar, cordinate_x, cordinate_y)

# SIMPAN MENJADI FILE GAMBAR .jpg
plt.imsave("Persegi dan Segitiga Siku.jpg", hasil)
