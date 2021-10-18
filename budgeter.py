import csv

DATA_FILE = 'data.csv'
FIELDNAMES = ['date', 'transaction', 'amount', 'note']

def load_data():
  list_of_data = []
  with open('data.csv', 'r', newline='') as data_file:
    reader = csv.DictReader(data_file)
    for row in reader:
      row = list_of_data
  return list_of_data

def view_previous_entries(entries):
  #The goal is to show all of the accounting entries in a human readable 
  view_previous_entries = DATA_FILE
  return entries
  

def display_profit_loss(entries):
  expenses = 0
  income = 0
  for row in entries:
    if row["transaction"] == "Income":
      income += row["amount"]
    elif row['transaction'] == "Expenses":
      expenses += row['amount']
  print(expenses, ':Theses are your expenses')
  print(income, ": This is your income")
  print(income - expenses, "This is your profit")

  
def add_new_entry(entries):
  with open("data.csv", 'w', newline='') as data_file:
    writer = csv.DictWriter(data_file, FIELDNAMES)
  
  date = input("Date of Transaction (YYYY-MM-DD):")
  question = input("Was this income (Y/N): ")
  
  if question.upper == "Y":
    transaction = "Income"
  elif question.upper == "N":
    transaction = "Expenses"
  
  amount = int(input("Amount: "))
  
  description = input("Describe the transaction: ")
  
  new_dict = {'date': date, 'transaction': question , 'amount': amount, 'note': description}
  writer.writerow(new_dict)


  #dictwriter add this to csv file

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