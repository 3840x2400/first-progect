def stepen(x, y):
    if x < 0:
        return 'X bolshe 0'
    if y > 0:
        return 'Y menshe 0'
    z = 1
    for i in rande(y *= -1):
        z *= x
    return 1 / z

x = float(input("Please enter a positive number"))
y = float(input("Please enter a negative integer"))
print(stepen(x, y))
