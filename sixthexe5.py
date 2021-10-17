class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Star drawing")

class Pen(Stationery):
    def draw(self):
        print(f"Start draing with pen {self.title}")

class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with handle {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Start drawing with handle {self.title}")

pen = Pen("A")
pencil = Pencil("B")
handle = Handle("C")
for s in (pen, pencil, handle):
    s.draw()
