import re
import random
from collections import defaultdict

# function to parse dice notation
def parse_dice(dice_str):
    match = re.match(r'(\d*)d(\d+)([+-]\d+)?', dice_str)
    if match:
        num_dice = int(match.group(1)) if match.group(1) else 1
        num_sides = int(match.group(2))
        modifier = int(match.group(3)) if match.group(3) else 0
        return num_dice, num_sides, modifier
    else:
        print(f"Invalid dice notation: {dice_str}")
        return None


# read chat log file
with open('chat-log.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# initialize dictionary to store roll data for each character name
roll_data = {}

# iterate over lines and update roll data for each character name
for line in lines:
    # extract character name and dice notation from line
    match = re.search(r'(.+?):rolling\s+(.+)', line)
    if match:
        name = match.group(1)
        dice_str = match.group(2)
        # parse dice notation
        dice_data = parse_dice(dice_str)
        if dice_data is None:
            continue
        num_dice, num_sides, modifier = dice_data
        # roll dice and calculate sum
        roll_sum = sum(random.randint(1, num_sides) for _ in range(num_dice)) + modifier
        # update roll data for character name
        if name in roll_data:
            roll_data[name]['sum'][num_sides] += roll_sum
            roll_data[name]['count'][num_sides] += 1
        else:
            roll_data[name] = {'sum': defaultdict(int), 'count': defaultdict(int)}
            roll_data[name]['sum'][num_sides] = roll_sum
            roll_data[name]['count'][num_sides] = 1


# calculate average roll for each character name
for name, data in roll_data.items():
    print(name)
    for num_sides, sum in data['sum'].items():
        if data['count'][num_sides] > 0:
            average_roll = sum / data['count'][num_sides]
            print('  d{}: {:.2f}'.format(num_sides, average_roll))
        else:
            print('  d{}: no rolls found'.format(num_sides))
