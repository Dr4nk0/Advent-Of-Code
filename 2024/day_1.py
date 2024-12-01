with open('day_1_input.txt') as f:
    lines = f.readlines()

first_list = []
second_list = []

for line in lines:
    # Supprimer les espaces inutiles et diviser la ligne en deux nombres
    parties = line.strip().split()
    # Convertir les deux parties en entiers
    if len(parties) == 2:  # S'assurer qu'il y a exactement deux colonnes
        entier1, entier2 = map(int, parties)
        first_list.append(entier1)
        second_list.append(entier2)

def part_one (first_list, second_list):
    fl = sorted(first_list)
    sl = sorted(second_list)
    counter = 0

    for value in fl :
        value_index = fl.index(value)
        diff = value - sl[value_index]
        counter = counter + abs(diff)

    return counter

def part_two (first_list, second_list):
    hashmap = {}
    counter = 0

    for i in first_list :
        if i in second_list : 
            hashmap[i] = second_list.count(i)

    for key, value in hashmap.items() :
        if value > 0 :
            sum = key * value
            counter = counter + sum
    
    return counter


print (part_one (first_list, second_list))
print (part_two (first_list, second_list))