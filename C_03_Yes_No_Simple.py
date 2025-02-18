#functions here
def yes_no(question):
    """Checks that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")


#main routine goes here
while True:
    want_instrustions = yes_no("Do you want to read the instructions? ")
    print(f"You chose {want_instrustions}\n")