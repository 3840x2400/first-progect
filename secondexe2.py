num_input = input('list: ')

num_list = num_input.split()

num_scor = len(num_list)
x = 0
if num_scor > 1:
        num_list[x], num_list[x+1] = num_list[x+1], num_list[x]
        x += 2
print(num_list)