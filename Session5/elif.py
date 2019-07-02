# month = int(input("thang trong nam:"))
# if month < 4:
#     print("mua xuan")
# elif month <7:
#     print("mua he")    
# else:
#     if month < 9:
#         print("mua thu")
#     else:
#         print("mua dong")   
for i in range(input('How many random numbers?: ')):
         line = int(random.randint(1, 100))
         afile.write(line)
         print(line)
