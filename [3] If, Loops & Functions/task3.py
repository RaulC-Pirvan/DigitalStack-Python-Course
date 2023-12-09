def print_value():
    try:

        # We store the keyboard input into our value var
        value = input('Please insert an integer: ')

        # Converting our input to int and then returning it
        return int(value)

    # Exception for when the input is not an integer
    except ValueError as e:
        print('That was not an integer ;-;')
        return 0

# We call our method and display the result
print(f'The result is: {print_value()}')
