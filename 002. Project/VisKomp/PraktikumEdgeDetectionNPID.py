print("\033c")       #To close all
import numpy as np
from matplotlib import pyplot as plt
import time

###################################################################################################
print ("Acquiring user entries.")
###################################################################################################
th = 20                                                       #Threshold of ignoring noises.
th2 = 20      #Threshold for differential values of neighboring pixels, for edge detection.
                               #The more the th2 the sharper the edge line will be resulted.
green_lw = 4                                                       #width of the green line.
print("th, th2, green_lw =", th, th2, green_lw)
print (" ")
#dir = "C://Users//MN//OneDrive - Universitas Pembangunan Jaya//Coding_Python//MK_VisKomp//Gambar_in_out//"
#nama_file_input = "Heksagon_Gradasi"; th2 = 20
dir = "/Users/aditya/git/aditya1-github/VisKomp/Images/NPID/"
nama_file_input = "Car_Gradasi"; th2 = 20
#nama_file_input = "Cat_https_www.wired.com"; th2 = 10
#nama_file_input = path + "ayo_ogunseinde_unsplash_r.jpg"; th2 = 10
#nama_file_input = path + "charlize_theron_r.JPG"; th2 = 10
#nama_file_input = path + "nas_r.JPG"; th2 = 20
#nama_file_input = path + "child_n_laptop_r.jpg"; th2 = 20
###################################################################################################
print ("Reading the input file, acquiring its size and creating array templates for processing.")
###################################################################################################
pic = plt.imread(dir + nama_file_input + ".jpg")
row, col, depth = np.shape(pic)
print("col, row, depth =", row, col, depth)
ori = np.zeros(shape=(row, col, depth), dtype = np.uint8)
buffer = np.zeros(shape=(row, col, depth), dtype = np.uint8)
ori[:, :, :] = pic[:,:,:]
buffer[:, :, :] = pic[:,:,:]
plt.figure('Original Image')
plt.imshow(ori)
plt.ion()
plt.show()
plt.pause(0.01)
print("")
##################################################################################################
print ("Preliminary edge detection (Algorithm #1) is taking place.")
print ("Every pixel that indicates any kind of object edge will be colored blue. Check it out.")
print ("At the same time, we are finding object weight center, x_min, x_max, y_min, and y_max.")
##################################################################################################
y_start = 0; y_end = row
x_start = 0; x_end = col
n = 0                                               #Initiation of the number of edge pixels
yc = y_start                              #Initiation for the y coordinate of weight center
xc = x_start                              #Initiation for the x coordinate of weight center
y_min = y_end                                                      #Initiation for the y_min
y_max = y_start                                                    #Initiation for the y_max
x_min = x_end
x_max = x_start
for i in range (0+1, row-1):                               #+1 is to avoid division by zero.
    for j in range (0+1, col-1):
        cek1, cek2, cek3, cek4, cek5, cek6, cek7, cek8, cek9 = \
        False, False, False, False, False, False, False, False, False           #Initiation

        #A point is checked if it is at the edge of the object by checking its neighbors.
        #Piksel yang dicek berada di tengah.
        #Piksel tetangga berada di atas, di kiri, di bawah dan di kanan piksel yang dicek.
        point_r  = ori[i,j,0];   point_g = ori[i,j,1];    point_b = ori[i,j,2]
        neigh1_r = ori[i-1,j,0]; neigh1_g = ori[i-1,j,1]; neigh1_b = ori[i-1,j,2]  #di atas
        neigh2_r = ori[i,j-1,0]; neigh2_g = ori[i,j-1,1]; neigh2_b = ori[i,j-1,2]  #di kiri
        neigh3_r = ori[i+1,j,0]; neigh3_g = ori[i+1,j,1]; neigh3_b = ori[i+1,j,2]  #di bawah
        neigh4_r = ori[i,j+1,0]; neigh4_g = ori[i,j+1,1]; neigh4_b = ori[i,j+1,2]  #di kanan
        cek_n1r = abs(int(neigh1_r) - int(point_r)) #Delta nilai R antara neigh1 dan piksel yg dicek.
        cek_n2r = abs(int(neigh2_r) - int(point_r)) #Delta nilai R antara neigh2 dan piksel yg dicek.
        cek_n3r = abs(int(neigh3_r) - int(point_r)) #Delta nilai R antara neigh3 dan piksel yg dicek.
        cek_n4r = abs(int(neigh4_r) - int(point_r)) #Delta nilai R antara neigh4 dan piksel yg dicek.

        if cek_n1r > th2 or cek_n2r > th2 or cek_n3r > th2 or cek_n4r > th2:
            #print(i,j, "Edge detected")
            buffer[i,j,:] = 0, 0, 255                #Piksel yang merupakan edge diwarnai biru.
            n = n + 1
            yc = yc + i
            xc = xc + j
            if i < y_min: y_min = i
            if i > y_max: y_max = i
            if j < x_min: x_min = j
            if j > x_max: x_max = j

yc = round (yc/n)                    #yc and xc will be used in the second-stage edge detection.
xc = round (xc/n)
print ("y_min, yc, y_max =", y_min, yc, y_max, ".")
print ("x_min, xc, x_max =", x_min, xc, x_max, ".")
print("")
plt.figure('Preliminary Edge Detection')
plt.imshow(buffer)
plt.ion()
plt.show()
plt.pause(0.01)

