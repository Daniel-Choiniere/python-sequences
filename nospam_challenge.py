menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]


for meal in menu:
    for item in reversed(meal):
        if "spam" == item:
            meal.remove(item)
    print(", ".join(meal))

print()

# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=", ")
#     print()



