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

for x in range(1, 11):
    # SAVE THE IMAGE BACK TO THE PATH
    imsave(path + file + "_" + str(x) + ".jpg", pic)