class NormalCar:    def drive(self):        print('[NormalCar] drive() called!')    def back(self):        print('[NormalCar] back() called!')class TurboCar(NormalCar):    def turbo(self):        print('[TurboCar] turbo() called!')myTurbo = TurboCar()myTurbo.turbo()myTurbo.drive()myTurbo.back()print('---------------------------')class CalculatorSuper:    def add(self, n1, n2):        return n1 + n2;    def sub(self, n1, n2):        return n1 - n2;class CalculatorChild(CalculatorSuper):    def mul(self, n1, n2):        return n1 * n2;    def div(self, n1, n2):        return n1 / n2;myCal = CalculatorChild()print(f'cal.add(10, 20): {myCal.add(10, 20)}')print(f'cal.sub(10, 20): {myCal.sub(10, 20)}')print(f'cal.mul(10, 20): {myCal.mul(10, 20)}')print(f'cal.div(10, 20): {myCal.div(10, 20)}')