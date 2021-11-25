from time import sleep


class TrafficLight:
    color = ("red", 'yellow', 'green')
    delay = (7, 2, 15)

    def __init__(self):
        self.__color = 'green'

    def running(self):
        while True:
            for i in self.color:
                self.__color = i
                print(self.__color)
                sleep(self.delay[self.color.index(self.__color)])


traffic_light = TrafficLight()
traffic_light.running()
