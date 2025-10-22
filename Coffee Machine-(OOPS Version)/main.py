from importlib.resources import is_resource
from tkinter.font import names

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu =Menu()
is_on=True



while is_on:
    options = menu.get_items()
    user_option= input(f"what would you like? ({options}):")
    if user_option=="off":
        is_on=False
    elif user_option=="report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink= menu.find_drink(user_option)
        if coffee_maker.is_resource_sufficient(drink) and  money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    
            
      
    
    
    








