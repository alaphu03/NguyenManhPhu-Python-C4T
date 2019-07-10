x=0
txt = input("so canh nguoi cua da giac nguoi dung muon ve:")
while True:
    x +=1
    if txt.isdigit() and x < int(txt)+1 :
        from turtle import *
        left(360/ x)
        forward(100)
        mainloop()
        break        
    else :
        print("nhap so")

