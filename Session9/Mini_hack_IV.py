input_string = input("Enter a list of numbers, separated by space ")
items  = input_string.split()
if len(items) <=5 :
    print("Enter 5 or more numbers")
else:
    break
while True:
    for i in range(len(items)):
        if i % 2 ==0:
            print(items[i])
            break
        else:
            break