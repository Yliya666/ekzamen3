#1
def card(a):
    print(('*'*(len(a[:4])))+a[-4:])
a=int(input('Введите номер карты:'))
a=str(a)
card(a)


#2 задача
def Palindrome(a):
    if a[::-1] == a[::]:
        return 'Палиндром'
    else:
        return "Не палиндром"
b = str(input('Введите слово: '))
print(Palindrome(b))

#3
class Tomato:

    states = {0: 'ничего', 1: 'цветочки', 2: 'зеленый помидор', 3: 'красный помидор'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False


    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num-1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])


    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник работает...')
        self._plant.grow_all()
        print('САдовник закончил')

    def harvest(self):
        print('Садовник собирает урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор урожая закончен')
        else:
            print('Слишком рано! Ваше растение зеленое и незрелое.')

    @staticmethod
    def knowledge_base():
        print('''В идеале время сбора урожая помидоров должно наступить.
когда плод зрелый зеленый и
затем позволили созреть лозе.
Это предотвращает расслоение и синяки.
и позволяет в определенной мере контролировать процесс созревания.''')


if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()

