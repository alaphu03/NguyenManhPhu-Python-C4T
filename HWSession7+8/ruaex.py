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
for k in enumerate(colors):
    color(k)
    fillcolor(k)
    begin_fill()
    for i in range(5):
        if i%2 ==0:
            forward(100)
            right(90)
        else:
            forward(50)
            right(90)
    end_fill()
mainloop()
