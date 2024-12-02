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

def day_2_part_one (splitted) :
    
    splitted_unique = [i for i in splitted if splitted.count(i) <= 1]
    
    if len(splitted) == len(splitted_unique) :

        if sorted(splitted) == splitted or sorted(splitted, reverse=True) == splitted :
            
            for i in range(1, len(splitted)) :
                if abs(splitted[i] - splitted[i-1]) > 3 :
                    return False
            return True
    else :
        return False

                        
with open('input.txt') as f:
    lines = f.readlines()

    
counter_part_one = 0


for line in lines:
    splitted = line.split()
    splitted_int = [int(i) for i in splitted]
    
    if day_2_part_one (splitted_int) :
        print (f"{splitted_int} is safe")
        counter_part_one = counter_part_one + 1
    else :
        for index, num in enumerate(splitted_int) :
            test = splitted_int.pop(index)
            if day_2_part_one (test) :
                counter_part_one = counter_part_one + 1
            else :
                print (f"{splitted_int} is unsafe")
    
print (f"The result for part_two is {counter_part_one}")

