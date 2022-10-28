from matplotlib import pyplot as plt
from skimage.io import imread, imsave
import warnings
warnings.filterwarnings("ignore")

#USER ENTRY
path = "/Users/aditya/git/aditya1-github/VisKomp/images/"
file = "punthuk_setumbu"

#READ A FILE (IMAGE) FROM A DIRECTORY
pic = imread(path + file + ".jpg")

# SHOW THE IMAGE
plt.figure(1)
plt.imshow(pic)
plt.show()

# SAVE THE IMAGE BACK TO THE PATH
i = 1
while i < 10:
    i = i + 1
    imsave(path + file + "_" + str(i) + ".jpg", pic)

# or you can use like this
# for x in range(1, 11):
#     # SAVE THE IMAGE BACK TO THE PATH
#     imsave(path + file + "_" + str(x) + ".jpg", pic)


# proses melatih nn sampai mampu mengingat sekian ribu kondisi dengan akurat disebut dengan proses training / Learning
# yang terjadi pada proses training adalah komputer sedang mencari persamaan yang tepat
# proses training memakan waktu yang lama, sesudah training selesai terbentuk maka persamaan tersebut dipakai untuk prediksi dan prosesnya sangat cepat