def int_func(txt):
    word = txt[0].upper() + txt[1:].lower()
    return word



string = input("Enter words separated by a space: ")
for word in string.split(' '):
    print(f'{int_func(word)} ', end=' ')
    