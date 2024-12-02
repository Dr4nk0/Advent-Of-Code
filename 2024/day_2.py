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

with open('input.txt') as f:
    lines = f.readlines()


def is_level_safe (splitted) :
    
    splitted_unique = [i for i in splitted if splitted.count(i) <= 1]
    
    if len(splitted) == len(splitted_unique) :

        if sorted(splitted) == splitted or sorted(splitted, reverse=True) == splitted :
            
            for i in range(1, len(splitted)) :
                if abs(splitted[i] - splitted[i-1]) > 3 :
                    return False
            return True
    else :
        return False


def is_level_dampener (split) :

    for i in range(len(split)) :

        new_split = split[:i] + split[i+1:]

        if is_level_safe(new_split) :
            return True


counter_part_one = 0
counter_part_two = 0

for line in lines:

    splitted = line.split()
    splitted_int = [int(i) for i in splitted]
    
    if is_level_safe (splitted_int) :
        counter_part_one = counter_part_one + 1
    else :
        if is_level_dampener(splitted_int) :
            counter_part_two = counter_part_two + 1

    
print (f"The result of part one is {counter_part_one}")
print (f"The result of part two is {counter_part_one+counter_part_two}")

