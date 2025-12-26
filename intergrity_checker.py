
import hashlib
import os

def calculate_hash(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

file_name = "sample.txt.txt"
hash_file = "hash.txt"

current_hash = calculate_hash(file_name)

if not os.path.exists(hash_file):
    # First run – store hash
    with open(hash_file, "w") as f:
        f.write(current_hash)
    print("Hash stored successfully.")
    print("File integrity baseline created.")
else:
    # Next runs – verify integrity
    with open(hash_file, "r") as f:
        old_hash = f.read()

    if current_hash == old_hash:
        print("File integrity maintained ✅")
    else:
        print("File integrity violated ❌")
