# Initiative tracker project 2023
# Main code functionality
# Written by Max Creutz

initiative_list = []
initiative_list_ordered = []

name = input("Name: ")
value = int(input("Value: "))

character = name,value

initiative_list.append(character)

name = input("Name: ")
value = int(input("Value: "))

character = name,value

initiative_list.append(character)

print(initiative_list)

initiative_list_ordered = initiative_list

print("Sorted:", initiative_list_ordered.sort(key=lambda x: x[1], reverse=True))