#functions here
def num_check(question, num_type, exit_code=None):
    """Checks users enter an integer / float that is more tham zero (or the optional exit code)"""

    if num_type == "integer":
        error = "Oops - please enter a inerger more than zero."
        change_to = int
    else:
        error = "Ooops - please enter a number more than zero."
        change_to = float

    while True:
        response = input(question).lower()

        # check for the exit code
        if response == exit_code:
            return response
        
        try:
            #Change the response to an interger and check that it's more than zero
            response = change_to(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


#Main routinr goes here


#Loop for testing
while True:
    print()

    my_float = num_check(question="Please enter a number more than 0: ", num_type="float")
    print(f"Thanks. You chose {my_float}")
    print()
    my_int = num_check(question="Please enter an integer more than 0: ",num_type="integer", exit_code="")

    if my_int == "":
        print("You have chosen infinite mode.")
    else:
        print(f"Thanks. You chose {my_int}")