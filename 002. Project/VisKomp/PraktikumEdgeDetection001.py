#Program Untuk Titik dan Garis
print("\033c")         #To Close All
import numpy as np
import matplotlib.pyplot as plt

#setting the size of the canvas
row = int(800)
col = int(800)
#setting  batas vertikal (tinggi / 2) 2 adalah area warn
batas1 = int(row/2)
batas2 = int(row)
print('row, col =', row, ',' , col)


#Start making the background image
#Gambar = np.zeros(shape=(row, col, 3),dtype=np.int16) #memberi warna latar hitam
#Gambar[:, :, :] = 255 #memberi warna latar putih
latar1 = np.zeros(shape = (row, col, 3), dtype=np.uint8)
latar2 = np.zeros(shape = (row, col, 3), dtype=np.uint8)

#chose 1 : black and blue

latar1[batas1:batas2, :, :] = 0     # background black R=0 G=0 B=0
latar1[batas1:batas2, :, 1] = 255   # background green R=0 G=255 B=0

#chose 2 : gradation image
latar2[:, :, :] = int(0)
delta_row = round(row/256) + 1

for i in range (0, row - delta_row):
    for j in range (0, col):
        latar2[i + delta_row, j, 0] = latar2[i, j, 0] + 1
        latar2[i + delta_row, j, 1] = latar2[i, j, 1] + 1

#saving latar to file
#plt.imsave("latar1.jpg", latar1)
#plt.imsave("latar2.jpg", latar2)

plt.figure(1)
plt.imshow(latar1)
plt.figure(2)
plt.imshow(latar2)
plt.show()