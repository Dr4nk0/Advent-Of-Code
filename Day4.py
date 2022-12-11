count = []
count_2 = []

def check_list_nesting (a,b,c,d) :
    if (a >= c) and (b <= d) : # Full overlap of list A in list B
        count.append(1)
    elif (c >= a) and (d <= b) : # Full overlap of list B in list A
        count.append(1)

def check_list_nesting_one (a,b,c,d) :
    if (b == c) or (a == c) :
        count_2.append(1)
    elif (a == d) or (b == d) :
        count_2.append(1)
    if (a > c) and (b < d) :
        count_2.append(1)
    elif (c > a) and (d < b) :
        count_2.append(1)

with open(r"input.txt", "r") as input_file :
    # First part of the challenge
    data = input_file.readlines()
    counter = 0
for line in data :
    values = line.split(",")
    a, b = values[0].split("-")
    c, d = values[1].split("-")
    a_r = int(a)
    b_r = int (b)
    c_r = int (c)
    d_r = int (d)
    check_list_nesting(a_r,b_r,c_r,d_r)
    # Second part of the challenge
    check_list_nesting_one(a_r,b_r,c_r,d_r)
print (f"There is a total of {sum(count)} pairs fully overlapping themselves")
print (f"There is a total of {sum(count_2)} pairs that overlap on at least one number")
