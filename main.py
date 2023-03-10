import re

log_file = 'test.txt'
roll_data = {}
NAMES = [] # names should be loaded in from names.txt
import argparse

def load_names():
    """Loads in the character names from names.txt into the global dictionary NAMES
    """
    global NAMES
    with open("names.txt", "r") as f:
        NAMES = [line.strip() for line in f]

def arguments():
    """If the script is called with the -r flag, returns True to show all the rolls.
       Otherwise, returns False
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--show-rolls", help="show rolls", action="store_true")
    args = parser.parse_args()

    return args.show_rolls

def add_roll(name, dice, result):
    """Adds the data for a roll into the roll_data dictionary.

       Parameters: 
       name -- The character that made the roll
       dice -- What dice was roll, like a d20, d10, d6, ect.
       result -- The value of the dice roll. So if a d20 rolled an 11, result would be 11
    """
    if name not in  roll_data:
         roll_data[name] = {}
    if dice not in  roll_data[name]:
         roll_data[name][dice] = []
    roll_data[name][dice].append(result)

def find_roll(s):
    """Takes in a string and tries to parse a roll. 
       So the string "Ezekiel rolling d20" would return 20.
       If no match is found, returns None

       Parameters :
       s -- string of text

       Return:
       roll_value if dice roll is found. Otherwise None.
    """
    pattern = r"d(\d+)"
    if "rolling" in s.lower():
        match = re.search(pattern, s)
        if match:
            roll_value = match.group(1)
            return roll_value
    return None

def find_name(s):
    """Finds the character name in a string if a name in NAMES is detected

       Parameters :
       s -- string of text

       Return:
       The character name if found. Otherwise None.
    """
    for name in NAMES:
        if name in s:
            return name
    return None

def main():
    """ Main function that handles reading in the chat-log.txt and parsing the data to find the
       statistics for dice rolls in a Dungeons and Dragons Campaign.
    """
    load_names()
    show_rolls = arguments()

    # Reads in log_file
    with open(log_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        current_name, current_roll = None, None
        # loops through every line in the chat-log
        for i, line in enumerate(lines):

            name =  find_name(line)
            roll = find_roll(line)
        
            if name is not None:
                current_name = name
                current_roll = None # fixes some edge cases
            if roll is not None:
                current_roll = roll

            if current_name != None and current_roll != None:
                stripped_string = line.replace(" ", "").replace("\t", "").replace("\n", "")
                # if the line is just a number with nothing else
                if stripped_string.isdigit():
                    add_roll(current_name, current_roll, int(stripped_string))

    # Prints the data found
    for name, dice_data in roll_data.items():
        print(f"{name}:")
        for dice_type, rolls in dice_data.items():
            avg_roll = sum(rolls) / len(rolls)
            print(f"  d{dice_type}: number of rolls: {len(rolls)} rolls: {rolls if show_rolls else ''} (avg: {avg_roll:.2f})")


if __name__ == "__main__":
    main()