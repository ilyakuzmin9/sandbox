import random
import csv

def generate_mac():
    # Generate a random 6-byte MAC address in hexadecimal format
    mac_bytes = [random.randint(0x00, 0xff) for i in range(6)]
    mac_hex = ":".join("{:02x}".format(b) for b in mac_bytes)
    return mac_hex

def generate_mac_list(n):
    # Generate a list of n random MAC addresses
    mac_list = [generate_mac() for i in range(n)]
    return mac_list

def write_list_to_csv(a_filename, a_my_list,a_header=None):
    # Open the CSV file for writing
    with open(a_filename, "w", newline="") as file:
        writer = csv.writer(file)
        if a_header:
            writer.writerow(a_header)
        # Write each element of the list to a separate row in the CSV file
        for element in a_my_list:
            writer.writerow([element])
    print("List written to CSV file successfully.")

