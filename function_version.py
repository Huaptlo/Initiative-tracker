name_value_list = []

def add_name_value(name, value):
    """Adds a name-value pair to the global list"""
    name_value_list.append((name, value))

def sort_names_values():
    """Sorts the global list by value in descending order"""
    name_value_list.sort(key=lambda x: x[1], reverse=True)

def print_highest_value(current_index):
    """Prints the current highest name and value to the console"""
    current_name, current_value = name_value_list[current_index]
    print(f"Highest name: {current_name}, value: {current_value}")

# example usage of the functions:
add_name_value('Alice', 10)
add_name_value('Bob', 5)
add_name_value('Charlie', 20)
sort_names_values()
print_highest_value(0) # prints "Highest name: Charlie, value: 20"