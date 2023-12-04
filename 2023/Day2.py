import re

with open('Day2-input.txt') as f:
    lines = f.readlines()
    
game_score = {}
total = 0

blue_regex = r'(\d+)\s+blue'
red_regex = r'(\d+)\s+red'
green_regex = r'(\d+)\s+green'

for line in lines :
    
    # Get Game ID
    pattern = re.compile(r'(\d+):')
    match = pattern.search(line)
    game_ID = match.group(1)
    game_score[game_ID] = {}

    # Get blue values
    blue_count = 0
    game_count = []
    resultats = re.findall(blue_regex, line)
    for i in resultats : game_count.append(int(i))
    game_score[game_ID]["blue"] = game_count
    
    # Get red values
    red_count = 0
    game_count = []
    resultats = re.findall(red_regex, line)
    for i in resultats : game_count.append(int(i))
    game_score[game_ID]["red"] = game_count
    
    # Get green values
    green_count = 0
    game_count = []
    resultats = re.findall(green_regex, line)
    for i in resultats : game_count.append(int(i))
    game_score[game_ID]["green"] = game_count

for key, value in game_score.items() :

    # Part One
    # if (max(value["red"]) <= 12) and (max(value["green"]) <= 13) and (max(value["blue"]) <= 14) : total = total + int(key)
 
    # Part Two
    min_blue = max(value["blue"])
    min_red = max(value["red"])
    min_green = max(value["green"])
    
    game_total = min_blue * min_red * min_green
    total = total + game_total
 

print (total)
