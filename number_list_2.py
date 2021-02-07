empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

# sorted creates a new list
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# when you create a list from another a list the contents of thew list will be the same type as that object
digits = sorted("432985617")
# creates a list of strings
print(digits)

# using built in list function creates a list
digits = list("432985617")
print(digits)

# best way to copy a list to create a new identical list is with the built in copy function
more_numbers = numbers.copy()
print(more_numbers)
# not the same object - FALSE
print(numbers is more_numbers)
# but contains the same items - TRUE
print(numbers == more_numbers)
