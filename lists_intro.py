computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse pad"]

# for part in computer_parts:
#     print(part)
#
# print()
# print(computer_parts[2]) # keyboard
#
# print(computer_parts[0:3]) # computer, monitor, keyboard
# print(computer_parts[-1]) # mouse pad

    # STRINGS ARE IMMUTABLE THEY CAN NOT BE CHANGED
    # LISTS ARE MUTABLE AND THEY CAN BE CHANGED, SORTED ETC.

    # replaces the item at position 3
# computer_parts[3] = "trackball"
# print(computer_parts)

    # replaces multiple items using slice
print(computer_parts[3:])
computer_parts[3:] = ["trackball"]
print(computer_parts)