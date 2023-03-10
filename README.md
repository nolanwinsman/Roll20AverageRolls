# Roll20AverageRolls
---

Script to take the chat log in [Roll20](https://roll20.net/welcome) Campaign and calculate each character's average Dice Rolls.

## Installation

1. Clone the repo

```sh
git clone https://github.com/nolanwinsman/Roll20AverageRolls.git
```

## Requirements

- Python
- names.txt
- chat-log.txt

First, you need to create a **names.txt** file in the root of this project with the names of each of the DnD characters in Roll20 on a seperate line.

An example of a **names.txt** might be something like

```
    Aria Shadowmancer
    Kaelen Brightblade
    Thorne Ironfist
    Lyra Starweaver
    Valtair Blackthorn
```

The names need to be spelled exactly the same as they are on Roll20. 

Next, you need to create the file **chat-log.txt** in the root of this project. This is a log of your entire chat on Roll20. 

At the top of your chat, you should see a button to **View all chat entries for this game >>**

![](images/view_all_chat_entries.png)

This will open the entire chat log. Copy all of it into **chat-log.txt**

## How to Run 

With all the steps above complete, simply run the command below to run the script and it should output the statistics for each characters rolls.

```sh
python main.py
```

You can also run it with the **-r** flag to show all of the rolls

```sh
python main.py -r
```

## How it Works

The script parses the DnD chat log to calculate how many rolls each character did and what the results were. So for an example like this.

```
Ezekiel Steadywater:rolling d20
(
15
)
=15
rolling d20
(
10
)
=10
Darius Innocentini:rolling 1d20 + 5
(
7
)
+5
=12
```

It would output the following.

```
Ezekiel Steadywater:
  d20: number of rolls: 2 rolls:  (avg: 12.50)
Darius Innocentini:
  d20: number of rolls: 1 rolls:  (avg: 7.00)
```

## Files

- `main.py`: the main script file
- `README.md`: this file
- `images/` : folder for images using in README

## Improvements

- Fix bug where people not in names.txt add rolls to people in names.txt

# Contact

Nolan Winsman - [@Github](https://github.com/nolanwinsman) - nolanwinsman@gmail.com

Project Link: [https://github.com/nolanwinsman/Roll20AverageRolls](https://github.com/nolanwinsman/Roll20AverageRolls)

# Contributers

- nolanwinsman