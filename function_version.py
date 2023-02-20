name_value_list = []

def add_name_value(name, value):
    # Lisää nimen ja arvon listaan
    name_value_list.append((name, value))

def sort_names_values():
    # Järjestää nimet listassa takaperin
    name_value_list.sort(key=lambda x: x[1], reverse=True)

def print_highest_value(current_index):
    # Tulostaa ensimmäisen listassa olevan nimen ja arvon
    current_name, current_value = name_value_list[current_index]
    print(f"Highest name: {current_name}, value: {current_value}")

# Esimerkkejä käytöstä
add_name_value('Pekka', 10)
add_name_value('Jukka', 5)
add_name_value('Örkki 1', 20)
sort_names_values()
print_highest_value(0) # Tulostaa "Highest name: Charlie, value: 20"