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

# for i in range(10):
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
#     print(' ')

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





# for y in range(10):
#     if(y%2 == 0):
#         for x in range(10):
#             if(x%2 == 0):
#                 print("1", end=" ");
#             else:
#                 print("0", end=" ");
#         print("")
#     else:
#         for x in range(10):
#             if(x%2 == 0):
#                 print("0", end=" ");
#             else:
#                 print("1", end=" ");
#         print("")