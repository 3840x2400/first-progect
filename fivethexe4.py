nums = {
    'One':"Один",
    'Two' : "Два",
    'Three' : "Три",
    'Four' : "Четыре",
}


with open(ver_test.txt) as file, open('new_file.txt', 'w') as new_file:
    file_line = file.readlines()
    for line in file_line:
        data = line.split()
        rus_num = nums.get(data[0])
        new_file.write(f'{line.replace(data[0], rus_num)}')
        