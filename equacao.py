import math

class Equação:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__delta = ''
        self.__x1 = ''
        self.__x2 = ''
        self.__px = []
        self.__py = []
        
    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_px(self):
        return self.__px

    def get_py(self):
        return self.__py

    def calc_delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c
        
    def calc_x1(self):
        return (- self.__b + math.sqrt(self.calc_delta()))/ (2 * self.__a)

    def calc_x2(self):
        return (- self.__b - math.sqrt(self.calc_delta()))/ (2 * self.__a)

    def calc_p(self):
        d = self.calc_x1() - self.calc_x2()
        xmin = self.calc_x1() - d
        xmax = self.calc_x2() + d
        e = (xmax-xmin)/100
        x = xmin
        while x<= (xmax + e):
            self.__px.append(x)
            self.__py.append(self.__a * x ** 2 + self.__b * x + self.__c)
            x += e
