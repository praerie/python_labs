import random

def generate_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def create_ip_dataset(size, overlap=0):
    shared = {generate_ip() for _ in range(overlap)}
    log1 = shared.union({generate_ip() for _ in range(size - overlap)})
    log2 = shared.union({generate_ip() for _ in range(size - overlap)})
    return log1, log2

ips1, ips2 = create_ip_dataset(1000, overlap=300)