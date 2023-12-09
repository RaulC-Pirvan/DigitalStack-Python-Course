def get_sum(my_list):

    # Base case: if the list is empty, return 0 for all our sums
    if len(my_list) == 0:
        return 0, 0, 0

    # We are going to extract the current number from the list
    current_number = my_list[0]
    
    # Recursive call to our function with the rest of the list
    total_sum, even_numbers_sum, odd_numbers_sum = get_sum(my_list[1:])
    
    # Returning a TUPLE containing our sums
    return (
        current_number + total_sum,
        even_numbers_sum + (current_number if current_number % 2 == 0 else 0),
        odd_numbers_sum + (current_number if current_number % 2 != 0 else 0)
    )    


# Initializing our list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Calling get_sum function and assigning the results to our vars
total_sum, even_numbers_sum, odd_numbers_sum = get_sum(my_list)

# Displaying the results
print(f'The total sum is: {total_sum}')
print(f'The sum of the even numbers is: {even_numbers_sum}')
print(f'The sum of the odd numbers is: {odd_numbers_sum}')
