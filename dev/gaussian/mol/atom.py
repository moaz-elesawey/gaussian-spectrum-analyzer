from numpy import array


class Atom:
    def __init__(self, index, atomic_number, v, x, y, z) -> None:
        self.index = int(index)
        self.atomic_number = int(atomic_number)
        self.v = v
        self.x = x
        self.y = y
        self.z = z
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
        
    def get_object(self):
        return {'index': self.index, "x": self.x, "y": self.y, "z": self.z, "atomicNumber": self.atomic_number}

    @property
    def pos(self):
        return self.x, self.y, self.z

    def __repr__(self) -> str:
        return f'Atom({self.index}, {self.atomic_number})'
