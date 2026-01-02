import bisect, json, os

class RangeIndex:
    def __init__(self, path="format/idx_range.json"):
        self.path = path
        self.data = self._load()

    def _load(self):
        if not os.path.exists(self.path):
            return {}
        with open(self.path) as f:
            return json.load(f)

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)

    def insert(self, field, value, doc_id):
        field = str(field)
        value = str(value)
        self.data.setdefault(field, {})
        self.data[field].setdefault(value, [])
        self.data[field][value].append(doc_id)
        self.save()

    def query_gt(self, field, value):
        field = str(field)
        value = str(value)
        if field not in self.data:
            return []
        keys = sorted(self.data[field].keys(), key=float)
        idx = bisect.bisect_right(keys, value)
        result = []
        for k in keys[idx:]:
            result.extend(self.data[field][k])
        return result
