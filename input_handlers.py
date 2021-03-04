
def perk_level_translate(translate_var):
  if isinstance(translate_var, int):
    if translate_var>=100:
      return "Master"
    elif translate_var>=75:
      return "Expert"
    elif translate_var>=50:
      return "Adept"
    elif translate_var>=25:
      return "Apprentice"
    else:
      return "Novice"
  elif isinstance(translate_var, str):
      if translate_var == "Master":
        return 100
      elif translate_var == "Expert":
        return 75
      elif translate_var == "Adept":
        return 50
      elif translate_var == "Apprentice":
        return 25
      elif translate_var == "Novice":
        return 0
      elif translate_var == "":
        pass
      else:
        raise Exception(f"error, improper string ({translate_var}) passed to perk_level_translate")
  else:
    raise Exception("error, improper variable passed to perk_level_translate")

####################

def parse_ordinator():
  parsed_dict_container = []
  text_dump_file = open("raw_data_dump/perk_ordinator_dump.txt", "r")
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
      print_strings.append(perk_level_translate(int(print_strings[0])))
      
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

def parse_apocalypse():
  parsed_dict_container = []
  text_dump_file = open("raw_data_dump/magic_apocalypse_dump.txt", "r")
  text_dump_list = [line.rstrip('\n') for line in text_dump_file]
  current_tree = ""
  current_tier = ""

  for i in text_dump_list:
    line_parse = i.split(":")
    if len(line_parse) == 1:
      if "Master" in line_parse[0]:
        current_tier = "Master"
      elif "Expert" in line_parse[0]:
        current_tier = "Expert"
      elif "Adept" in line_parse[0]:
        current_tier = "Adept"
      elif "Apprentice" in line_parse[0]:
        current_tier = "Apprentice"
      elif "Novice" in line_parse[0]:
        current_tier = "Novice"
      elif "Alteration" in line_parse[0]:
        current_tree = "Alteration"
      elif "Conjuration" in line_parse[0]:
        current_tree = "Conjuration"
      elif "Destruction" in line_parse[0]:
        current_tree = "Destruction"
      elif "Illusion" in line_parse[0]:
        current_tree = "Illusion"
      elif "Restoration" in line_parse[0]:
        current_tree = "Restoration"
    else:
      parsed_dict_container.append(
        {
          "Spell Name" : line_parse[0],
          "Spell Tree" : current_tree,
          "Skill Level" : str(perk_level_translate(current_tier)),
          "Skill Tier" : current_tier,
          #"Spell Requirements" : current_tier + " (" + perk_level_translate(current_tier) + ")",
          "Spell Description" : line_parse[1],
          "Spell Archetype" : "n/a",
          "Spell Tome Sellers" : "n/a",
        })
  return parsed_dict_container

####################

def parse_triumvirate():
  parsed_dict_container = []
  parsed_dict_container = []
  text_dump_file = open("raw_data_dump/magic_triumvirate_dump.txt", "r")
  text_dump_list = [line.rstrip('\n') for line in text_dump_file]

  current_tree = ""
  current_archetype = ""
  output_holder = [] #holds the five spells from a block until the code reaches 'available from' and can append the spell sellers to each list entry before converting to dict entries for parsed_dict_container
  spell_merchants = [] #holds the spell merchants as populated, until done
  pop_spell_merchants = False #bool for whether iterations are adding to the above list or not

  #print(text_dump_list)
  for i in text_dump_list:
    # ham-fisted fix to problem with post-block perk descriptions using parenthesis (what I was previously using to split)
    i = i.replace("Novice)", "Novice:", 1)
    i = i.replace("Apprentice)", "Apprentice:", 1)
    i = i.replace("Adept)", "Adept:", 1)
    i = i.replace("Expert)", "Expert:", 1)
    i = i.replace("Master)", "Master:", 1)
    line_parse = i.split(":")
    #print(line_parse) #testing line delete me later

    if len(line_parse) > 1:
      line_parse = [i[1:] for i in line_parse] #strip whitespace/parenthesis

      line_parse.append(current_tree)
      line_parse.append(current_archetype) # set archetype/tree

      output_holder.append(line_parse) 

      # single element lists are processed below here
    else:

      # check if we're adding spell merchants or not currently, and that we've not reached the end of that section
      if pop_spell_merchants and not line_parse[0] == "":
        # reformat the entry
        merchant_entry = line_parse[0].split(",")
        merchant_entry = merchant_entry[0] + " (" + merchant_entry[1][1:] + ")"
        spell_merchants.append(merchant_entry)

      elif pop_spell_merchants and line_parse[0] == "": #reached end
        for i in output_holder: # add all merchants to every entry in output holder
          i.append(spell_merchants)
        
          # process current output now the merchants have been appended
          parsed_dict_container.append(
            {
              "Spell Name" : i[1],
              "Spell Tree" : i[3],
              "Skill Level" : str(perk_level_translate(i[0])),
              "Skill Tier" : i[0],
              #"Spell Requirements" : current_tier + " (" + perk_level_translate(current_tier) + ")",
              "Spell Description" : i[2],
              "Spell Archetype" : i[4],
              "Spell Tome Sellers" : ", ".join(i[5]),
            })

        output_holder = []
        # clear output_holder because this entry isn't valid for output_holder and we need to make room for the next block. elements in output_holder are only line_parse entries that have multiple elements and need spell merchants appended

        spell_merchants = [] # clear spell merchants
        pop_spell_merchants = False # reset checking for spell merchants
      
      if "Available from" in line_parse[0]: #we're about to hit spell merchants so start checking every entry for this
        pop_spell_merchants = True

      if "❱❱❱" in line_parse[0]:
        current_archetype = line_parse[0][7:].title()
      # set current spell tree
      if "Alteration" in line_parse[0]:
        current_tree = "Alteration"
      elif "Conjuration" in line_parse[0]:
        current_tree = "Conjuration"
      elif "Destruction" in line_parse[0]:
        current_tree = "Destruction"
      elif "Illusion" in line_parse[0]:
        current_tree = "Illusion"
      elif "Restoration" in line_parse[0]:
        current_tree = "Restoration"
  return parsed_dict_container