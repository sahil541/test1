import graphics
import sys

def Flip(image_filename):
    img_src = graphics.Image(graphics.Point(0, 0), image_filename)
    img_dst = img_src.clone()
    X, Y = img_src.getWidth(), img_src.getHeight()
    for x in range(X):
        for y in range(Y):
            r, g, b = img_src.getPixel(x, y)
            color = graphics.color_rgb(r, g, b)
            img_dst.setPixel(X-x-1, y, color)

    return img_dst

if __name__ == '__main__':
    input = sys.argv[1] or 'my_image.ppm'
    output = 'mirror-%s' % input
    img = Flip (input)
    img.save(output)