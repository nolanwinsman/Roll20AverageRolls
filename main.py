import re

log_file = 'chat-log.txt'
roll_data = {}
NAMES = [] # names should be loaded in from .env file

def load_names():
    global NAMES
    with open("names.txt", "r") as f:
        NAMES = [line.strip() for line in f]



def add_roll(name, dice, result):
    if name not in  roll_data:
         roll_data[name] = {}
    if dice not in  roll_data[name]:
         roll_data[name][dice] = []
    roll_data[name][dice].append(result)

def find_roll(s):
    pattern = r"d(\d+)"
    if "rolling" in s.lower():
        match = re.search(pattern, s)
        if match:
            roll_value = match.group(1)
            return roll_value
    return None

def find_name(s):
    for name in NAMES:
        if name in s:
            return name
    return None

def main():
    load_names()

    with open(log_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        current_name, current_roll = None, None
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
                if stripped_string.isdigit():
                    add_roll(current_name, current_roll, int(stripped_string))

    for name, dice_data in roll_data.items():
        print(f"{name}:")
        for dice_type, rolls in dice_data.items():
            avg_roll = sum(rolls) / len(rolls)
            print(f"  d{dice_type}: number of rolls: {len(rolls)} rolls: {None}(avg: {avg_roll:.2f})")


if __name__ == "__main__":
    main()