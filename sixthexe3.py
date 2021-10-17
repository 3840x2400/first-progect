class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return "{0} {1}".format(self.name, self.surname)


    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

employee =Position("Alex", "Broun", "Hoochi_Choochi", 40000, 5000)
print(employee.name)
print(employee.surname)
print(employee._income)
print(employee.get_full_name())
print(employee.get_total_income())
