
#########################
"""
Accepts input in the form of a list containing dict entries for every item.
(Basically objects but with built-in python types)
"""
#########################

def parser_printer(given_list: list, file_output_string: str, write_raw_to_file: bool = True, erase_file: bool = True):
  if write_raw_to_file:
    if erase_file:
      given_file = open(file_output_string, "w")
    else:
      given_file = open(file_output_string, "a")
  
  for i in given_list: # i is the dict
    for n in i: # n is the key:value pairs in dict
      if not write_raw_to_file:
        print_line(n, i)
      else:
        given_file.write(i[n] + "\t")
        #print(i[n], end='\t')
    if not write_raw_to_file:
      print() # at end print a blank line to separate perk blocks
    else:
      given_file.write("\n")
  if not write_raw_to_file:
    print("\nFinished printing to console. \n")
  else:
    print("\nPrinted output to: " + file_output_string + "\n")

# simplifies printing dict
def print_line(given_string, given_dict):
  print(given_string + ": " + given_dict[given_string])