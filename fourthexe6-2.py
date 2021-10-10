#from itertools import cycle, count

#n = 100
#my_list = [x for x in range(5)]
#counter = count()
#cycler = cycle(my_list)
#print([next(counter) for x in range(n)])
#print([next(cycler) for x in range(n)])

def gen_factorial(number):
    curr = 1
    for x in range(1, number + 1):
        curr *= x
        yield curr

n = 12
for index, elem in enumerate(gen_factorial(n)):
    print(f"#{index + 1} {elem}")
