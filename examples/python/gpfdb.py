import json, os, time, re
from collections import defaultdict

# ---------- Utilities ----------

def load(path, default):
    if not os.path.exists(path):
        return default
    with open(path) as f:
        return json.load(f)

def save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def tokenize(text):
    return set(re.findall(r"[a-z]+", text.lower()))

# ---------- Engine ----------

class GPFDB:
    def __init__(self, root="format"):
        self.store_path = f"{root}/store.json"
        self.idx_field_path = f"{root}/idx_field.json"
        self.idx_text_path = f"{root}/idx_text.json"

        self.store = load(self.store_path, {"meta": {"version":1,"last_id":0},"docs":[]})
        self.idx_field = load(self.idx_field_path, {})
        self.idx_text = load(self.idx_text_path, {})

    # ---------- Insert ----------
    def insert(self, doc_type, data):
        self.store["meta"]["last_id"] += 1
        _id = self.store["meta"]["last_id"]

        doc = {
            "_id": _id,
            "_type": doc_type,
            "_created": int(time.time()),
            "_updated": int(time.time()),
            "data": data
        }

        self.store["docs"].append(doc)

        # field index
        for k, v in data.items():
            key = f"{k}:{v}"
            self.idx_field.setdefault(key, []).append(_id)

        # full-text index
        text = json.dumps(data)
        for token in tokenize(text):
            self.idx_text.setdefault(token, []).append(_id)

        self.flush()
        return _id

    # ---------- Query ----------
    def find_eq(self, field, value):
        key = f"{field}:{value}"
        ids = self.idx_field.get(key, [])
        return [d for d in self.store["docs"] if d["_id"] in ids]

    def search_text(self, word):
        ids = self.idx_text.get(word.lower(), [])
        return [d for d in self.store["docs"] if d["_id"] in ids]

    # ---------- Persistence ----------
    def flush(self):
        save(self.store_path, self.store)
        save(self.idx_field_path, self.idx_field)
        save(self.idx_text_path, self.idx_text)

