my_list =[8, 11, 6, 4, 3, 3, 2, 2, 1, 1]
rating = int(input('rating number: '))
inserted = False
for index, elem in enumerate (my_list):
    if rating > elem:
        my_list.insert(index, rating)
        inserted = True
        break

if not inserted:
    my_list.append(rating)

print(my_list)
