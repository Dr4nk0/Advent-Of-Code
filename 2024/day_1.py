from functools import wraps
from time import time

def timed(f):
  @wraps(f)
  def wrapper(*args, **kwds):
    start = time()
    result = f(*args, **kwds)
    elapsed = time() - start
    print (f"{f.__name__} took {elapsed} time to finish")
    return result
  return wrapper


with open('day_1_input.txt') as f:
    lines = f.readlines()

first_list = []
second_list = []

for line in lines:
    parties = line.strip().split()
    entier1, entier2 = map(int, parties)
    first_list.append(entier1)
    second_list.append(entier2)

@timed
def part_one (first_list, second_list):

    first_list_sorted = sorted(first_list)
    second_list_sorted = sorted(second_list)
    
    # Zip create a list dict of tupples : {('84511', '39170'), (3, 'THREE'), (1, 'ONE')}
    counter = sum(abs(a - b) for a, b in zip(first_list_sorted, second_list_sorted))

    return counter

@timed
def part_two (first_list, second_list):
    
    hash_table = {}
    counter = 0

    for i in first_list :
        if i in second_list : 
            if i not in hash_table :
                hash_table[i] = 0
            hash_table[i] += 1

    for key, value in hash_table.items() :
        counter += key * value
    
    return counter


print (f"The answer for part one is : {part_one (first_list, second_list)}")
print (f"The answer for part two is : {part_two (first_list, second_list)}")