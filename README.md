# Roll20AverageRolls
---

Script to take the chat log in Roll20 Campaign and calculate each character's average Dice Rolls.

## Installation

1. Clone the repo

```sh
git clone https://github.com/nolanwinsman/Roll20AverageRolls.git
```

## Requirements

- Python
- names.txt
- chat-log.txt

First, you need to create a **names.txt** file in the root of this project with the names of each of the DnD characters in Roll20.

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

With all the steps above complete, simply run the command

```sh
python main.py
```

to run the script and it should output the statistics for each characters rolls.

## How it Works

## Files

# Contact

Nolan Winsman - [@Github](https://github.com/nolanwinsman) - nolanwinsman@gmail.com

Project Link: [https://github.com/nolanwinsman/ArchNolan](https://github.com/nolanwinsman/ArchNolan)

# Contributers

- nolanwinsman