import sys

if len(sys.argv) < 5:
    print(f"Все данные (выработка, ставка, премия, черный заработок)! ")
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = float(sys.argv[4])
    result = a * b + c + d
    print(result)
    