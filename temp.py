from random import randint
from tkinter import *

red = randint(0, 255)
green = randint(0, 255)
blue = randint(0, 255)


red = hex(red)[2:]
green = hex(green)[2:]
blue = hex(blue)[2:]

def getcolor(r, g, b):
    red, green, blue =str(hex(r)[2:]), str(hex(g)[2:]), str(hex(b)[2:])
    if len(red) == 1:
        red = '0' + red

    if len(green) == 1:
        green = '0' + green

    if len(blue) == 1:
        blue = '0' + blue

    return f'#{red}{green}{blue}'


root = Tk()
pallete = [[None] * 16 for _ in range(16)]
print(pallete)
for row in range(0, 256, 17):
    for column in range(0, 256, 17):
        pallete[row // 17][column // 17] = Button(text=f"{row // 17}{column // 17}", bg=getcolor(row, 0 , column))
        pallete[row // 17][column // 17].grid(row=row//17, column=column//17)

root.mainloop()

# pallete = [[btn00, btn01, btn02],
#            [btn10, btn11, btn12],
#
# ]

