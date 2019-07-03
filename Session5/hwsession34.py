#          turtle exercise)

# from turtle import *
# color("red")
# right(30)
# forward(100)
# left(60)
# forward(100)
# left(120)
# forward(100)
# left(60)
# forward(100)
# for i in range(3):
#     right(150)
#     forward(100)
#     left(60)
#     forward(100)
#     left(120)
#     forward(100)
#     left(60)
#     forward(100)

# mainloop()



#        serious exercise)

#        ex1) Tinh chi so BMI


# height = int(input("height(cm):"))
# weight = int(input("weight(kg):"))
# h = height / 100
# BMI = weight / (h * h)
# if BMI < 16 :
#     print("Now,your BMI is ", BMI, "you are Severely underweight")
# elif BMI < 18.5 :
#     print("Now,your BMI is ", BMI, "you are Underweigh")   
# elif BMI < 25 :
#     print("Now,your BMI is ", BMI, "you are normal")
# elif BMI < 30 :
#     print("Now,your BMI is ", BMI, "you are overweight")
# else :
#     print("Now,your BMI is ", BMI, "you are obese")

#        ex2) tinh luy thua

# a = 1 
# n = int(input("so nguoi dung nhap:"))
# for i in range(1, n+1):
#     a = a * i
# print("luy thua so nguoi dung nhap:", a)

#        ex3) 
#       a)
#     i)  

# r1 = range(20)
# print (*r1)

#     ii)

# n = int(input("so nguoi dung nhap:"))
# r2 = range(n)
# print("day so tu 0 den so lien truoc nguoi dung nhap", *r2)

#      b)
#     i)

# for i in range(1000):
#     if i % 2 == 0:
#         print (0, end = ' ')  
#     else:
#         print (1, end = ' ')

#      ii)

# n = int(input("so cap so 0 va 1 lien tiep nguoi dung muon nhap:"))
# for i in range(2*n):
#     if i % 2 == 0:
#         print (0, end = ' ')  
#     else:
#         print (1, end = ' ')

#        c)
#      i)


# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end = ' ')
#     print('')

#      ii)

# n = int(input("so nguoi dung muon:"))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(i * j, end = ' ')
#     print('')



#       d)
#      i)

# for i in range(1, 11):
#     for j in range(1, 11):
#         print( (i + j + 1) % 2  , end = ' ')
#     print('')


#       ii)

# n = int(input("so cap so 0 va 1 nguoi dung muon print:"))
# for i in range(1, n):
#     for j in range(1, n):
#         print( (i + j + 1) % 2  , end = ' ')
#     print('')