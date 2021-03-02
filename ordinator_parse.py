
def parse_ordinator():
  parsed_dict_container = []
  text_dump_file = open("ordinator_dump.txt", "r")
  text_dump_list = [line.rstrip('\n') for line in text_dump_file]
  current_tree = ""

  for i in text_dump_list:
    print_strings = i.split(" - ")
    
    # perk block separators are 1 alphanumerical/whitespace character so this check excludes them when searching for specific headers
    if len(print_strings) >= 2:
      print_strings[1] = print_strings[1].partition("(")
      if not print_strings[1][1] == "":
        #combine partitioned tuples
        print_strings.append(print_strings[1][2][0])
        #strip trailing whitespace
        print_strings[1] = print_strings[1][0][:-1]
      else:
        print_strings.append("1")
        print_strings[1] = print_strings[1][0]

      #append perk tree
      print_strings.append(current_tree)

      #append perk proficiency level
      if int(print_strings[0])>=100:
        print_strings.append("Master")
      elif int(print_strings[0])>=75:
        print_strings.append("Expert")
      elif int(print_strings[0])>=50:
        print_strings.append("Adept")
      elif int(print_strings[0])>=25:
        print_strings.append("Apprentice")
      else:
        print_strings.append("Novice")
      parsed_dict_container.append(
        {
          "Perk Name" : print_strings[1],
          "Perk Tree" : print_strings[4],
          "Skill Level" : print_strings[0],
          "Skill Tier" : print_strings[5],
          #"Skill Requirements" : print_strings[5] + " (" + print_strings[0] + ")",
          "Perk Limit" : print_strings[3],
          "Perk Description" : print_strings[2],
        }
      )
    #update perk tree
    elif not print_strings[0] == "":
        current_tree = print_strings[0]

  return parsed_dict_container # the organised data dict

####################

def print_ordinator(given_list: list, write_raw_to_file: bool = True):
  ordinator_file = open("ordinator_output.txt", "w")
  
  for i in given_list: # i is the dict
    for n in i: # n is the key:value pairs in dict
      if not write_raw_to_file:
        print_line(n, i)
      else:
        ordinator_file.write(i[n] + "\t")
        #print(i[n], end='\t')
    if not write_raw_to_file:
      print() # at end print a blank line to separate perk blocks
    else:
      ordinator_file.write("\n")

# simplifies printing dict
def print_line(given_string, given_dict):
  print(given_string + ": " + given_dict[given_string])