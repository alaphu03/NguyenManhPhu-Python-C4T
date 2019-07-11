# items = ['blue', 'red', 'teal', 'green']
# print("our color list:", *items, sep=',')
# items.append(input("Enter a new color: "))
# print("our new color list:", *items, sep=',')


# items = ['blue', 'red', 'teal', 'green']
# n = input("enter a positon:")
# print("Color at your position:", items[int(n)])

items = ['blue', 'red', 'teal', 'green']
for i,item in enumerate(items):
    print(i+1,'.', item)
    item_to_delete = input("item to delete")
if item_to_delete.isalpha:
    items.remove(item_to_delete)
    for i,item in enumerate(items):
        print(i+1,'.', item)
else:
    items.pop(int(item_to_delete) -1)
    for i,item in enumerate(items):
        print(i+1,'.', item)









