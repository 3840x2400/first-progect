
earning = int(input('Выручка: '))
costs = int(input('Издержки: '))

if costs > earning:
    print('Убыток')
elif earning > costs:
    print('Прибыль')
    print (earning - costs)
    profitability = round((earning - costs) / earning, 2)
    print(f'Рентабельность: {profitability}')
    empl_count = int(input('Количество штатных сотрудников: '))
    profit_per_empl = round((earning - costs) / empl_count, 2)
    print(f'Прибыль фирмы в рассчете на одного сотрудника: {profit_per_empl}')
elif earning == costs:
    print('Финансовый результат = 0')