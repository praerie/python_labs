from email_addresses.generate_emails import emails1, emails2
from ip_addresses.generate_ips import ips1, ips2

def main():
    print("\nPart A: Email Addresses - Set Operations\n")

    # Union
    all_emails = emails1.union(emails2)
    print(f"Union: {len(all_emails)} total unique email addresses")

    # Intersection
    common_emails = emails1.intersection(emails2)
    print(f"Intersection: {len(common_emails)} common email addresses between the two lists")

    # Difference (emails unique to list 1)
    unique_to_list1 = emails1.difference(emails2)
    print(f"Difference #1: {len(unique_to_list1)} email addresses unique to list 1")

    # Difference (emails unique to list 2)
    unique_to_list2 = emails2.difference(emails1)
    print(f"Difference #2: {len(unique_to_list2)} email addresses unique to list 2")

    # Symmetric Difference
    emails_only_one = emails1.symmetric_difference(emails2)
    print(f"Symmetric Difference: {len(emails_only_one)} email addresses unique to either list")

    print("\nPart B: IP Addresses - Set Operations\n")

    # Union
    all_ips = ips1.union(ips2)
    print(f"Union: {len(all_ips)} total unique IP addresses")

    # Intersection
    common_ips = ips1.intersection(ips2)
    print(f"Intersection: {len(common_ips)} IP addresses found in both logs")

    # Difference (IPs unique to log 1)
    unique_to_log1 = ips1.difference(ips2)
    print(f"Difference #1: {len(unique_to_log1)} IP addresses unique to log 1")

    # Difference (IPs unique to log 2)
    unique_to_log2 = ips2.difference(ips1)
    print(f"Difference #2: {len(unique_to_log2)} IP addresses unique to log 2")

    # Symmetric Difference
    ips_only_one = ips1.symmetric_difference(ips2)
    print(f"Symmetric Difference: {len(ips_only_one)} IP addresses found in only one log\n")

if __name__ == "__main__":
    main()
