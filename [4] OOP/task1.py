class fraction(object):

    # The constructor for our class
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):

        # Method that returns a string representation of the fraction
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):

        # Method for adding two fractions
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator, new_denominator)
    
    def __sub__(self, other):

        # Method for substracting two fractions
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return fraction(new_numerator, new_denominator)

    def inverse(self):

        # Method for computing the inverse of the fraction given
        return fraction(self.denominator, self.numerator)

first_fraction = fraction(5, 2)
second_fraction = fraction(4, 3)

# Displaying the results
print(f'Our first fraction is: {first_fraction}')
print(f'Our second fraction is: {second_fraction}')

third_fraction = first_fraction + second_fraction
print(f'Our third fraction is: {third_fraction}')

fourth_fraction = first_fraction - second_fraction
print(f'Our fourth fraction is: {fourth_fraction}')

fifth_fraction = fourth_fraction.inverse()
print(f'Our fifth fraction is: {fifth_fraction}')
