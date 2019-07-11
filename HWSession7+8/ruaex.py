colors = ['red', 'blue', 'brown', 'yellow', 'grey']
from turtle import *
for i in range(5):
    color(colors[i])
    n=int(input("So canh: "))
    for i in range(5):
        forward(100)
        left(360/i)


mainloop()