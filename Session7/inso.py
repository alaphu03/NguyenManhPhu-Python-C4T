# a = range(3, 13)
# print(*a)




# while True:
#     n = input("Enter a natural number?")
#     if n.isdigit():
#         while True:
#             if int(n) > 0:
#                 f = range(int(n)+1)          
#                 print("day so lien tiep tu 0 den so ban vua nhap la:", *f)
#                 break
#             else:
#                 print("nhap so tu nhien")
#     else :
#         print("not a natural number")

# while True:
#     n = input("Enter an odd number?")
#     if n.isdigit() and int(n) > 0 and int(n) % 2 == 1 :
#         f = range(int(n)+1)          
#         print("day so lien tiep tu 0 den so ban vua nhap la:")
#         print(0, f, 2)
#         break
#     else :
#         print("Enter an odd number")
f = range(12)
print(*f, 2)
        


