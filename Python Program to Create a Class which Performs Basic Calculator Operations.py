# Python Program to Create a Class which Performs Basic Calculator Operations
class Hcalc:
    memory = 0.0
    counter = 1
    msg_0 = 'Enter an equation'
    msg_1 = 'Do you even know what numbers are? Stay focused!'
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3 = 'Yeah... division by zero. Smart move...'
    msg_4 = 'Do you want to store the result? (y / n):'
    msg_5 = 'Do you want to continue calculations? (y / n):'
    operations = {"+": lambda x, y: x + y,
                  "-": lambda x, y: x - y,
                  "*": lambda x, y: x * y,
                  "/": lambda x, y: x / y
                  }

    def __init__(self, x, operator, y):
        self.x = x
        self.operator = operator
        self.y = y

    def x_y_check(self):
        if Hcalc.counter == 1:
            if self.operator == "/" and (self.y == 0 or self.y.isalpha()):
                print(Hcalc.msg_3)
                return True
            elif self.x.replace(".", "").isnumeric() is not True or self.y.replace(".", "").isnumeric() is not True:
                print(f'{Hcalc.msg_1}')
                return True
            else:
                Hcalc.counter += 1
                return False
        if Hcalc.counter > 1:
            if self.x.replace(".", "").isnumeric() is not True:
                self.x = self.memory
            if self.y.replace(".", "").isnumeric() is not True:
                self.y = self.memory

    def operator_check(self):
        if self.operator not in ('+', '-', '/', '*'):
            return True
        else:
            return False

    def store_continue(self):
        store = input(Hcalc.msg_4)
        if store == 'y':
            Hcalc.memory = Hcalc.operations[self.operator](self.x, self.y)
            cont = input(Hcalc.msg_5)
            if cont == 'y':
                return True
            else:
                return False
        if store == 'n':
            cont = input(Hcalc.msg_5)
            if cont == 'y':
                return True
            else:
                return False

    def control_func(self):
        if Hcalc.x_y_check(self) is True:
            return True

        if Hcalc.operator_check(self) is True:
            print(Hcalc.msg_2)
            return True

        self.x = float(self.x)
        self.y = float(self.y)

        if self.operator in ["+", "-", "*", "/"]:
            if self.operator == "/" and self.y == 0:
                print(Hcalc.msg_3)
                return True
            else:
                print(Hcalc.operations[self.operator](self.x, self.y))

        if Hcalc.store_continue(self) is True:
            return True


z = True
while z is True:
    x_, operator_, y_ = input('Enter an equation').split()
    calc = Hcalc(x=x_, operator=operator_, y=y_)
    z = calc.control_func()
