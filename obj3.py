from PIL import Image, ImageEnhance

img = Image.open("walpaper.jpg")
img_data = img.getdata()

lst=[]
for i in img_data:

    lst.append(i[0]*0.299+i[1]*0.587+i[2]*0.114)

new_img = Image.new("L", img.size)
new_img.putdata(lst)

new_img.save("bw.jpg")