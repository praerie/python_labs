import os
import time
import random

DATASET_DIR = "datasets"  # folder where datasets are stored

SIZES = ["small", "medium", "large", "very_large"]  # different dataset sizes to test with

# number of keys to search for in each test
LOOKUPS_PER_SET = 100

# load dataset from text file and convert to list of ints
def load_dataset(filename):
    path = os.path.join(DATASET_DIR, filename + ".txt")
    with open(path, "r") as f:
        return list(map(int, f.read().split()))

# perform hash-based searching using a dictionary (hash table)
def hash_search(data, keys):
    hash_table = {val: True for val in data}            # build hash table from dataset
    return sum(1 for key in keys if key in hash_table)  # count how many keys are found

def main():
    for size in SIZES:
        filename = f"{size}_random"
        data = load_dataset(filename)

        # pick half the keys from inside the dataset (guaranteed hits)
        sample_keys = random.sample(data, min(LOOKUPS_PER_SET // 2, len(data)))

        # generate half the keys from values outside the dataset range (likely misses!)
        miss_keys = [random.randint(max(data)+1, max(data)+1000) for _ in range(LOOKUPS_PER_SET // 2)]

        # combine both into a single lookup list
        search_keys = sample_keys + miss_keys

        # measure how long the hash-based search takes
        start = time.perf_counter()
        found = hash_search(data, search_keys)
        end = time.perf_counter()

        # print the results: how many were found + how long it took
        print(f"{filename:<20} | Found: {found:>3}/{LOOKUPS_PER_SET} | Time: {end - start:.6f} sec")

if __name__ == "__main__":
    main()
