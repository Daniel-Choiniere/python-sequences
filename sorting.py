# A pangram is a sentence that contains every letter from the alphabet
pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
# sorted creates a whole new list, thats why we bind it to a new variable
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# sort does not create a new list it just arranges it
numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)