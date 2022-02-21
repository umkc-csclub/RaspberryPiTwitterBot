import json, random


def get_message(message_db="messages.json", used_db="used.txt"):
    with open(message_db) as f:
        messages = json.load(f)

    with open(used_db) as f:
        used = {int(i) for i in f}

    options = list(set(range(len(messages))) - used)

    pick_ix = random.choice(options)

    with open(used_db, "a") as f:
        f.write(f"{pick_ix}\n")

    return messages[pick_ix]
