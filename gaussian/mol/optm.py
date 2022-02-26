from numpy import array

class OptimizationStep:
    def __init__(self, index, x, y, z, atomic_number) -> None:
        self.index = index
        self.x = x
        self.y = y
        self.z = z
        self.atomic_number = atomic_number
        self.color = self.get_color()

    def get_color(self):
        Z = int(self.atomic_number)
        color = [125, 125, 125, 1]

        if Z == 8:
            color = [1, 0, 0, 1]
        elif Z == 6:
            color = [.2, .2, .2, 1]
        elif Z == 1:
            color = [1, 1, 1, 1]
        elif Z == 7:
            color = [0, 0, 1, 1]
        elif Z == 16:
            color = [1, 1, 0, 1]

        return array(color)

    @property
    def pos(self):
        return self.x, self.y, self.z

    def __repr__(self) -> str:
        return f'OptmStep({self.index}, {self.x}, {self.y}, {self.z})'

    def __str__(self) -> str:
        return f'{self.index}: '
