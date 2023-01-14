print("\033c")       #To close all
import numpy as np
from matplotlib import pyplot as plt

#USER ENTRIES
dir = "/Users/aditya/git/aditya1-github/VisKomp/Images/NPID/"
# nama_file_input_1 = "Heksagon_Gradasi"
# nama_file_input_2 = "Heksagon_Gradasi_NPID"
nama_file_input_1 = "Car_Gradasi"
nama_file_input_2 = "Car_Gradasi_NPID"
margin = 0.05 #lebar atau margin atas-bawah-kiri-kanan untuk di crop

#PROGRAM
pic1 = plt.imread(dir + nama_file_input_1 + ".jpg")
pic2 = plt.imread(dir + nama_file_input_2 + ".jpg")
row, col, depth = np.shape(pic2)
print("col, row, depth =", row, col, depth)

#Finding y_min
stop = 0
for i in range (0, row-1, 1):
    if stop ==1: break
    for j in range (0, col-1, 1):
        if pic2[i, j, 2] > 150:
            y_min = i
            stop = 1
print(y_min)

#Finding y_max
stop = 0
for i in range (row-1, 0, -1):
    if stop ==1: break
    for j in range (col-1, 0, -1):
        if pic2[i, j, 2] > 250:
            y_max = i
            stop = 1
print(y_max)

#Finding x_min
stop = 0
for j in range (0, col-1, 1):
    if stop == 1: break
    for i in range (0, row-1, 1):
        if pic2[i, j, 2] > 250:
            x_min = j
            stop = 1
print(x_min)

#Finding x_max
stop = 0
for j in range (col-1, 0, -1):
    if stop == 1: break
    for i in range (row-1, 0, -1):
        if pic2[i, j, 2] > 250:
            x_max = j
            stop = 1
print(x_max)

#ADDING MARGINS
dy = y_max - y_min                                            #Object's height
dx = x_max - x_min                                            #Object's width
y_min = y_min - round(margin*dy); y_max = y_max + round(margin*dy)  #Add top and bottom margin
x_min = x_min - round(margin*dx); x_max = x_max + round(margin*dx)  #Add left and right margin
print (y_min, y_max)
print (x_min, x_max)
dy = y_max - y_min                                        #Height of the cropped picture
dx = x_max - x_min                                        #Width of the cropped picture

crop = np.zeros(shape=(dy, dx, depth), dtype = np.uint8)
crop[0:dy, 0:dx, 0:3] = pic1[y_min:dy+y_min, x_min:dx+x_min, 0:3]

plt.imsave(dir + nama_file_input_1 + "_cropped.jpg", crop)

plt.figure("Original Picture")
plt.imshow(pic1)
plt.ion

plt.figure("Picture After Edge Detection using NPID")
plt.imshow(pic2)
plt.ion

plt.figure("Cropped Picture")
plt.imshow(crop)
plt.ion
plt.show()