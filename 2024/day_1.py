with open('day_1_input.txt') as f:
    lines = f.readlines()

first_list = []
second_list = []

for line in lines:
    parties = line.strip().split()
    entier1, entier2 = map(int, parties)
    first_list.append(entier1)
    second_list.append(entier2)


def part_one (first_list, second_list):
    first_list_sorted = sorted(first_list)
    second_list_sorted = sorted(second_list)
    
    counter = 0

    for index, num in enumerate(first_list_sorted) :

        diff = num - second_list_sorted[index]
        counter = counter + abs(diff)

    return counter

def part_two (first_list, second_list):
    hash_table = {}

    counter = 0

    for i in first_list :
        if i in second_list : 
            hash_table[i] = second_list.count(i)

    for key, value in hash_table.items() :
        if value > 0 :
            sum = key * value
            counter = counter + sum
    
    return counter


print (f"The answer for part one is : {part_one (first_list, second_list)}")
print (f"The answer for part two is : {part_two (first_list, second_list)}")