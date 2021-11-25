
month = input('Number of month: ')
a, b, c, d = 'winter', 'spring', 'summer', 'autumn'
month_dic = {'1': a, '2' : a, '3': b, '4' : b, '5' : b, '6' : c, '7' : c, '8' : c, '9' : d, '10' : d, '11' : d, '12' : a}
print(month_dic[month])
season_list = [a, a, b, b, b, c, c, c, d, d, d, a]
print(season_list[int(month) - 1])
