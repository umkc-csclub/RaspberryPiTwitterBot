import json
import random


def get_message(message_db="messages.json", used_db="used.txt"):
    try:
        with open(used_db) as f:
            used = {int(i) for i in f}
    except FileNotFoundError:
        used = set()
    
    with open(message_db) as f:
        messages = {ix: line for (ix, line) in enumerate(json.load(f)) if ix not in used}

    pick_ix = random.choice(list(messages.keys()))

    with open(used_db, "a+") as f:
        f.write(f"{pick_ix}\n")

    return messages[pick_ix]
