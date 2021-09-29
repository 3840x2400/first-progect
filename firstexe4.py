

a = int(input('Input integer number: '))
m = a % 10 # получаем последнюю цифру числа
a = a // 10 # получаем остальную часть числа
while a > 0 :
    if a % 10 > m :
        m = a % 10
    a = a // 10
print(m)