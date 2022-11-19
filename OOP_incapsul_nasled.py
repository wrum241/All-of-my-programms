# ООП инкапсуляция, наследование

class Chelovek:
    def can_walk(self):
        print('я умею ходить')
    def can_breathe(self):
        print('я умею дышать')
    def can_eat(self):
        print('я умею кушать')
    def has_rights(self):
        self._rights = 'имеет свои права'
    def can_poo(self):
        self.__x = 'может пукать'
        self.__y = 'может пукать жидко'
    pass

class Architect(Chelovek):
    def can_build(self):
        print('я умею строить')
    def can_build_house(self):
        self._woodenhouse = 'деревянный дом'
        self.__papperhouse = 'бумажный домик'
    pass

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
    pass

class Okoolist(Doctor):
    def can_heal_eyes(self):
        print('я умею лечить глаза')
    pass

