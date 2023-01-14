import numpy as np
import matplotlib.pyplot as plt

# terima inputan
th = 300                                                            # threshold warna putih

#Setting Initialization
# penyimpanan file
filePath = "/Users/aditya/git/aditya1-github/VisKomp/images/NPID/"       # direktori file
objBackground = plt.imread(filePath + "Background_604x914.jpg")             # file background
obj = plt.imread(filePath + "Car.jpg")                          # file object gambar

# ukuran canvas
row = int(604)                                                      # jumlah baris pixel
col = int(914)                                                      # jumlah kolom pixel
channel = int(3)                                                    # jumlah warna dalam pixel, krn menggunakan RGB maka ada 3 warna Red Green Blue
background = np.zeros(shape=(row, col, channel), dtype=np.uint8)    # membuat latar canva pixel
print('initialization : \n row, col =', row, ',', col)              # cetak u/ log

# mewarnai canvas dari object background
background[:, :, :] = objBackground[:, :, :]

#proses mewarnai terhadap setiap pixel
for i in range(1, row):                                             # loop sebanyak jml row - jump_row
    for j in range(1, col):                                         # loop sebanyak jml column

        r = obj[i, j, 0]                                            # mengambil nilai ke-1 warna merah pada pixel
        g = obj[i, j, 1]                                            # mengambil nilai ke-2 warna hijau pada pixel
        b = obj[i, j, 2]                                            # mengambil nilai ke-3 warna merah pada pixel

        if float(r) + float(g) + float(b) < (255*3) - th:
            background[i, j, :] = obj[i, j, :]                   # mewarnai dengan RGB setiap pixel

# mensimpan hasil warna pada pixel menjadi image
plt.imsave(filePath + "Car_Gradasi.jpg", background)

#proses memanggil
plt.figure(1)                                                       # membuat jendela untuk canva
plt.imshow(background)                                              # menampilkan background ke jendela canva
plt.show()                                                          # menampilkan jendela canva