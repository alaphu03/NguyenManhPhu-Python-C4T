while True:
    txt = input("Nhap ten cua ban :")
    if txt.isalpha():
        txt2 = input("Nhap ho cua ban:")
        while True:
            if txt2.isalpha():
                print("ho va ten cua ban la:", txt2, txt)
                break
            else:
                print("ho khong duoc phep co so")
    else:
        print("ten khong duoc phep co so")