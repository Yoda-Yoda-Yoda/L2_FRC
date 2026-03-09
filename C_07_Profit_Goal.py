def yes_no_check(question):
    """Checks that users entered yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")

def profit_goal(total_cost):
    """Calculate profit goal work out profit goal and total sales required"""
    # Initialise variable and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:
        # ask for profit goal...
        response = input("What is your profit goal (eg $500 or 50%): ")

        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # get amount (everything after the $)
            amount = response[1:]

            # check if the last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is a number more than zero.
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue
        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no_check(f"Do you mean ${amount:.2f}. ie {amount:.2f} dollars")

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            precent_type = yes_no_check(f"Do you mean {amount}%, y / n:")
            if precent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        if profit_type == "$":
            return amount

        else:
            goal = (amount / 100) * total_cost
            return goal

# main routine goes here

while True:
    total_expenses = 200
    target = profit_goal(total_expenses)
    sales_target = total_expenses + target
    print(f"Profit Goal: ${target:.2f}")
    print(f"Sales Target: ${sales_target:.2f}")
    print()