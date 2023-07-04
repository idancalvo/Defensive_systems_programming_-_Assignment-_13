class AppleBasket:

    def __init__(self, colo, quantity):
        assert type(colo)==str and type(quantity) == int
        self.__apple_colo = colo
        self.__apple_quantity = quantity

    def increase(self):
        self.__apple_quantity += 1

    def __str__(self):
        return f"A basket of {self.__apple_quantity} {str(self.__apple_colo)} apples"


if __name__ == "__main__":
    print(AppleBasket('red', 4))
    print(AppleBasket('blue', 50))
