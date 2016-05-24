class Class(object):

color1 = Color()
color2 = Color()
color3 = Color()

color1.r = 0
color1.g = 255
color1.b = 255

color2.r = 255
color2.g = 255
color2.b = 255

color3.r = 128
color3.g = 128
color3.b = 128

colors = [color1,color2,color3]
print type(colors)
for color in colors:
    print colors
