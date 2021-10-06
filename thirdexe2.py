def user_info(name, surname, year, city, email, phone):
    print(f'{name} {surname} {year} {city} {email} {phone}')

n = input("Name: ")
s = input("Surname: ")
y = input("Year: ")
c = input("City: ")
e = input("E-mail: ")
p = input("Phone: ")

user_info(name=n, surname=s, year=y, city=c, email=e, phone=p)


