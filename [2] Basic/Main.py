# Initializing our list
list_of_numbers = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# We are going to sort a copy of our list, so we can keep our initial list unmodified
sorted_list_of_numbers = sorted(list_of_numbers)
print("Sorted list: ", sorted_list_of_numbers)

# We are going to sort another copy of our list in descending order
descending_list_of_numbers = sorted(list_of_numbers, reverse=True)
print("Descending list: ", descending_list_of_numbers)

# Using slice to only print the numbers with an even index
even_index_list_of_numbers = list_of_numbers[::2]
print("Even index: ", even_index_list_of_numbers)

# Same as before but we are printing the numbers with an odd index
odd_index_list_of_numbers = list_of_numbers[1::2]
print("Odd index: ", odd_index_list_of_numbers)

# We are going to create a separate list for our multiples of 3
multiples_of_3 = []

# Using a FOR loop we are going to check every element of our list
for num in list_of_numbers:
    # the IF statement checks if the current number is a multiple of 3
    if num % 3 == 0:
        multiples_of_3.append(num)
print("Multiples of 3: ", multiples_of_3)
