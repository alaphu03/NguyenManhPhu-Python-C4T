items =[]
while True:
    n = input("C:Creat R:Read U:Update D:Delete Q:Quit   Chon mot thao tac:")
    if n == "C":
        items.append(input("Nhap thu ban yeu thich: "))
    elif n == "R":
        if len(items) == 0:
            print("Danh sach rong")
        else:
            print("Danh sach thu yeu thich cua ban:")
            for i in items:
                print(i) 
    elif n == "U":
        if len(items) == 0:
            print("Danh sach rong")
        else:
            location = int(input("Nhap vi tri thu ban muon thay doi: "))
            items[location] = input("Thu ban muon thay doi: ")
    elif n == "D":
        if len(items) == 0:
            print("Danh sach rong")
        else:
            location = int(input("Nhap vi tri thu ban muon xoa: "))
            items.pop(location)
    else:
        break
    print()