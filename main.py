# Initiative tracker project 2023
# Main code functionality
# Written by Max Creutz


name_value_list = []

# Looppi joka pyytää nimeä ja arvoa jotka lisätään listaan
while True:
    # Kysytään nimeä ja arvoa
    name = input("Nimi (tai 'Q' lopettaaksesi): ")
    if name == 'Q':
        break
    value = int(input("Aloite: "))

    # Lisätään nimi ja arvo listaan
    name_value_list.append((name, value))

# Järjestetään lista takaperin
name_value_list.sort(key=lambda x: x[1], reverse=True)

# Looppi jolla käyttäjä saa seuraavan nimen ja arvon
current_index = 0
while True:
    current_name, current_value = name_value_list[current_index]
    print(f"Nimi: {current_name}, aloite: {current_value}")
    input_str = input("Paina enter seuraavaan (tai 'Q' lopettaaksesi): ")
    if input_str == 'Q':
        break
    current_index = (current_index + 1) % len(name_value_list)
