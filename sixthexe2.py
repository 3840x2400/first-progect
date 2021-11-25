class Road:
    def __init__(self, length, width):
        self._length = length
        self._wigth = wigth

    def get_weidht(self, spec_grav, thick):
        return self._length * self._wigth * spec_grav * thick / 1000

r = Road(5000, 20)
print(r.get_weidht(25, 5))
