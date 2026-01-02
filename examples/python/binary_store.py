import struct, json

BIN_PATH = "binary/store.bin"

def write_record(record):
    raw = json.dumps(record).encode("utf-8")
    with open(BIN_PATH, "ab") as f:
        f.write(struct.pack(">I", len(raw)))
        f.write(raw)

def read_records():
    records = []
    with open(BIN_PATH, "rb") as f:
        while True:
            size = f.read(4)
            if not size:
                break
            length = struct.unpack(">I", size)[0]
            data = f.read(length)
            records.append(json.loads(data))
    return records
