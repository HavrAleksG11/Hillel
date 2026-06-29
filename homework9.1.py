class Romb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError()
            object.__setattr__(self, name, value)

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError()

            object.__setattr__(self, "angle_a", value)
            object.__setattr__(self, "angle_b", 180 - value)

        elif name == "angle_b":
            raise AttributeError()

        else:
            object.__setattr__(self, name, value)

    def info(self):
        return f"Ромб: сторона a = {self.side_a}, кут a = {self.angle_a}, кут b = {self.angle_b}"


romb1 = Romb(10, 60)
print(romb1.info())

romb1.angle_a = 120
print(romb1.info())
