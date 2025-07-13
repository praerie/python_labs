import os
import random

# sizes of datasets to generate
DATASET_SIZES = {
    "small": 100,
    "medium": 1_000,
    "large": 10_000,
    "very_large": 100_000
}

OUTPUT_DIR = "datasets"  # folder where the datasets will be saved

# generate a list of unique random integers for a given size
def generate_data(size):
    return random.sample(range(size * 10), size)  # ensures no duplicates

# save the dataset to a text file, space-separated
def save_dataset(data, name):
    os.makedirs(OUTPUT_DIR, exist_ok=True)  # create output folder if needed
    path = os.path.join(OUTPUT_DIR, name + ".txt")
    with open(path, "w") as f:
        f.write(" ".join(map(str, data)))   # convert ints to strings before saving

def main():
    for label, size in DATASET_SIZES.items():
        data = generate_data(size)              # generate random dataset
        save_dataset(data, f"{label}_random")   # save with descriptive filename
        print(f"Saved: {label}_random.txt")     # print confirmation

if __name__ == "__main__":
    main()
