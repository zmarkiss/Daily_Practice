#  Methods and attributes demonstration using input()
#  __init__ & custom method


class User:
    def __init__(self, name, surname, age, country):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country

    # define the necessary method here
    def user_information(self):
        return "{} {} is {} years old and lives in {}.".format(self.name, self.surname, self.age, self.country)


user = User(name=input(), surname=input(), age=int(input()), country=input())
print(user.user_information())
