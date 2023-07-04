class MealyError(Exception):
    pass


class Mealy():

    def __init__(self):
        self.pos = 'A'
        self.dict = {'A': {'b': ['D', 2], 'spin': ['B', 0], 'color': ['F', 1]},
                     'B': {'b': ['B', 4], 'spin': ['C', 3]},
                     'C': {'color': ['D', 5]},
                     'D': {'b': ['E', 6]},
                     'E': {'b': ['B', 8], 'spin': ['F', 7]},
                     'F': {}}

    def build(self):
        if('b' in self.dict[self.pos].keys()):
            data = self.dict[self.pos]['b']
            self.pos = data[0]
            return data[1]
        else:
            raise MealyError('build')

    def spin(self):
        if('spin' in self.dict[self.pos].keys()):
            data = self.dict[self.pos]['spin']
            self.pos = data[0]
            return data[1]
        else:
            raise MealyError('spin')

    def color(self):
        if('color' in self.dict[self.pos].keys()):
            data = self.dict[self.pos]['color']
            self.pos = data[0]
            return data[1]
        else:
            raise MealyError('color')


def main():
    return Mealy()


def test():
    o = main()
    assert o.build() == 2
    assert o.build() == 6
    try:
        a = o.color()
    except Exception as e:
        assert type(e) == MealyError
    assert o.spin() == 7
    try:
        a = o.build()
    except Exception as e:
        assert type(e) == MealyError
    try:
        a = o.spin()
    except Exception as e:
        assert type(e) == MealyError
    try:
        a = o.color()
    except Exception as e:
        assert type(e) == MealyError
    o = main()
    assert o.spin() == 0
    assert o.build() == 4
    assert o.spin() == 3
    assert o.color() == 5
    assert o.build() == 6
    assert o.build() == 8
    o = main()
    assert o.color() == 1
