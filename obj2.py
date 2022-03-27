from PIL import Image
im = Image.open('profile.jpg', 'r')
pixel_values = list(im.getdata())

count = 0
for i in range(len(pixel_values)):
    count += 1
    print('SNo. ', count, 'Red ', pixel_values[i][0], 'Green ', pixel_values[i][1], 'Blue ', pixel_values[i][2])


