# ООП инкапсуляция, наследование

class Chelovek:
    def can_walk(self):
        print('я умею ходить')

    def can_breathe(self):
        print('я умею дышать')

    def can_eat(self):
        print('я умею кушать')

    def has_rights(self):
        self._prava = 'имеет свои права'

    def can_poo(self):
        self.__x = 'может пукать'
        self.__y = 'может пукать жидко'

    def __init__(self):
        self.__attr = None

    def __method(self):
        print('я приватныйватный')
    pass


class Architect(Chelovek):
    def can_build(self):
        print('я умею строить')

    def can_build_house(self):
        self._woodenhouse = 'деревянный дом'
        self.__papperhouse = 'бумажный домик'

    def __method(self):
        print('ого как')

    def just(self):
        self.__method()

    def __init__(self):
        super().__init__()
        self.__attr = 'menyau kaliny'
        print(self.__attr)
    pass

asd = Architect()


class Architect_3cat(Architect):
    def help_architect(self):
        print('я помогаю главному архитектору')

    def pappers_bringer(self):
        print('я подношу бумажки главному архитектору')

    def while_work(self):
        self._otlichnorabotaet = 'качественно выполняющий работу сотрудник'
        self.__lazybaby = 'неторопливый сотрудник'

class Doctor(Chelovek):
    def can_heal(self):
        print('я умею лечить')

    def always_at_work(self):
        self._work_quality = 'много работает'
        self.__podcherk = 'неразборчиво пишет'

    def __init__(self):
        super().__init__()
        self.attr = 'chegototam'
    pass

class Okoolist(Doctor):
    def can_heal_eyes(self):
        print('я умею лечить глаза')
    pass

dsa = Okoolist()
setattr(Okoolist, '_vozrast', 34)
sdd = Okoolist()

class Example:
    def __init__(self, a: str):
        print('ya stroka', a)

    @staticmethod
    def get_params():
        print('Переданно 0 параметров')

    @staticmethod
    def get_params(param):
        print('Передан 1 параметр')

class OS:
    def __getattr__(self, item):
        print('getattr')

dd = OS()
dd.__getattr__('strochka')
