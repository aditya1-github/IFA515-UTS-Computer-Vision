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
# # Point diameter and color
pd = int(3); pr = 255; pg = 0; pb = 0
# # The user decide the line width and color
lw = int(3); lr = 255; lg = 0; lb = 0
hd = int(pd/2)                          #Calculate the half point diameter
hw = int(lw/2)                          #Calculate the half line width

#MEMBUAT GARIS OBJEK HEXAGON
Gambar = np.zeros(shape=(row, col, 3),dtype=np.int16) #latar hitam
Gambar[:, :, :] = 255

#GARIS DIBUAT DARI KIRI KE KANAN / DARI KOORDINAT 0

#KOORDINAT GARIS LUAR
#              p1,   p2, p3,  p4, p5,  p6,   p1
cordinate_y = [200, 200, 400, 600, 600, 400, 200]
cordinate_x = [285, 515, 631, 515, 285, 169, 285]


def create_line_hexagon(Gambar, cordinate_x, cordinate_y):#param
    for i in range(0, len(cordinate_y)-1): # perulangan sebanyak koordinat y
        if cordinate_x[i+1] < cordinate_x[i]: #kondisi membuat garis dari kiri ke kanan
                hasil = buat_garis(Gambar, cordinate_y[i+1], cordinate_x[i+1], cordinate_y[i], cordinate_x[i], hd, hw,pr, pb, pg, lr, lg, lb)
                Gambar = hasil
        else:
                hasil = buat_garis(Gambar, cordinate_y[i], cordinate_x[i], cordinate_y[i+1], cordinate_x[i+1], hd, hw, pr, pb, pg, lr, lg, lb)
                Gambar = hasil
        #print hasil
        plt.figure(2)
        plt.imshow(hasil)
        plt.show()
        # print hasil
    return hasil

def create_line_hexagon_in(Gambar, cordinate_x, cordinate_y):
    for i in range(0, 3): # membuat garis dalam sebanyak 3 kali
        if cordinate_x[i + 3] < cordinate_x[i]:
            hasil = buat_garis(Gambar, cordinate_y[i+3], cordinate_x[i+3], cordinate_y[i], cordinate_x[i], hd, hw, pr,pb, pg, lr, lg, lb)
            Gambar = hasil
        else:
            hasil = buat_garis(Gambar, cordinate_y[i], cordinate_x[i], cordinate_y[i+3], cordinate_x[i+3], hd, hw, pr, pb, pg, lr, lg, lb)
            Gambar = hasil
        plt.figure(2)
        plt.imshow(hasil)
        plt.show()
    return hasil

def fill_hexagon_in(Gambar, cordinate_x, cordinate_y):
    for i in range(1, 7):
        y2 = 400
        x2 = 400
        if i % 2 == 0:
            if i >= 3 and i < 5: #4
                while cordinate_x[i] <= cordinate_x[i-1]:
                    cordinate_x[i] += 1
                    hasil = buat_garis(Gambar, y2, x2, cordinate_y[i], cordinate_x[i], hd, hw, pr, pb, pg, lr,lg, lb)
                    Gambar = hasil
            elif i >= 5: #6
                while x2 >= cordinate_x[i-1]:
                    x2 -= 1
                    hasil = buat_garis(Gambar, cordinate_y[i], cordinate_x[i], y2, x2, hd, hw, pr, pb, pg, lr,lg, lb)
                    Gambar = hasil
            else: #2
                while x2 <= cordinate_x[i]:
                    x2 += 1
                    hasil = buat_garis(Gambar, cordinate_y[i - 1], cordinate_x[i - 1], y2, x2, hd, hw, pr, pb, pg, lr, lg,lb)
                    Gambar = hasil
        else:
            if i >= 3 and i < 5: #3
                while x2 <= cordinate_x[i-1]:
                    x2 += 1
                    hasil = buat_garis(Gambar, y2, x2, cordinate_y[i], cordinate_x[i], hd, hw, pr, pb, pg, lr,lg, lb)
                    Gambar = hasil
            elif i >= 5: #5
                while x2 >= cordinate_x[i]:
                    x2 -= 1
                    hasil = buat_garis(Gambar, y2, x2, cordinate_y[i-1], cordinate_x[i+1], hd, hw, pr, pb, pg, lr,lg, lb)
                    Gambar = hasil
            else: # 1
                while cordinate_x[i - 1] <= cordinate_x[i]:
                    cordinate_x[i-1] += 1
                    hasil = buat_garis(Gambar, cordinate_y[i-1], cordinate_x[i-1], y2, x2, hd, hw, pr, pb, pg, lr, lg, lb)
                    Gambar = hasil
        plt.figure(2)
        plt.imshow(hasil)
        plt.show()
    return hasil

hasil = create_line_hexagon(Gambar, cordinate_x, cordinate_y)
hasil = create_line_hexagon_in(Gambar, cordinate_x, cordinate_y)
hasil = fill_hexagon_in(Gambar, cordinate_x, cordinate_y)
plt.figure(2)
plt.imshow(hasil)
plt.show()