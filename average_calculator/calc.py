def calculator():
    print("This calculator will help you find an average!")
    print("Enter integers one at a time.")
    print("When you're ready to compute an average, type 'compute'")
    
    finished = False
    numbers = []
    while not finished:
        user_input = input("Enter an integer or 'compute': ")
        
        if user_input == "compute":
            print_average(numbers)
            finished = True
           
        else:
            try:
                number = int(user_input)
                numbers.append(number)
            except ValueError:
                print("Invalid input. Input must be an integer or 'compute'")


def print_average(numbers):
    average_value = rounded_average(numbers)
    print(f"The rounded average of the numbers you entered is {average_value}")


def rounded_average(numbers):
    avg = sum(numbers) / len(numbers)
    return round(avg)
