class House:
    def __init__(self, name, new_floor, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
        self.new_floor = new_floor

    def go_to(self, new_floor, number_of_floor):
        if new_floor >= 1 and new_floor <= self.number_of_floor:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа нет')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return (f'Название:{self.name}, кол-во этажей: {self.number_of_floor}')

    def __eq__(self, other):
        if self.number_of_floor == other.number_of_floor:
            return self.number_of_floor == other.number_of_floor
        else:
            return False

    def __lt__(self, other):
        if self.number_of_floor < other.number_of_floor:
            return self.number_of_floor < other.number_of_floor
        else:
            return False

    def __le__(self, other):
        if self.number_of_floor <= other.number_of_floor:
            return self.number_of_floor <= other.number_of_floor
        else:
            return False

    def __gt__(self, other):
        if self.number_of_floor > other.number_of_floor:
            return self.number_of_floor > other.number_of_floor
        else:
            return False

    def __ge__(self, other):
        if self.number_of_floor >= other.number_of_floor:
            return self.number_of_floor >= other.number_of_floor
        else:
            return False

    def __ne__(self, other):
        if self.number_of_floor!= other.number_of_floor:
            return True
        else:
            return False

    def __add__(self, value):
        self.number_of_floor += value
        return self.number_of_floor

    def __radd__(self, value):
        self.number_of_floor += value
        return self.number_of_floor

    def __iadd__(self, value):
        self.number_of_floor += value
        return self.number_of_floor + value



amurskie = House('amurskie', 10, 30)
#amurskie.go_to(0, 30)
zory = House('zory', 20, 30)
#zory.go_to(20, 30)
print(len(amurskie))
print(str(amurskie))
print(len(zory))
print(str(zory))
print(amurskie == zory)
print(amurskie < zory)
print(amurskie <= zory)
print(amurskie > zory)
print(amurskie >= zory)
print(amurskie!= zory)
print(amurskie + 5)
iadd = zory + 5
print(zory)
