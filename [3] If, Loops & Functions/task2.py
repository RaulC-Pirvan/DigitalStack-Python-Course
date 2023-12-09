def get_sum(my_list):
    if len(my_list) == 0:
        return 0, 0, 0

    current_number = my_list[0]

    total_sum, even_numbers_sum, odd_numbers_sum = get_sum(my_list[1:])
    
    return (
        current_number + total_sum,
        even_numbers_sum + (current_number if current_number % 2 == 0 else 0),
        odd_numbers_sum + (current_number if current_number % 2 != 0 else 0)
    )    


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

total_sum, even_numbers_sum, odd_numbers_sum = get_sum(my_list)

print(f'The total sum is: {total_sum}')
print(f'The sum of the even numbers is: {even_numbers_sum}')
print(f'The sum of the odd numbers is: {odd_numbers_sum}')
