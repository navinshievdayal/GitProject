import sys 
  
  
def print_to_stdout(*a): 

    print(*a, file = sys.stdout) 
  
print_to_stdout(1+2+3+4+5+6+7+8+9+10)
