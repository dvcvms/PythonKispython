class MealyError(BaseException):
    def __init__(self, m) -> None:
        self.m = m
        super().__init__(m)


class mealy:
    def __init__(self):
        self.state = "A"
        self.state_map = {
            "A": {
                "spin": ("B", 0)
            },
            "B": {
                "punch": ("C", 1),
                "spin": ("E", 3),
                "stand": ("G", 2)
            },
            "C": {
                "spin": ("D", 4)
            },
            "D": {
                "spin": ("E", 5)
            },
            "E": {
                "spin": ("F", 6),
                "stand": ("G", 8),
                "punch": ("A", 7),
            },
            "F": {
                "speed": ("G", 9),
            }
        }

    def spin(self):
        if "spin" in self.state_map[self.state]:
            tmp = self.state_map[self.state]["spin"]
            self.state = tmp[0]
            return tmp[1]
        raise MealyError("spin")

    def punch(self):
        if "punch" in self.state_map[self.state]:
            tmp = self.state_map[self.state]["punch"]
            self.state = tmp[0]
            return tmp[1]
        raise MealyError("punch")

    def stand(self):
        if "stand" in self.state_map[self.state]:
            tmp = self.state_map[self.state]["stand"]
            self.state = tmp[0]
            return tmp[1]
        raise MealyError("stand")



def test():
    a = main()
    for i in "ABCDEFG": # поменять кол-во букв
        a.state = i
        try:
            a.spin()
        except MealyError:
            pass
        a.state = i
        try:
            a.punch()
        except MealyError:
            pass
        a.state = i
        try:
            a.placed()
        except MealyError:
            pass

def main():
    return mealy