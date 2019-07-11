# colors = ['red', 'blue', 'brown', 'yellow', 'grey']
# from turtle import *
# for i in range(5):
#     color(colors[i])
#     for k in range(5):
#         for j in range(k):
#             forward(100)
#             left(360/j)
# mainloop()

from turtle import*
colors=["red", "blue", "brown", "yellow", "grey"]
for i,k in enumerate(colors):
    color(k)
    for i in range(i+3):
        forward(100)
        left(360/(i+3))
mainloop()