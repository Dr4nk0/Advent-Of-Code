from heapq import nlargest
Elfs_inventory = {}

with open(r"input.txt", "r") as input_file :
    data = input_file.read()
    # First part of the challenge
    groups = [ grp.split("\n") for grp in data.split("\n\n") ]
    elf_number = 1
    for elf in groups :
        elf = list(map(int, elf))
        elf_power = sum(elf)
        Elfs_inventory[elf_number] = elf_power
        elf_number = elf_number + 1
    print("The biggest power holded by an Elf is", max(Elfs_inventory.values()))
    # Second Part of the challenge
    top_three_calories = nlargest(3, Elfs_inventory, key = Elfs_inventory.get)
    calories_count = 0
    for val in top_three_calories :
        calories_count = calories_count + Elfs_inventory.get(val)
    print ("The top three Elves are carrying a total of {0} calories".format(calories_count))
