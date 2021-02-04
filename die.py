from random import randint

class Die:
    """
    Класс, представляющий один кубик
    """
    def __init__(self, num_sides=6):
        """
        6 гранный кубик
        """
        self.num_sides = num_sides

    def roll(self):
        """
        Возвращает числа от 1 до числа граней
        """
        return randint(1, self.num_sides)
