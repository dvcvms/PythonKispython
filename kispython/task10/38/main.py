class MealyError(BaseException):
    def __init__(self, m) -> None:
        self.m = m
        super().__init__(m)


class mealy:
    def __init__(self):
        self.state = "A"
        self.state_map = {
            "A": {
                "chip": ("B", 0),
                "skew": ("D", 1),
            },
            "B": {
                "skew": ("C", 2),
                "chip": ("D", 4),
                "carve": ("E", 3)
            },
            "C": {
                "carve": ("D", 5)
            },
            "D": {
                "skew": ("E", 6)
            },
            "E": {
                "chip": ("F", 7),
            },
            "F": {
                "carve": ("D", 8),
            }
        }

    def chip(self):
        if "chip" in self.state_map[self.state]:
            tmp = self.state_map[self.state]["chip"]
            self.state = tmp[0]
            return tmp[1]
        raise MealyError("chip")

    def skew(self):
        if "skew" in self.state_map[self.state]:
            tmp = self.state_map[self.state]["skew"]
            self.state = tmp[0]
            return tmp[1]
        raise MealyError("skew")

    def carve(self):
        if "carve" in self.state_map[self.state]:
            tmp = self.state_map[self.state]["carve"]
            self.state = tmp[0]
            return tmp[1]
        raise MealyError("carve")



def test():
    o = main()
    assert o.spin() == 0
    assert o.punch() == 1
    assert o.spin() == 4
    assert o.spin() == 5
    assert o.punch() == 7
    assert o.spin() == 0
    assert o.spin() == 3
    assert o.spin() == 6
    assert o.punch() == 9
    o = main()
    assert o.spin() == 0
    assert o.stand() == 2
    o = main()
    assert o.spin() == 0
    assert o.spin() == 3
    assert o.stand() == 8
    raises(lambda: o.stand(), MealyError)
    raises(lambda: o.punch(), MealyError)
    raises(lambda: o.spin(), MealyError)

def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None

def main():
    return mealy