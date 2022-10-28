
def buat_garis(Gambar, y1, x1, y2, x2,hd, hw, pr, pb, pg, lr, lg, lb):

    #Draw the first point.
    for i in range(x1-hd, x1+hd):
        for j in range(y1-hd, y1+hd):
            if ((i-x1) ** 2 + (j-y1) ** 2 ) < hd**2:
                Gambar[j,i,0] = pr
                Gambar[j,i,1] = pg
                Gambar[j,i,2] = pb

    #Draw the second point.
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if ((i - x2) ** 2 + (j - y2)**2) < hd ** 2:
                Gambar[j, i, 0] = pr
                Gambar[j, i, 1] = pg
                Gambar[j, i, 2] = pb

    dy = y2 - y1
    dx = x2 - x1

    # Draw the line. Untuk garis yang  horisontal
    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i - x1) + y1) #mencari y dengan persamaan garis
            x = i
            y = j
            print('x, y = ', x, ', ', y)
            for i in range(x - hw, x + hw): #membuat titik dan mewarnai dengan warna merah diantara koordinat x dan y
                for j in range(y-hw, y+hw):
                    if ((i-x)**2 + (j-y)**2) < hw**2:
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
 #
 #Drwa the line, untuk garis yang vertikal
    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1) #mencari y dengan persamaan garis
            x = i
            y = j
            print('x, y =', x, ', ', y)
            for i in range(x - hw, x + hw): #membuat titik dan mewarnai dengan warna merah diantara koordinat x dan y
                for j in range(y - hw, y + hw):
                    if((i-x)**2 + (j-y) **2 < hw **2 ):
                        Gambar[j, i, 0] = lr
                        Gambar[j, i, 1] = lg
                        Gambar[j, i, 2] = lb
    return Gambar
