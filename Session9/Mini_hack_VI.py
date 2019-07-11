dis = ["ST", "BD", "BTL", "CG", "DD", "HBT"]
population = [150.300, 247.100, 333.300, 266.800, 420.900, 318.000]
s = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
max_p= population.index(max(population)) 
min_p= population.index(min(population))
print("Quan co dan so dong nhat:",dis[max_p])
print("Quan co dan so it nhat:",dis[min_p])
dens=[]
for i in range(len(population)):
    dens.append( population[i] / s[i] )
print(dens, sep =',')
adens = round(sum(dens)/(len(dens)+1))
print("Mat do dan cu trung binh:",adens)