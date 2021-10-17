class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("GO!")

    def stop(self):
        print("Stop!")

    def turn(self,direction):
        print(f"Car turned to {direction}")

    def show_speed(self):
        print(f"Current speed is {self.speed}")

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Speed limit violated")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Speed Limit violated")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color,name, True)

town = TownCar(90, "green", "Town")
sport = SportCar(120, "red", "Sport")
work = WorkCar(41, "yellow", "Work")
police = PoliceCar(100, "blue", "Police")

town.show_speed()
town.show_speed()

work.speed = 30
work.show_speed()

police.turn('Left')