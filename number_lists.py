even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
print(len(even))
print(len(odd))

print()
print("mississippi".count("s"))
print("mississippi".count("iss"))

# combines the odd list to the even list
print()
even.extend(odd)
print(even)

# sorting does not create a new list, it arranges the items in the list
even.sort()
print(even)

even.sort(reverse=True)
print(even)

