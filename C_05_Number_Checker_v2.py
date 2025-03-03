#functions here
def int_check(question, low, high):
    """Checks user enter an integer between two values"""

    error = f"Oops - please enter an integer between {low} and {high}"

    
    while True:
        
        try:
            #Change the response to an interger and check that it's more than zero
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


#Main routine goes here


#Loop for testing
while True:
    print()

    # ask user for an integer
    my_num = int_check(question="Choose a number: ", low=1, high=10)
    print(f"You chose {my_num}")