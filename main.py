from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

is_on = False

while not is_on:
  choice = input(f'would you like to order {menu.get_items()} ')
  if choice == 'off':
    is_on == True
  if choice == 'report':
    coffee_machine.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    if coffee_machine.is_resource_sufficient(drink):
      payment_accepted = money_machine.make_payment(drink.cost)
      if payment_accepted:
        coffee_machine.make_coffee(drink)
      

