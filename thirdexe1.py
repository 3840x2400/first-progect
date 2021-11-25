
def a_delit_b(a, b):
    if b == 0:
        return 'Na nol delit nelzja'
    else:
        return a / b

a = float(input('a: '))
b = float(input('b: '))
print(a_delit_b(a, b))

