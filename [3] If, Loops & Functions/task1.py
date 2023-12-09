def get_sum(*args, **kwargs):

    # We are going to initialize our return value with 0
    final_sum = 0
    for iterator in args:
        
        # We are going to check if our value is an INT instance or a FLOAT instance
        if isinstance(iterator, int) or isinstance(iterator, float):

            # if it passes the test, we will add it to the sum
            final_sum += iterator

    
    for iterator in kwargs.items():

        # We will do the same for our keywords arguments
        if isinstance(iterator, int) or isinstance(iterator, float):
            final_sum += iterator

    return final_sum


print(get_sum(1, 5, -3, 'abc', [12, 56, 'cad']))
print(get_sum())
print(get_sum(2, 4, 'abc', param_1 = 2))
