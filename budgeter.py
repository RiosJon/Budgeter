import csv

DATA_FILE = 'data.csv'
FIELDNAMES = ['date', 'transaction', 'amount', 'note']

def load_data():
  list_of_data = []
  with open('data.csv', 'r', newline='') as data_file:
    reader = csv.DictReader(data_file)
    for row in reader:
      list_of_data.append(row)
  return list_of_data

def view_previous_entries(entries):
  #The goal is to show all of the accounting entries in a human readable
  for entry in entries:
    print(f' The date was {entry["date"]} and this was a {entry["transaction"]}  for the amount of ${entry["amount"]} used for {entry["note"]}')
  
def display_profit_loss(entries):
  expenses = 0
  income = 0
  for row in entries:
    if row["transaction"] == "Income":
      income += int(row["amount"])
    elif row['transaction'] == "Expense":
      expenses += int(row['amount'])
  print(expenses, ':Theses are your expenses')
  print(income, ": This is your income")
  print(income - expenses, "This is your profit")

  
def add_new_entry(entries):
  
  date = input("Date of Transaction (YYYY-MM-DD):")
  question = input("Was this income (Y/N): ")
  transaction = ""
  if question.upper() == "Y":
    transaction = "Income"
  else:
    transaction = "Expenses"
  
  amount = int(input("Amount: "))
  
  description = input("Describe the transaction: ")
  
  new_dict = {'date': date, 'transaction': transaction , 'amount': amount, 'note': description}
  entries.append(new_dict)

  with open("data.csv", 'a', newline='') as data_file:
    writer = csv.DictWriter(data_file, FIELDNAMES)
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