# ООП инкапсуляция, наследование

slomannij faile
class Chelovek:
    def can_walk(self):
        print('я умею ходить')
    def can_breathe(self):
        print('я умею дышать')
    def can_eat(self):
        print('я умею кушать')
    pass

class Architect(Chelovek):
    def can_build(self):
        print('я умею строить')
    pass

class Architect_3cat(Architect):
    def help_architect(self):
        print('я помогаю главному архитектору')
    def pappers_bringer(self):
        print('я подношу бумажки главному архитектору')

class Doctor(Chelovek):
    def can_heal(self):
        print('я умею лечить')

class Okoolist(Doctor):
    def can_heal_eyes(self):
        print('я умею лечить глаза')
    pass
