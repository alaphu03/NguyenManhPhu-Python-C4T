# from turtle import*
# colors=["red", "blue", "brown", "yellow", "grey"]
# for i, k in enumerate(colors):
#     color(k)
#     for h in range(i+3):
#         forward(100)
#         left(360/ (i+3) )
# mainloop()



from turtle import*
colors=["red", "blue", "brown", "yellow", "grey"]
for k in colors:
    color(k)
    fillcolor(k)
    begin_fill()
    forward(100)
    right(90)
    forward(200)
    right(90)
    forward(100)
    right(90)
    forward(200)
    right(90)
    forward(100)       
    end_fill()
mainloop()
