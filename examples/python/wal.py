import json, os

WAL_PATH = "wal/wal.log"

def wal_append(entry):
    with open(WAL_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")

def wal_read():
    if not os.path.exists(WAL_PATH):
        return []
    with open(WAL_PATH) as f:
        return [json.loads(line) for line in f]

def wal_clear():
    open(WAL_PATH, "w").close()
