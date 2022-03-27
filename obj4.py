from PIL import Image
import numpy as np
img = Image.open(r"walpaper.jpg")
img_arry = np.array(img)
I_max = 255
img_arry = I_max - img_arry
inverted_img = Image.fromarray(img_arry)
inverted_img.save(r"inverted.jpg")
