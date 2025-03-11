#functions here
def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer."
    
    while True:
        
        try:
            #Change the response to an interger and check that it's more than zero
            response = int(input(question))

            return response

        except ValueError:
            print(error)


#Main routine goes here


#Loop for testing
while True:
    print()

    #ask user for their name
    name = input("Name: ")

    #ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    #output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")