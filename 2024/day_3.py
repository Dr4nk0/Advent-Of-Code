from functools import wraps
from time import time
import re

def timed(f):
  @wraps(f)
  def wrapper(*args, **kwds):
    start = time()
    result = f(*args, **kwds)
    elapsed = time() - start
    print (f"{f.__name__} took {elapsed} time to finish")
    return result
  return wrapper
    
def part_one (lines) :
    
    total = 0
        
    for line in lines:
        
        mul_instructions = re.findall(r'mul\(\d+,\s*\d+\)', line)
        
        for mul in mul_instructions :
            
            numeric_values = [int(i) for i in re.findall(r'\b\d+\b', mul)]
            
            total = total + numeric_values[0] * numeric_values[1]

    print (f"Result for part one is : {total}")
    

def part_two (lines) :
    
    total = 0
    save = []
    
    
    for line in lines :
        
        index_record = 0
                
        instructions = re.findall(r"(?:mul\(\d+,\s*\d+\)|do\(\)|don't\(\))", line)
                
        for i in instructions :
            
            if "mul" not in i :
                index_record = instructions.index(i)
                break
            else :
                save.append(i)
                                
                                            
        # for i in instructions :
            
        #     print (f"\n{instructions =}\n")
        #     print (i)
            
        #     if i == "don't()" : 
                                
        #         for j in instructions[instructions.index(i)+1:] :
                    
        #             print (f" parsed : {instructions[instructions.index(i)+1:]}")
                
        #             if "mul" in j :
                        
        #                 instructions.pop(instructions.index(j))
                    
        #             elif "do()" in j :
        #                 break
        #     else : 
        #         pass
                                                                
        for i in instructions[index_record:] :
            
            if i == "do()" : 
                
                for j in instructions[instructions.index(i)+1:] :
                                            
                    if "mul" not in j : 
                        
                        continue
                        
                    else :
                        save.append(j)
                    
        #print (save)
                        
        for mul in save :
            
            numeric_values = [int(i) for i in re.findall(r'\b\d+\b', mul)]
            
            total = total + numeric_values[0] * numeric_values[1]

    print (f"Result for part two is : {total}")

############################

with open('input.txt') as f:
    lines = f.readlines()
    
part_one (lines)

part_two (lines)

