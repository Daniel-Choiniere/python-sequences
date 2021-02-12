# use parentheses instead of brackets to create a tuple
t = ("a", "b", "c")
print(t)


name = "Dan"
age = 35

# Not a tuple
print(name, age, "Python", 2021)
# A tuple
print((name, age, "Python", 2021))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# still use square brackets when accessing tuples
# Tuples are IMMUTABLE, this protects the integrity of your data
# Tuples use less memory than lists
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# Converting a tuple to a list
metallica2 = list(metallica)
print(metallica2)

