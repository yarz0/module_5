class House:
    def __init__(self, street, new_floor, number_of_floor):
        self.street = street
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
        return (f'Название:{self.street}, кол-во этажей: {self.number_of_floor}')


amurskie = House('amurskie', 10, 30)
amurskie.go_to(0, 30)
zory = House('zory', 20, 30)
zory.go_to(20, 30)
print(len(amurskie))
print(str(amurskie))
print(len(zory))
print(str(zory))
