from turtle import *
color("blue")
speed(-1)
right(90)
for i in range(1,110,2):
    for n in range(4):
        forward(i)
        left(90)
    left(10)
mainloop()