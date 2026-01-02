import time
from examples.python.gpfdb import GPFDB

db = GPFDB()

start = time.time()
res = db.find_eq("status", "active")
end = time.time()

print("Results:", len(res))
print("Search time:", round(end - start, 6), "seconds")
