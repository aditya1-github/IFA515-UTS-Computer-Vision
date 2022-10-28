# Membuat perulangan sampai 1 juta kali
#
#i = 1
#while i <= 1000000:
#    print("Loop ke ", i)
#    i = i + 1

# Melakukan perulangan menggunakan keyword for sampai 1 juta kali
for i in range(0, 1000000+1):
    print(i)

# Melakukan perulangan menggunakan keyword for sampai 1 juta kali dan mencetak nilainya setiap kelipatan 1000
for i in range(0, 1000000+1):
    if i%1000 == 0:
        print(i)

# Melakukan perulangan sampai 1 juta kali dan mencetak setiap kelipatan 1000
#i = 1
#while i <= 1000000:
#    if i % 1000 == 0:
#        print(i)
#    i = i + 1