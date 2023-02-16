name_value_list = []

# loop to allow user to add as many names and values as they want
while True:
    # prompt user to enter a name and a numeric value
    name = input("Enter a name (or 'done' to exit): ")
    if name == 'done':
        break
    value = int(input("Enter a numeric value: "))

    # add the name and value to the list
    name_value_list.append((name, value))

# sort the list by value in descending order
name_value_list.sort(key=lambda x: x[1], reverse=True)

# loop to allow user to cycle through the sorted list
current_index = 0
while True:
    current_name, current_value = name_value_list[current_index]
    print(f"Highest name: {current_name}, value: {current_value}")
    input_str = input("Press enter to see the next highest value, or type 'done' to exit: ")
    if input_str == 'done':
        break
    current_index = (current_index + 1) % len(name_value_list)
