import random
value = random.randint(1, 101)
if value < 30:
    print('Rainy')
elif value < 60:
    print('Cloudy')
else :
    print('Sunny')