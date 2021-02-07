data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[0:2]
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# this will not work because we delete the an item therefore changing the
# index position of the items so they will skipped over
# for index, value in enumerate(data):
#     if(value < min_valid) or (value > max_valid):
#         del data[index]
#
# print(data)

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop) # for debugging
del data[:stop]
print(data)

# process the high values in the list
start = 0
# we use -1 as the stop value because the second range option is not inclusive,
# so we need to use -1 to get the last item in the data.
# Then we use a step of -1 to work backwards
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # We have the index of the last item we want to keep
        # Set start to the position of the first item to delete,
        # which is 1 after index
        start = index + 1
        break
print(start)
del data[start:]
print(data)

