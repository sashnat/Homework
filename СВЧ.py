import sys


class Model:
    def __init__(self, t_max=35, w_max=100): #res = None):
        self.t_max = t_max
        self.w_max = w_max


class Start(Model):
    def __init__(self, t, w): #res = None):
        self.t = t
        self.w = w
        super().__init__()


class Result(Start):
    def result(self):
        a = int(self.t) * int(self.w)
        if 0 < a <= int(self.t_max) * int(self.w_max):
            print("ваше блюдо готово!!!")
        else:
            print("ошибочный ввод данных")


class Switch_off:
    def __init__(self, c=1):   # если нужно инициировать значение "c" при вызове класса
        self.c = c

    def act(self):
        if self.c == 1: # or self.c == True:
            print('отмена')
            sys.exit()
        else:
            print("прерывания готовки не было")


m = Result(input("input t - Натуральное число"), input("input w - Натуральное число"))
c = Switch_off(0)
c.act()
m.result()


c = Switch_off(1)
c.act()
