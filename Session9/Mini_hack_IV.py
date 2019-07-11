while True: 
    input_string = input("Enter a list of numbers, separated by space ")
    items  = input_string.split()
    if len(items) <= 4 :
        print("Enter 5 or more numbers")
    else:
        break
print("All even numbers entered:")
for item in items:
    if int(item) % 2 ==0:
        print(item, sep =',')
            
