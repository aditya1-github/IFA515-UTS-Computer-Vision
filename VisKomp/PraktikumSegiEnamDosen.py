#Program Untuk Titik dan Garis
print("\033c")         #To Close All
import numpy as np
import matplotlib.pyplot as plt

#setting the size of the canvas
row = int(1920)
col = int(1080)
print('row, col = ', row, ',', col)

#####Function Untuk Membuat Titik Dan Garis
def buat_titik(Gambar, y1, x1, y2, x2, hd, hw, pr, pb, pg, lr, lg, lb):
    #Draw the first point.
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if ((i - x1) ** 2 + (j - y1) ** 2 ) < hd**2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb
        #Draw the second point.
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) ** 2 + (j - y2) ** 2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    dy = y2 - y1
    dx = x2 - x1
    # Draw the line. Untuk garis yang cendrung horisontal
    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i - x1) + y1) #Finding y using the line equation
            x = i
            y = j
            print('x, y = ', x, ', ', y)
            for i in range(x - hw, x + hw): #creating a circle surrounding (x,y) and coloring it
                for j in range(y - hw, y + hw):
                    if ((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb

    #Drwa the line, untuk garis yang cendrung vertikal
    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)#Finding y using the line equation
            x = i
            y = j
            print('x, y =', x, ', ', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if((i - x) ** 2 + (j - y) ** 2) < hw ** 2:
                        Gambar[j, i, 2] = lr
                        Gambar[j, i, 2] = lg
                        Gambar[j, i, 2] = lb
        return Gambar

## MAIN PROGRAM
# USER ENTRIES
# Point Coordinates
y1 = 200; x1 = 100
y2 = 200; x2 = 800

# Point diameter and color
pd = int(3); pr = 255; pg = 0; pb = 0
# The user decide the line width and color
lw = int(3); lr = 255; lg = 0; lb = 0
hd = int(pd/2)                          #Calculate the half point diameter
hw = int(lw/2)                          #Calculate the half line width

#MEMBUAT OBJEK RECTANGLE
Gambar = np.zeros(shape=(row, col, 3), dtype=np.int16) #latar hitam
Gambar[:, :, :] = 255
y1 = 200; x1 = 100
y2 = 200; x2 = 800
while y2 < 401:
    y1 += 1
    y2 += 1
    titik = buat_titik(Gambar, y1, x1, y2, x2, hd, hw, pr, pb, pg, lr, lg, lb)
    hasil = titik
    Gambar = hasil
plt.figure(1)
plt.imshow(hasil)
plt.show()