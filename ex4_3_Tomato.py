#Task 3

#1. Создайте класс Tomato

class Tomato:

# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора

    states = {1: "small", 2: "average", 3: "big"}

# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states

    def __init__(self, index):
        self._index = index
        self._state = 0

# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания

    def grow(self):
        if self._state < 2:
            self._state += 1
        else:
            self._state += 0

# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)

    def is_ripe(self):
        if self._state == 2:
            return True
        return False

# 1. Создайте класс TomatoBush
class TomatoBush:
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
    def __init__(self, amount):
        self.tomatoes = [Tomato(index) for index in range(amount)]

# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания

    def grow_all(self):
        for item in self.tomatoes:
            item.grow()

# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми

    def all_are_ripe(self):
        return all(item.is_ripe() for item in self.tomatoes)

# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая

    def give_away_all(self):
        self.tomatoes.clear()

# 1. Создайте класс Gardener

class Gardener:
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым

    def work(self):
        print("In job")
        self._plant.grow_all()

# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Сбор")
        else:
            print("созревает")

# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.

    @staticmethod
    def knowledge_base():
        print("Documents")


Gardener.knowledge_base()
bush = TomatoBush(6155)
gardener = Gardener("Stas", bush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()