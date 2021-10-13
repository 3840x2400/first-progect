with open('ver_test.txt') as file:
    filin = file.readlines()
    for num, line in enumerate(filin):
        str_count += 1
        worco = len(line.split())
        print(f'#{num + 1} - {worco} words')
