with open('wer_test_2.txt') as file:
    filin = file.readlines()
    employees = {}
    sum_salary = 0
    for line in file_lines:
        emp_info = line.split()
        employees.update({emp_info[0]:float(emp_info[1])})
        sum_salary += float(emp_info[1])
average_sal = sum_salary / len(employees)
print(f'Average = {average_sal}')

for k, v in employees.items():
    if v < 20000:
        print(f'{k}: {v}')
