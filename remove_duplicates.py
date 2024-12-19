import os
import hashlib

def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()  # Calculates file hash

def find_duplicates(folder):
    hashes = {}
    duplicates = []
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            h = file_hash(path)
            if h in hashes:
                print(f"Duplicate: {path} is a duplicate of {hashes[h]}")
                duplicates.append(path)
            else:
                hashes[h] = path
    return duplicates

def remove_duplicates(duplicates):
    for file in duplicates:
        os.remove(file)
        print(f"Deleted: {file}")

if __name__ == "__main__":
    folder_path = r"C:\Users\MELVIN\Desktop\internpulse\Portfolio\design\static"
    print(f"Scanning folder: {folder_path}")
    duplicates = find_duplicates(folder_path)
    remove_duplicates(duplicates)
    print(f"Duplicate removal complete! {len(duplicates)} files removed.")
    
    
    
def find_duplicates(folder):
    hashes = {}
    duplicates = []
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            h = file_hash(path)
            print(f"Hash of {file}: {h}")  # Debugging line to print file hashes
            if h in hashes:
                print(f"Duplicate: {path} is a duplicate of {hashes[h]}")
                duplicates.append(path)
            else:
                hashes[h] = path
    return duplicates

