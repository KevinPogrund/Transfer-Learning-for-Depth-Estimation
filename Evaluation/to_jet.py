# Edited code originally by Samantha Ball

import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg

folder = "/home/minibeast/Kevin/bts/pytorch/result_bts_eigen_v2_pytorch_densenet161/raw"  # folder name containing 16-bit depth maps
folder = "./"
for filename in sorted(os.listdir(folder)):
    print(filename)
    if not filename.endswith((".png", "jpg")):  # to ensure continuous processing
        continue
    img = mpimg.imread(os.path.join(folder, filename))
    plt.imshow(img, cmap="jet")  # plot as jet colour map
    plt.axis('off')  # remove axes
    plt.savefig("jet/bts_" + filename.split(".")[0] + ".png",
                bbox_inches='tight', pad_inches=0)  # save without surrounding whitespace
