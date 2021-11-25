def my_func(num_1, num_2, num_3):
    sum_nums = num_1 + num_2 + num_3
    return sum_nums - min(num_1, num_2, num_3)


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
i = my_func(a, b, c)