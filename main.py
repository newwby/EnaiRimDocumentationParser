import ordinator_parse as parse1
import time
import replit

def run_loop():
  user_input = ""
  accepted_input = ["EXIT", "FILE"]
  raw_state = True
  while user_input.upper() not in accepted_input:
    print("\n\n#########################")
    print("Accepted commands:\nEXIT << Exits program\nFILE << toggles print mode versus output to file mode\nPERK << executes perk (Ordinator) function\n\n(File Output Mode currently set to {0})".format(str(raw_state).upper()))
    print("#########################\n")
    user_input = input("Please input command: ")
  if user_input.upper() == "FILE":
    raw_state = not raw_state
    print("\nFile Output Mode has been set to {0}\n".format(str(raw_state).upper()))
    time.sleep(2)
    replit.clear()
    run_loop()
  elif user_input.upper() == "EXIT":
    replit.clear()
  elif user_input.upper() == "PERK":
    # print organised ordinator text dump data
    parse1.print_ordinator(parse1.parse_ordinator())

run_loop()