
def not_blank(question):
    """Checks that a user input isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry! this can't be blank. Please try again\n")

def num_check(question, num_type="float", exit_code=None):
    """Checks that response is a float / integer """

    if num_type == "float":
        error = "Please enter a number more then 0"
    else:
        error = "Please enter an integer more then 0"

    while True:
        try:

            if num_type == "float":
                response = float(input(question))
            else:
                response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def get_expenses(exp_type):
    """Get variable / fixed expenses and outputs
    panda (as a string) and a subtotal of the expenses"""

    # Lists for panda
    all_items = []

    # Expenses dictionary

    # Loop to get expenses
    while True:
        item_name = not_blank("Item Name: ")

        # check user enter at least one variable expenses
        if (exp_type == "variable" and
            item_name == "xxx") and len(all_items) == 0:
            print("Oops - you have not entered anything. "
                  "You need at least one item.")
            continue

        elif item_name == "xxx":
            break

        all_items.append(item_name)

    # return all items for now so we can check loop
    return all_items


# main routine starts here

# print("Getting Variable Costs... ")
# variable_expenses = get_expenses("variable")
# num_variable = len(variable_expenses)
# print(f"You entered {num_variable} item")
# print()

print("Getting fixed costs...")
fixed_expenses = get_expenses("fixed")
num_fixed = len(fixed_expenses)
print(f"Yoy entered {num_fixed} items")