

DATA_FILE = 'data.csv'
FIELDNAMES = ['date', 'transaction', 'amount', 'note']

def load_data():
  pass

def view_previous_entries(entries):
  pass

def display_profit_loss(entries):
  pass

def add_new_entry(entries):
  pass

# ===========================================
# =    Do Not Modify Anything Below Here    =
# ===========================================

def get_menu_choice():
  choice = None
  
  while choice == None:
    try:
      choice = int(input('> '))
    except ValueError as err:
      print('That was not a valid entry, please try again!')
      continue

    if choice < 1 or choice > 4:
      print('That was not a valid choice, please try again!')
      choice = None

  return choice

def print_menu():
  print('\nWhat would you like to do?\n')
  print('1) View previous entries')
  print('2) Display the current profit/loss')
  print('3) Add a new entry')
  print('4) Exit\n')

def main():
  print('====================')
  print('Welcome to Budgeter!')
  print('====================')

  entries = load_data()

  while True:
    print_menu()
    menu_choice = get_menu_choice()

    if menu_choice == 1:
      view_previous_entries(entries)
    elif menu_choice == 2:
      display_profit_loss(entries)
    elif menu_choice == 3:
      add_new_entry(entries)
    elif menu_choice == 4:
      break

main()