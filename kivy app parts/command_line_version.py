# Initiative tracker project 2023
# Main code functionality
# Written by Max Creutz

# Lista johon nimet ja arvot lisätään
name_value_list = []

# Looppi joka pyytää nimeä ja arvoa jotka lisätään listaan 
# Loopin voi lopettaa ainastaan kun kysytään nimeä että tulee pakosti uusi nimi ja arvo yhdistelmä mikä lisätään listaan
while True:
    # Kysytään nimeä
    name = input("Nimi (tai 'Q' lopettaaksesi): ")
    # Lopettaa loopin
    if name == 'Q':
        break
    # Kysytään arvoa
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
