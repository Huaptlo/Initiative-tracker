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
    print(f"Nimi: {current_name}, arvo: {current_value}")

# Esimerkkejä käytöstä
# Lisätään nimi ja arvo
add_name_value('Pekka', 10)
add_name_value('Jukka', 5)
add_name_value('Örkki 1', 20)
# Järjestetään lista
sort_names_values()
# Haetaan listasta nesimmäinen arvo, muuttamalla suluissa olevaa lukua saadaan haettua eri nimi ja arvo
print_highest_value(0) # Tulostaa "Nimi: Örkki 1, arvo: 20"