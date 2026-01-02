from examples.python.gpfdb import GPFDB
import json

db = GPFDB()

spec = json.load(open("tests/spec_test.json"))

ids = []
for item in spec["insert"]:
    ids.append(db.insert(item["type"], item["data"]))

# range test (manual)
res1 = [d["_id"] for d in db.find_eq("name","Alice")]
assert res1 == spec["queries"][1]["expect_ids"]

print("PYTHON PORT: OK")
