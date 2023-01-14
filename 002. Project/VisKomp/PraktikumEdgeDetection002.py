import numpy as np
import matplotlib.pyplot as plt

#Setting Initialization
# penyimpanan file
filePath = "/Users/aditya/git/aditya1-github/VisKomp/images/NPID/"       # direktori file
fileExt = ".jpg"                                                    # ekstension file
fileName = filePath + "Background_604x914" + fileExt                        # nama file beserta ekstensinya

# ukuran canvas
row = int(604)                                                      # jumlah baris pixel
col = int(914)                                                      # jumlah kolom pixel
channel = int(3)                                                    #
jump_row = 4                                                        # jumlah baris akan diwarnai saat satu kali proses pewarnaan
background = np.zeros(shape=(row, col, channel), dtype=np.uint8)    # membuat latar canva pixel
print('initialization : \n row, col =', row, ',', col)              # cetak u/ log

# mewarnai
# background[int(row/2):int(row), :, :] = 0     # background black R=0 G=0 B=0
# background[int(row/2):int(row), :, 1] = 255   # background green R=0 G=255 B=0

#proses mewarnai terhadap setiap pixel
for i in range(1, row - jump_row):                                  # loop sebanyak jml row - jump_row
    for j in range(1, col):                                         # loop sebanyak jml column
        #background[i + jump_row, j, 0] = background[i, j, 0] + 1    # mewarnai dengan RGB setiap pixel
        background[i + jump_row, j, 1] = background[i, j, 1] + 1    # mewarnai dengan RGB setiap pixel
    print('row, col =', i, ',', j)                                  # cetak u/ log

# mensimpan hasil warna pada pixel menjadi image
plt.imsave(fileName, background)

#proses memanggil
plt.figure(1)                                                       # membuat jendela untuk canva
plt.imshow(background)                                              # menampilkan background ke jendela canva
plt.show()                                                          # menampilkan jendela canva