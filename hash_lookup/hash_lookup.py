import os
import time
import random
from collections import defaultdict

DATASET_DIR = "datasets"  # folder containing your generated datasets
SIZES = ["small", "medium", "large", "very_large"]
LOOKUPS_PER_SET = 100  # number of keys to search for in each test

# load the dataset from file and return it as a list of ints
def load_dataset(filename):
    path = os.path.join(DATASET_DIR, filename + ".txt")
    with open(path, "r") as f:
        return list(map(int, f.read().split()))

# linear search: check each element one-by-one (O(n))
def linear_search(data, keys):
    return sum(1 for key in keys if key in data)

# binary search: assumes sorted input (O(log n))
def binary_search(sorted_data, keys):
    def bin_search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
    return sum(1 for key in keys if bin_search(sorted_data, key))

# custom hash table using separate chaining (lists to handle collisions)
class CustomHashTable:
    def __init__(self, size=1000):
        self.size = size
        self.table = defaultdict(list)

    def _hash(self, key):
        return key % self.size  # simple modulo hash function

    def insert(self, key):
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def search(self, key):
        index = self._hash(key)
        return key in self.table[index]

# insert all data into hash table and search keys
def custom_hash_search(data, keys):
    ht = CustomHashTable(size=len(data) // 2)  # use load factor of ~2.0
    for val in data:
        ht.insert(val)
    return sum(1 for key in keys if ht.search(key))

def main():
    for size in SIZES:
        filename = f"{size}_random"
        data = load_dataset(filename)

        # pick 50 keys from the dataset and 50 likely-missing keys
        sample_keys = random.sample(data, min(LOOKUPS_PER_SET // 2, len(data)))
        miss_keys = [random.randint(max(data)+1, max(data)+1000) for _ in range(LOOKUPS_PER_SET // 2)]
        search_keys = sample_keys + miss_keys

        print(f"\nDataset: {filename}")

        # linear search
        start = time.perf_counter()
        found_linear = linear_search(data, search_keys)
        linear_time = time.perf_counter() - start
        print(f"  Linear Search:   {found_linear}/100 found in {linear_time:.6f} sec")

        # binary search (requires sorting)
        sorted_data = sorted(data)
        start = time.perf_counter()
        found_binary = binary_search(sorted_data, search_keys)
        binary_time = time.perf_counter() - start
        print(f"  Binary Search:   {found_binary}/100 found in {binary_time:.6f} sec")

        # custom hash table search
        start = time.perf_counter()
        found_hash = custom_hash_search(data, search_keys)
        hash_time = time.perf_counter() - start
        print(f"  Hash Table (Custom): {found_hash}/100 found in {hash_time:.6f} sec")

if __name__ == "__main__":
    main()
