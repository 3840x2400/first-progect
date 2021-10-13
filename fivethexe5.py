import random

with open('test_f.txt', 'w') as file:
    for _ in range(30):
        file.write(f'{random.randint(0, 10)}')

with open('text_num.txt') as file:
    num_str = file.read().split()
    sum = 0
    for num in num_str:
        sum += int(num)

print(sum)