#################################################################################################
print ("Final edge detection (Algorithm #2) is taking place.")
print ("Paint the outmost edge pixels in every line green.")
#################################################################################################
print ("Preparing arrays to accomodate edge pixel properties: coordinates and colors.")
print("The edge array has a length and contains index number, y_edge, x_edge, R_edge, G_edge, and B_edge.")
time.sleep(5)
len_edge = max(2*(y_max-y_min), 2*(x_max-x_min)) + 2                       #Length of edge array
indeks_edge = np.zeros(shape = (len_edge), dtype = int)            #Index of every edge's pixels
y_edge = np.zeros(shape = (len_edge), dtype = int)          #List of y coordinate of edge pixels
x_edge = np.zeros(shape = (len_edge), dtype = int)
R_edge = np.zeros(shape = (len_edge), dtype = int)
G_edge = np.zeros(shape = (len_edge), dtype = int)
B_edge = np.zeros(shape = (len_edge), dtype = int)
G_edge[:] = 255                                        #Every edge's pixels will be painted green.

# #CHECK THE CONTENTS OF THE ARRAYS BEFORE EXECUTING THE FINAL EDGE DETECTION
# print ("Contents of edge arrays before executing the final edge detection:")
# for i in range (0, len_edge):
#     print (indeks_edge[i], y_edge[i], x_edge[i], R_edge[i], G_edge[i], B_edge[i])
# print("")

#EXECUTING THE FINAL EDGE DETECTION (ALGORITHM #2)
#FINDING EDGE PIXELS, THAT IS, ONE AT THE RIGHTMOST AND ONE AT THE LEFTMOST (IF OBJECT IS VERTICAL)
#FINDING EDGE PIXELS, THAT IS, ONE AT THE TOP AND ONE AT THE BOTTOM (IF OBJECT IS HORIZONTAL)
print("If any object resides too close to image margin, edge detection can cause 'Index is out of bound'.")
print("Setting the y_min, y_max, x_min and x_max so that they don't get out of bound.")
margin = int(green_lw)
if y_min < 0 + margin: y_min = 0 + margin
if y_max > row - margin: y_max = row - margin
if x_min < 0 + margin: x_min = 0 + margin
if x_max > col - margin: x_max = col - margin

if  (x_max - x_min >= y_max - y_min) or (x_max - x_min < y_max - y_min):
    counter = 0
    for i in range (y_min, y_max+1):       #Scanning half right of the object (downward, clockwise)
        print("")
        #print("Counter =", counter)
        indeks_edge[counter] = counter
        y_edge[counter] = i
        n = 0                                                      #Initiation for the next i loop
        x = 0                                                               #Initiation for next i
        for j in range (xc, x_max+1):
            #If pixel(i,j) is red, then check if the next two pixels are not red.
            cek1 = bool(buffer[i,j,0]   == 255 and buffer[i,j,1]   == 0 and buffer[i,j,2]   == 0)
            cek2 = bool(buffer[i,j+1,0] == 255 and buffer[i,j+1,1] == 0 and buffer[i,j+1,2] == 0)
            cek3 = bool(buffer[i,j+2,0] == 255 and buffer[i,j+2,1] == 0 and buffer[i,j+2,2] == 0)
            if cek1 == True and cek2 == False and cek3 == False:
                #This is temporary rightmost edge and will be overwritten by the next rightmost one.
                print('Finding a rigtmost edge in a row:', i, ",", j)
                x_edge[counter] = j
        counter = counter + 1

    print(""); print("It's now halfway."); print("")

    for i in range (y_max, y_min-1, -1):     #Scanning half left of the object (upward, clockwise)
        print("")
        #print(counter)
        indeks_edge[counter] = counter
        y_edge[counter] = i
        n = 0                                                      #Initiation for the next i loop
        x = 0                                                               #Initiation for next i
        for j in range(xc, x_min-1, -1):
            # If pixel(i,j) is red and next two pixels are not red, then the pixel(i,j) is the edge.
            cek1 = bool(buffer[i, j, 0] == 255   and buffer[i, j, 1]   == 0 and buffer[i, j, 2] == 0)
            cek2 = bool(buffer[i, j-1, 0] == 255 and buffer[i, j-1, 1] == 0 and buffer[i, j-1, 2] == 0)
            cek3 = bool(buffer[i, j-2, 0] == 255 and buffer[i, j-2, 1] == 0 and buffer[i, j-2, 2] == 0)
            if cek1 == True and cek2 == False and cek3 == False:
                #This is temporary lefttmost edge and will be overwritten by the next leftmost one.
                print('Finding a leftmost edge in a row:', i, ",", j)
                x_edge[counter] = j
        counter = counter + 1

# #CHECK THE CONTENTS OF THE ARRAYS AFTER EXECUTION OF FINAL EDGE DETECTION (ALGORITHM #2)
# print ("Contents of edge arrays after executing the final edge detection:")
# for i in range (0, len_edge):
#     print (indeks_edge[i], y_edge[i], x_edge[i], R_edge[i], G_edge[i], B_edge[i])
# print("")

#######################################################################################################
print("Now applying the edge arrays to color the outermost edge pixels in picture green. Check it out.")
#######################################################################################################
for i in range (0, len_edge):
    buffer[y_edge[i], x_edge[i], 0:3]   = R_edge[i], G_edge[i], B_edge[i]
    buffer[y_edge[i], x_edge[i]-1, 0:3] = R_edge[i], G_edge[i], B_edge[i]
    buffer[y_edge[i], x_edge[i]+1, 0:3] = R_edge[i], G_edge[i], B_edge[i]
    buffer[y_edge[i], x_edge[i]-2, 0:3] = R_edge[i], G_edge[i], B_edge[i]
    buffer[y_edge[i], x_edge[i]+2, 0:3] = R_edge[i], G_edge[i], B_edge[i]
plt.imsave(dir + nama_file_input + "_NPID.jpg", buffer )

plt.figure('Final Edge Detection')
plt.imshow(buffer)
plt.ion()
plt.show()
plt.pause(200)