# Assignment: File I/O and CSV Files

In this assignment, you'll practice these concepts we've covered in class:

* Using modules
* Reading documentation
* File I/O
   * CSV Files
* Reinforcing fundamentals:
   * Functions
   * Lists and iteration
   * Using dictionaries

In addition to those concepts, this assignment will require you to use all of the knowledge you've gained so far in the course, including data types, loops, f-strings, etc, etc.

This assignment can be challenging! Feel free to collaborate with other students on this assignment, but you should still hand in your own assignment.

## Deliverables

1. Make a copy of the assignment repo with **Use this template**
1. Open your Terminal and navigate to your work folder
1. **Clone** your copy of the assignment repo onto your computer
1. Do your work inside your repo
1. **Commit** any new files that you create as well as any other changes
1. **Push** the changes to Github when you are done

## Submitting

To submit this assignment:

1. Go to the **assignment's main repo** (not your fork)
1. Click the **Issues** tab
1. Click the **New Issue** button
1. In the Title field, fill in your name
1. In the comment field, paste the URL to your assignment repo
1. Click **Submit new issue** and you're done!

---

# Exercise 1: Budgeter

In this exercise, you will use the fundamental Python skills we've learned to create an interactive budgeting application.

Your cousin's lemonade stand wants to enter the 21st century and track their budget using a Python program that stores data in a `.csv` file. "No problem," you say, "I'm halfway finished with the Python course at GA, I can handle this!"

## Expected Output

```
====================
Welcome to Budgeter!
====================

What would you like to do?

1) View previous entries
2) Display the current profit/loss
3) Add a new entry
4) Exit

> 5
That was not a valid choice, please try again!
> asdfasdf
That was not a valid entry, please try again!
> 1
2021-01-01	Expense	$50	Lemons
2021-01-02	Income	$100	Sales

What would you like to do?

1) View previous entries
2) Display the current profit/loss
3) Add a new entry
4) Exit

> 2
The total income is $100
The total expenses are $50
The current profit is $50

What would you like to do?

1) View previous entries
2) Display the current profit/loss
3) Add a new entry
4) Exit

> 3
Date of transaction (YYYY-MM-DD): 2021-01-03
Was this Income (Y/N): Y
Amount: 25
Describe the transaction: Sales

What would you like to do?

1) View previous entries
2) Display the current profit/loss
3) Add a new entry
4) Exit

> 3
Date of transaction (YYYY-MM-DD): 2021-01-04
Was this Income (Y/N): N
Amount: 50
Describe the transaction: Lemons

What would you like to do?

1) View previous entries
2) Display the current profit/loss
3) Add a new entry
4) Exit

> 1
2021-01-01	Expense		$50	Lemons
2021-01-02	Income		$100	Sales
2021-01-03	Income		$25	Sales
2021-01-04	Expense		$50	Lemons

What would you like to do?

1) View previous entries
2) Display the current profit/loss
3) Add a new entry
4) Exit

> 2
The total income is $125
The total expenses are $100
The current profit is $25

What would you like to do?

1) View previous entries
2) Display the current profit/loss
3) Add a new entry
4) Exit

> 4
```

<details>
<summary>Starter Code, if you need to start over</summary>

```python


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
```
</details>

## User Stories

Here are all the things that your program must do:

1. When I start up the program, I am given the following options:
   1. View all previous entries
   1. Display the current profit or loss
   1. Add a new entry to the budget tracker
   1. Quit the budget tracker
1. If I choose to view all previous entries:
   1. The program prints the details of all previous entries in a human readable format
1. If I choose to display the current profit or loss:
   1. The program reports the business's total income
   1. The program reports the business's total expenses
   1. The program calculates the business's profit/loss by subtracting total expenses from total income, and reports the profit or loss, as the case may be
1. If I choose to add a new entry, I am asked to provide:
   1. The date of the transaction in "YYYY-MM-DD" string format
   1. Whether the budget item is Income or Expense
   1. The total amount of the budget item
      * Let's keep things simple and assume everything is in dollars, no cents
      * The amount must be greater than 0
   1. A note describing the budget item
