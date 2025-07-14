import random
import string

def generate_email():
    domains = ["duckduckgo.com", "boggle.com", "aol.net", "marketers.org"]
    name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
    domain = random.choice(domains)
    return f"{name}@{domain}"

def create_email_dataset(size, overlap=0):
    shared = {generate_email() for _ in range(overlap)}
    list1 = shared.union({generate_email() for _ in range(size - overlap)})
    list2 = shared.union({generate_email() for _ in range(size - overlap)})
    return list1, list2

emails1, emails2 = create_email_dataset(1000, overlap=200)