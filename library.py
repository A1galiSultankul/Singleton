from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def cost(self):
        pass

class Coffee(Beverage):
    def cost(self):
        return 5

class BeverageDecorator(Beverage):
    def __init__(self, beverage):
        self._beverage = beverage

    def cost(self):
        return self._beverage.cost()

class MilkDecorator(BeverageDecorator):
    def cost(self):
        return super().cost() + 2

class SugarDecorator(BeverageDecorator):
    def cost(self):
        return super().cost() + 1
class CreamDecorator(BeverageDecorator):
    def cost(self):
        return super().cost() + 3
    
def display_menu():
    print("Beverage Menu:")
    print("1. Coffee with Milk")
    print("2. Coffee with Sugar")
    print("3. Coffee with Cream")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

if __name__ == "__main__":
    my_beverage = Coffee()

    while True:
        choice = display_menu()

        if choice == '1':
            my_beverage = MilkDecorator(my_beverage)
            print("Adфded milk to the beverage.")
        elif choice == '2':
            my_beverage = SugarDecorator(my_beverage)
            print("Added sugar to the beverage.")
        elif choice == '3':
            my_beverage = CreamDecorator(my_beverage)
            print("Added sugar to the beverage.")
        elif choice == '4':
            print("Thank you for your order!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

    print("Total cost of your beverage: $", my_beverage.cost())
