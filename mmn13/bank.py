class BankAccount:

    def __init__(self, name, amt):
        assert type(name) == str and type(amt) == int
        self.__name = name
        self.__amt = amt

    def __str__(self):
        return f"Your account, {self.__name}, has {str(self.__amt)} dollars."


if __name__ == "__main__":
    t1 = BankAccount('Bob', 100)
    print(t1)
