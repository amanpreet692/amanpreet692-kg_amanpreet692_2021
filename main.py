def is_mapping_possible(s1,s2):
  mapping = dict()
  if len(s1) != len(s2):
    return False
  for i in range(len(s1)):
    c1 = s1[i]
    c2 = s2[i]
    if c1 not in mapping:
       mapping[c1] = c2
    elif mapping[c1] != c2:
      return False  
  return True
  
  
import sys
arg_list = sys.argv
if len(arg_list) < 3:
  print("Please provide the required arguments for the program")
  sys.exit()
print(str(is_mapping_possible(arg_list[1], arg_list[2])).lower())