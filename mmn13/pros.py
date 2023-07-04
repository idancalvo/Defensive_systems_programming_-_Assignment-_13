import sys


class User:
    def __init__(self, name, profession):
        assert type(name) == str and type(profession) == str
        self.__name = name
        self.__profession = profession


class Engineers(User):
    pass


class Technician(User):
    pass


class Barbers(User):
    pass


class Politician(User):
    pass


class Eng_electrical(Engineers):
    pass


class Eng_computer(Engineers):
    pass

class Eng_mechanical(Engineers):
    pass


def class_values (num_of_values):
    values = {}
    for i in range(num_of_values):
        values[input(f"val name {i + 1}?")] = None
    return values

def class_methods (new_class, num_of_methods):
    for i in range(num_of_methods):
        method = input(f"method name {i + 1}?")
        setattr(new_class, method, "your code...")

def create_new_class():
    class_name = input("name of the class?")
    bases_name = input("name of the father?")

    try:
        bases_name = (getattr(sys.modules[__name__], bases_name,),)
    except:
        bases_name = ()

    try:
        num_of_values = int(input("How many variables in class?"))
    except:
        num_of_values = 0

    values_dirct = class_values(num_of_values)

    new_class = type(class_name, bases_name, values_dirct)
    setattr(new_class, "__init__", "your code...")

    try:
        num_of_methods = int(input("How many methods in class?"))
    except:
        num_of_methods = 0

    class_methods(new_class, num_of_methods)
    return new_class

def main():
    temp_=create_new_class()
    print (f"\nname: {temp_.__name__}\nbase: {temp_.__base__.__name__}\ndict:{temp_.__dict__}")


if __name__ == "__main__":
    main()
