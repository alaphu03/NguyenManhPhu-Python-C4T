d =["ST", "BD", "BTL", "CG", "DD", "HBT"]
p= [150.300,247.100,333.300,266.800,420.900,318.000]
s =[117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
max_p= p.index(max(p)) 
min_p= p.index(min(p))
print("Quan co dan so dong nhat:",d[max_p])
print("Quan co dan so it nhat:",d[min_p])