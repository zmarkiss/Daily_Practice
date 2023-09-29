# Python Program to Create a Class which Performs Basic Calculator Operations
class Operation:
    def __init__(self, x, oper, y):
        self.x = x
        self.oper = oper
        self.y = y
        self.msg_0 = 'Enter an equation'
        self.msg_1 = 'Do you even know what numbers are? Stay focused!'
        self.msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
        self.msg_3 = 'Yeah... division by zero. Smart move...'

    def x_y_check(self):
        if self.x.replace(".", "").isnumeric() is not True or self.y.replace(".", "").isnumeric() is not True:
            return True
        else:
            return False

    def oper_check(self):
        if self.oper not in ('+', '-', '/', '*'):
            return True
        else:
            return False

    def control_func(self):
        if Operation.x_y_check(self) is True:
            print(f'{self.msg_1}')
            return True
        elif Operation.oper_check(self) is True:
            print(self.msg_2)
            return True
        elif self.oper == '+':
            print(float(self.x) + float(self.y))
            return False
        elif self.oper == '-':
            print(float(self.x) - float(self.y))
            return False
        elif self.oper == '*':
            print(float(self.x) * float(self.y))
            return False
        elif self.oper == '/' and self.y != '0':
            print(float(self.x) / float(self.y))
            return False
        else:
            print(self.msg_3)
            return True


z = True
while z is True:
    x_, oper_, y_ = input('Enter an equation').split()
    operation = Operation(x=x_, oper=oper_, y=y_)
    z = operation.control_func()
