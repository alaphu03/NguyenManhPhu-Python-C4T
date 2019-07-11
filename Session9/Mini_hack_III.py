items =[2, 5, 8, 9, 12]
while True:
    i = input("so ban muon tim trong danh sach:")
    if i in items:
        for i in items:
            print("Found, position", item[i])
    else:
        print("Not found in our list") 