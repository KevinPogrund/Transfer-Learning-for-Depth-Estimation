#Edited code originally by Samantha Ball

import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg

folder = "/media/kevin/KP" #folder name containing 16-bit depth maps

for filename in os.listdir(folder):
    print(filename)
    if not filename.endswith((".png", "jpg")): #to ensure continuous processing
        continue
    img = mpimg.imread(os.path.join(folder, filename))
    plt.imshow(img, cmap="jet") #plot as jet colour map

    plt.axis('off') #remove axes
    plt.savefig(filename.split(".")[0] + "_jet.png", bbox_inches='tight') #save without surrounding whitespace