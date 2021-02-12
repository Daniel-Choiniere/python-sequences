# Working solution
numbers = input("Please enter three comma separated numbers").split(",")

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])

answer = numbers[0] + numbers[1] - numbers[2]
print(answer)


# Not working solution
numbers = input("Please enter three comma separated numbers")

numbers.split(",")

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])

answer2 = numbers[0] + numbers[1] - numbers[2]
print(answer2)


