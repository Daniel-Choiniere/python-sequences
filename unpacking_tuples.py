a = b = c = d = e = f = 12
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking a tuple")
data = 1, 2, 76  # data representing a tuple
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a list")
data_list = [12, 13, 14]  # data representing a list
p, q, r = data_list
print(p)
print(q)
print(r)

print()
# another advantage of tuples is that you can always unpack a tuple
# because a tuple cant be changed you always know how many items there are to unpack

# using enumerate to "pack" tuples
for character in enumerate("abcdefgh"):
    print(character)