1. After I finish one of the above tasks, the program allows me to do another task
1. If I choose to quit from the budget tracker, the program will exit

## Hints

### General Hints

* The first task is to *read* and *understand* the starter code - That is key to being able to solve this whole problem
* Ask yourself:
   * What is the point of the capitalized global variables at the top of the file?
   * What is the job of the `main()` function?
      * Do you understand *every single line* of the `main()` function?
   * What does `get_menu_choice()` and `print_menu()` do?
   * You **should not** modify any of these functions!
* Your job is to fill out the rest of the 4 functions: `load_data()`, `view_previous_entries()`, `display_profit_loss()`, and `add_new_entry()`
   * What is the job of each of these unimplemented functions?
   * What are the inputs (arguments/parameters) to each function? Why?
   * What should be the output (return value) of each of functions? Why?
   * Planning this out will give you a roadmap on how to implement the functions
* You should tackle each function in the following order, from easiest to hardest:
   * `load_data()`
   * `view_previous_entries()`
   * `display_profit_loss()`
   * `add_new_entry()`
* Below are some hints about each function you must write

#### `load_data()`

* You will need to load up all of the previously created entries when the user starts the program
* In this function, you will need to *read in* every line of data from the `data.csv` file
   * There is already a few lines in `data.csv`, check them out
   * What *module* do you need in order to work with these kind of files?
      * You've worked with this module!
      * What do you have to do, to allow your code to work with this module?
* What kind of data structure is an individual line of data represented in?
* What's the best way to store *multiples* of these data structures, once you read it in from the file?
* Does this function need to `return` something? Why or why not?
   * The answer is Yes. After you read in the data, you'll have to `return` the whole thing back to the caller of the `load_data()` function. Why?
   * Be sure to `return` *only after the file is properly closed!*
* Just like in the lesson, you'll need to use `DictReader`
* **Hint:** There are of course multiple ways to solve this, but my solution has 6-10 lines of code (just so you don't go too far off the rails).

#### `view_previous_entries()`

* The goal is to show all of the accounting entries in a human readable format
* Think about what the parameter for this function is. It's very important that you understand what the parameter is. That will inform your strategy on how to complete the rest of the function.
* **Hint:** There are of course multiple ways to solve this, but my solution has 2-4 lines of code, excluding blank lines (just so you don't go too far off the rails).

#### `display_profit_loss()`

* Your job here, as the user stories indicate, are to show the business's total income, expenses, and the profit (or loss) as the case may be
  * You'll have to **calculate** all three pieces of information
* Again, you must fully understand what the parameter is, in order to know how to write this function
* **Hint:** There are of course multiple ways to solve this, but my solution has about 10-15 lines of code, excluding blank lines (just so you don't go too far off the rails).

#### `add_new_entry()`

* This function is the most difficult, save it for last once you get everything else working
* Read through the sample output and the user stories for adding a new entry and understand what your job is here
* You'll certainly have to understand how to:
   * Solicit user input
   * Work with if statements
   * Work with dictionaries
* Just like in the lesson, you'll need to use `DictWriter`
* Remember that you have to *add* a single *line* to the end of the `.csv` file representing the new entry... what's that called again, when you *add* to the *end*?
* **Big Hint**: There is *something else, in addition to the file* where you have to add the new entry **to the end** as well, in order for option 1 or 2 to be accurate, if the user selects those as the next command...
   * Make sure that selecting *View previous entries* and *Display current profit/loss* works properly after you add the new entry -- it should reflect the update amounts.
* **STRETCH**: Handle user input errors, so that the user is prohibited from entering a string when you ask for an amount, for example
* **Hint:** There are of course multiple ways to solve this, but my solution has about 20-25 lines of code, depending if you do the stretch, excluding blank lines (just so you don't go too far off the rails).

---

# Look at You, Being a Boss!

What do you call a snake that's 3.14 meters long?

![](https://media.giphy.com/media/3owyoUHuSSqDMEzVRu/giphy.gif)

A `Pi-Thon`! :grin: