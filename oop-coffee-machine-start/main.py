from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

choice = Menu()
machine = CoffeeMaker()
banker = MoneyMachine()



condition=True
while condition==True:
    order = input(f"what would you like? [{choice.get_items()}]: ")
    if order=="off":
        condition=False
    elif order=="report":
        print(machine.report(), banker.report())
    else:
        drink=choice.find_drink(order)
        resources = machine.is_resource_sufficient(drink)
        if resources == True and banker.make_payment(drink.cost) == True:
                machine.make_coffee(drink)













