print("Welcome to the fizzbuzz game!")

number_select = input("Select a number between 1 and 100: ")
number_select = int (number_select)
print(number_select)

for number_select in range (1, +number_select+1):
    if number_select % 3 == 0 and number_select % 5 == 0:
        print("fizzbuzz")

    elif number_select % 3 == 0:
        print("fizz")

    elif number_select % 5 == 0:
        print("buzz")

    else:
        print(number_select)

