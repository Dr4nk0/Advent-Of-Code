with open('day1-input.txt') as f:
    lines = f.readlines()


digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
total = 0

for line in lines : 
    
    line_count = []
    line_value = 0

    for letter in line : 

        if letter in digits : line_count.append(letter)

    line_value = line_count[0] + line_count[-1]
    total = total + int (line_value)

print (total)


digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
alpha_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def find_all(s, c):
    idx = s.find(c)
    while idx != -1:
        yield idx
        idx = s.find(c, idx + 1)

total = 0

for line in lines :

    numbers = {'1' : [], '2': [], '3': [], '4': [], '5': [], '6':[], '7':[], '8':[], '9':[]}

    for index, alpha in enumerate(alpha_digits) :

        all = find_all(line, alpha)
        for x in all : numbers[digits[index]].append(x)

    for digit in digits :

        all = find_all(line, digit)
        for x in all : numbers[digit].append(x)
    
    global_list = []
    number_final = []

    for key in numbers:
        for x in numbers[key]:
            global_list.append(x)

    min_value = min(global_list)
    max_value = max(global_list)

    for key, value in numbers.items():
        if min_value in value : number_final.append(key)
    
    for key, value in numbers.items():
        if max_value in value: number_final.append(key)

    string = ''

    for number in number_final : 

        string += str(number)

    total = total + int (string)

print (total)

