import time
from examples.python.gpfdb import GPFDB

db = GPFDB()

N = 5000
start = time.time()

for i in range(N):
    db.insert("bench", {
        "name": f"user{i}",
        "age": i % 50,
        "status": "active" if i % 2 == 0 else "inactive"
    })

end = time.time()

print("Inserted:", N)
print("Time:", round(end - start, 3), "seconds")
print("Ops/sec:", int(N / (end - start)))
