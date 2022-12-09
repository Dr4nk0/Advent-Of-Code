import string
import itertools

lowercase_priority = {}
ascii_lower = list(string.ascii_lowercase)
uppercase_priority = {}
ascii_upper = list(string.ascii_uppercase)

dupplicated_item_list = []
dupplicated_item_list_value = []

i = 1
for letter in ascii_lower :
    lowercase_priority[letter] = i
    i = i + 1

i = 27
for letter in ascii_upper :
    uppercase_priority[letter] = i
    i = i + 1

with open(r"C:\Users\ng92FFF\Documents\AventOfCode\Day3\input.txt", "r") as input_file :
    # First part of the challenge
    data = input_file.readlines()
    ruckstacks = []
    for sub in data :
        ruckstacks.append(sub.replace("\n", ""))
    for ruckstack in ruckstacks :
        first_compartment = ruckstack[:len(ruckstack)//2]
        second_compartment = ruckstack[len(ruckstack)//2:]
        for item in first_compartment :
            if item in second_compartment :
                dupplicated_item_list.append(item)
                break # Once a value has been found twice, exit the ruckstack check and check next one
    for dedup_item in dupplicated_item_list :
        if dedup_item.isupper() == True :
            dupplicated_item_list_value.append(uppercase_priority[dedup_item])
        elif dedup_item.isupper() == False :
            dupplicated_item_list_value.append(lowercase_priority[dedup_item])
    print ("The sum of the priorities of the dedup items in ruckstacks is {0}".format(sum(dupplicated_item_list_value)))

with open(r"C:\Users\ng92FFF\Documents\AventOfCode\Day3\input.txt", "r") as input_file :
    # Second part of the challenge
    data = input_file.readlines()
    ruckstacks = []
    for sub in data :
        ruckstacks.append(sub.replace("\n", ""))
    every_teams = []
    every_teams_items = []
    every_teams_priority = []
    first_ident = 0
    second_ident = 3
    while second_ident <= len(ruckstacks) :
        every_teams.append(ruckstacks[first_ident:second_ident])
        first_ident = first_ident + 3
        second_ident = second_ident + 3
    group_number = 1
    for group in every_teams :
        first_elve = group[0]
        second_elve = group[1]
        third_elve = group[2]
        for item in first_elve :
            if ((item in second_elve) and (item in third_elve)) :
                every_teams_items.append(item)
                break
        group_number = group_number + 1
    for dedup_item in every_teams_items :
        if dedup_item.isupper() == True :
            every_teams_priority.append(uppercase_priority[dedup_item])
        elif dedup_item.isupper() == False :
            every_teams_priority.append(lowercase_priority[dedup_item])
    print ("The sum of the priorities of the dedup items in teams is {0}".format(sum(every_teams_priority)))
