# PROGRAM UNTUK PERSEGI PANJANG
print("\033c")  # To close all

# LIBRARY YANG DIBUTUHKAN
import numpy as np
import matplotlib.pyplot as matplot

# ==============================================================================================
# ======================================= MEMBUAT FUNGSI =======================================
# ==============================================================================================
# Funsi untuk membuat titik
def create_dot(no_of_points, hd, cordinate_x, cornidate_y, screen):
    # MENGGAMBAR 4 TITIK DENGAN WARNA PUTIH (loop, condition, comparation)
    for k in range(1, no_of_points + 1):
        x = cordinate_x[k]
        y = cornidate_y[k]
        for i in range(x - hd, x + hd):
            for j in range(y - hd, y + hd):
                if ((i - x) ** 2 + (j - y) ** 2) < hd ** 2:
                    screen[j, i, :] = 255 #225 adalah warna putih

def create_line(no_of_points, cordinate_x, cordinate_y, hw, screen):
    for k in range(1, no_of_points + 1):
        xa = cordinate_x[k];	xb = cordinate_x[k + 1]
        ya = cordinate_y[k];	yb = cordinate_y[k + 1]
        x_min = min(xa, xb);	x_max = max(xa, xb)
        y_min = min(ya, yb);	y_max = max(ya, yb)
        dy = yb - ya;	dx = xb - xa

        if abs(dy) <= abs(dx):
            line(dy, dx, x_min, x_max, xa, ya, hw, screen, "column")

        if abs(dx) < abs(dy):
            line(dx, dy, y_min, y_max, ya, xa, hw, screen, "row")

def line(d1, d2, min, max, a1, a2, diameter_w, screen, direction):
    my = d1 / d2
    for i in range(min, max):
        j = int(my * (i - a1) + a2)  # MENCARI Y MENGGUNAKAN NILAI X
        # print('x, y =', i, ',', j)

        screen[j, i, 0] = 255
        screen[j, i, 1] = 0
        screen[j, i, 2] = 0

        if direction == "column":
            border_line(i, j, diameter_w, screen)
        else:
            # row
            border_line(j, i, diameter_w, screen)

def border_line(x, y, diameter_w, screen):
    for i in range(x - diameter_w, x + diameter_w):  # MEMBUAT LINGKARAN DI SEKITAR (X,Y) DAN MEWARNAINYA DENGAN WARNA BIRU
        for j in range(y - diameter_w, y + diameter_w):
            if ((i - x) ** 2 + (j - y) ** 2) < diameter_w ** 2:
                #screen[j, i, 2] = 255
                screen[j, i, 0] = 255
                screen[j, i, 1] = 0
                screen[j, i, 2] = 0

# ==============================================================================================
# ======================================= PROGRAM UTAMA ========================================
# ==============================================================================================

# PENGATURAN UKURAN LAYAR
# col = int(1920); row = int(1080)
col = int(800); row = int(800)

# MENENRUKAN JUMLAH TITIK YANG DIGUNAKAN, UNTUK PERSEGI PANJANG ADALAH 4 TITIK.
# TITIK JUGA BISA DIBUAT MENJADI INPUTAN OLEH USER
no_of_points = 7

#Structure of the array relative to the point-1 up to point-7:
#The value of the last position is the same as x1
#This is to anticipate the drawing of the line between p4 and p1
# xn ADALAH KOORDINAT X DAN yn ADALAH KOORDINAT Y
# XN DAN YN HARUS BERJUMLAH SAMA DAN PEMASANGANNYA BERDASARKAN NILAI INDEX,
# CONTOH X PADA INDEX 1 DIPASANGKAN DENGAN Y PADA INDEX 1
cordinate_y = [0, 400, 200, 200, 400, 600, 600, 400, 400]
cordinate_x = [0, 169, 285, 515, 631, 515, 285, 169, 631]

# PENGATURAN UNTUK DIAMETER TITIK DAN LEBAR BARIS
pd = int(20); lw = int(10)

# MENGHITUNG DIAMTER SETENGAH TITIK DAN LEBAR SETENGAH GARIS
hd = int(pd/2); hw = int(lw/2)

# MEMPERSIAPKAN LAYAR DENGAN WARNA HITAM
screen = np.zeros(shape=(row, col, 3), dtype=np.uint16)
screen[:, :, :] = 255

# MENGGAMBAR 4 TITIK DENGAN WARNA PUTIH (loop, condition, comparation)
#create_dot(no_of_points, hd, cordinate_x, cordinate_y, screen)

# MEMBUAT BARIS DIANTARA TITIK-1 DAN TITIK-2, DIANTARA TITIK-2 DAN TITIK LAINNYA
create_line(no_of_points, cordinate_x, cordinate_y, hw, screen)

matplot.figure()
matplot.imshow(screen)
matplot.show()