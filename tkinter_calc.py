from tkinter import *
from tkinter import messagebox

mb = messagebox

class MathButton:
    def __init__(self, sign, action):
        self.but = Button(text=sign, width=10, command=getattr(self, action))
        self.but.pack()
    user_history = []

    def show_history(self, window):
        lab_label = Label(window, width=15, text='History:')
        lab_label.pack()
        for elem in self.user_history:
            lab_result = Label(window, width=15, text=f'{elem}')
            lab_result.pack()

    @staticmethod
    def test():
        try:
            n1 = float(ent_n1.get())
            n2 = float(ent_n2.get())
            return n1, n2
        except ValueError:
            lab_result['text'] = 'Error'
            return False

    def summa(self):
        nums = MathButton.test()
        if nums:
            lab_result['text'] = nums[0] + nums[1]
            self.user_history.append(f'{nums[0]} + {nums[1]} = {lab_result["text"]}')
        print(self.user_history)

    def diff(self):
        nums = MathButton.test()
        if nums:
            lab_result['text'] = nums[0] - nums[1]
            self.user_history.append(f'{nums[0]} - {nums[1]} = {lab_result["text"]}')
        print(self.user_history)

    def product(self):
        nums = MathButton.test()
        if nums:
            lab_result['text'] = nums[0] * nums[1]
            self.user_history.append(f'{nums[0]} * {nums[1]} = {lab_result["text"]}')
        print(self.user_history)

    def div(self):
        nums = MathButton.test()
        if nums:
            try:
                n = nums[0] / nums[1]
                lab_result['text'] = round(n, 2)
            except ZeroDivisionError:
                lab_result['text'] = 'ZeroDivisionError'
            self.user_history.append(f'{nums[0]} / {nums[1]} = {lab_result["text"]}')
        print(self.user_history)



    # def get_user_input(self):
    #     try:
    #         return int(input('Введите значение '))
    #     except:
    #         print('Вы не ввели число, попробуйте заново')
    #         return int(input('Введите значение '))


root = Tk()
root.title("Calculator")

ent_n1 = Entry(width=10)
ent_n1.pack()
ent_n2 = Entry(width=10)
ent_n2.pack()

but_summa = MathButton('Сложение', 'summa')
but_diff = MathButton('Разность', 'diff')
but_prod = MathButton('Умножение', 'product')
but_div = MathButton('Деление', 'div')

def back_button(this_window):
    if messagebox.askokcancel("Возврат в меню", "Хотите вернуться в главное меню?"):
        this_window.destroy()
def start_window():
    new_window_1 = Toplevel()
    new_window_1.title("История")
    new_window_1.resizable(False, False)
    new_window_1.wm_attributes("-topmost", 1)
    canvas_1 = Canvas(new_window_1, width=200, height=200, highlightthickness=0)
    Label(new_window_1, text="История вычислений:").pack()
    but_summa.show_history(new_window_1)
    # Label(new_window_1, text='MathButton.user_history')

    Button(new_window_1, text="Назад", command=lambda this_window=new_window_1: back_button(this_window)).pack()
    canvas_1.pack()
b1 = Button(text='История', command=start_window)
b1.pack()

lab_label = Label(width=15, text='Результат:')
lab_label.pack()

lab_result = Label(width=15)
lab_result.pack()

def exit():
    choice = mb.askyesno("Выход из приложения", "Вы уверены что хотите выйти?")
    if choice:
        root.destroy()
Button(root, width=20, text="Выход", relief=GROOVE, bd=5, command=exit).pack()

root.mainloop()