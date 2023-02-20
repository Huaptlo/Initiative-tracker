# Initiative tracker project 2023
# Main code functionality
# Written by Max Creutz


name_value_list = []

# Looppi joka pyytää nimeä ja arvoa jotka lisätään listaan
while True:
    # Kysytään nimeä ja arvoa
    name = input("Name (or 'end' to exit): ")
    if name == 'end':
        break
    value = int(input("Initiative: "))

    # Lisätään nimi ja arvo listaan
    name_value_list.append((name, value))

# Järjestetään lista takaperin
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
