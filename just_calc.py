class Math:
    a = int
    b = int
    user_history = []
    def show_history_by_index(self):
        index = self.get_user_input()
        for i in range(len(self.user_history)):
            if i == index:
                print(self.user_history[index])
                break
        else:
             print("Братюня такого порядкового номера небыло(")

    def show_history(self):
        print(self.user_history)

    def sum(self):
        self.init_values()
        c = self.a + self.b
        self.user_history.append(f'{self.a} + {self.b} = {c}')
        print(self.a, "+", self.b, "=", c)
        return c

    def minus(self):
        self.init_values()
        c = self.a - self.b
        self.user_history.append(f'{self.a} - {self.b} = {c}')
        print(self.a, "-", self.b, "=", c)
        return c

    def mult(self):
        self.init_values()
        c = self.a * self.b
        self.user_history.append(f'{self.a} * {self.b} = {c}')
        print(self.a, "*", self.b, "=", c)
        return c

    def div(self):
        self.init_values()
        if self.a == 0 or self.b == 0:
            print("На ноль делить нельзя")
        else:
            c = self.a / self.b
            self.user_history.append(f'{self.a} / {self.b} = {c}')
            print(self.a, "/", self.b, "=", c)
            return c


    def init_values(self):
        self.a = self.get_user_input()
        self.b = self.get_user_input()

    def get_user_input(self):
        try:
            return int(input('Введите значение '))
        except:
            print('Вы не ввели число, попробуйте заново')
            return int(input('Введите значение '))

class Menu:
    menu = {}
    def __init__(self, menu):
        self.menu = menu

    def show_menu(self):
        for i in self.menu:
            print(f'{i}: {self.menu.get(i)}')

    def get_user_answer(self):
        x = int(input('Выберите раздел [Введите номер раздела]: '))
        print('Вами выбран раздел', x)
        return x

class Interface:
    operation_count = int
    user_history = []
    math = Math()
    main_menu = Menu({
            1: "Сумма",
            2: "Разность",
            3: "Умножение",
            4: "Деление",
            5: "История",
            6: "Выход"
        })
    secondary_menu = Menu({
            1: "Заново",
            2: "Назад в меню",
            3: "Выход"
        })
    history_menu = Menu({
        1: "Показать всю историю",
        2: "Поиск по порядковому номеру вычесления"
    })

    def command_exec_menu(self, x):
        if x == 1:
            self.math.sum()
        elif x == 2:
            self.math.minus()
        elif x == 3:
            self.math.mult()
        elif x == 4:
            self.math.div()
        elif x == 5:
            self.history_menu.show_menu()
            a = self.history_menu.get_user_answer()
            if a == 1:
                self.math.show_history()
            elif a == 2:
                self.math.show_history_by_index()

    def return_result(self):
        print(self.math.user_history)

    def start_prog(self):
        a = 7
        while True:
            if a == 7:
                self.main_menu.show_menu()
                a = self.main_menu.get_user_answer()
                if a == 6:
                    break
                self.command_exec_menu(a)
            self.secondary_menu.show_menu()
            x = self.secondary_menu.get_user_answer()
            if x == 1:
                self.command_exec_menu(a)
            elif x == 2:
                a = 7
                continue
            elif x == 3:
                break

asd = Interface()
asd.start_prog()


