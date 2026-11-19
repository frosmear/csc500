#!/usr/bin/env python3
"""Day 5 - Capstone Part 5
Convert IP addresses, calculate network addresses, and display results.
"""

import sys

# Part A - Convert IP address to integer
def make_ip_num(ip_str):
    ip_num = int.from_bytes(
        bytes(int(octet) for octet in ip_str.split(".")),
        byteorder="big"
    )
    return ip_num


# Part B - Calculate network ID, first, last, and broadcast addresses
def calculate(ip_str, cidr):
    ip_integer = make_ip_num(ip_str)

    host_bits = 32 - cidr
    host_mask = (1 << host_bits) - 1
    network_mask = (0xFFFFFFFF << host_bits) & 0xFFFFFFFF

    network_id = ip_integer & network_mask
    broadcast = network_id | host_mask
    first = network_id + 1
    last = broadcast - 1

    return ip_integer, network_id, first, last, broadcast


# Part C - Convert integer to IP address string
def make_ip_str(ip_num):
    """Convert an integer IP address to dotted-decimal notation."""
    octets = []

    for shift in (24, 16, 8, 0):
        octets.append(str((ip_num >> shift) & 0xFF))

    ip_str = ".".join(octets)
    return ip_str


# Part D - Display IP address and network information
def pretty_print(my_tuple):
    """Display IP and network information from a five-integer tuple."""
    labels = (
        "Integer Value:",
        "Network ID:",
        "First Address:",
        "Last Address:",
        "Broadcast:"
    )

    print()

    for label, ip_num in zip(labels, my_tuple):
        ip_str = make_ip_str(ip_num)
        print(f"{label:<17} {str(ip_num)} ({ip_str})")


# Validate IPv4 address
def validate_ip(ip_address):
    octets = ip_address.split(".")

    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit():
            return False

        if not 0 <= int(octet) <= 255:
            return False

    return True


# Display IP address and network information
def display_ip_info(ip_address, cidr):
    my_tuple = calculate(ip_address, cidr)

    print(f"\nIP Address: {ip_address}/{cidr}")
    pretty_print(my_tuple)


# Get and validate command-line arguments
def get_arguments():
    if len(sys.argv) == 1:
        print("\nUsage:")
        print(f"  python3 {sys.argv[0]} <IPv4 address> <CIDR>")
        print("\nExamples:")
        print(f"  python3 {sys.argv[0]} 192.168.30.125 24")
        print("\nProvide an IPv4 address and CIDR as command-line arguments.")
        return None

    if len(sys.argv) != 3:
        print("\nError: Exactly two arguments are required.")
        print("Expected: <IPv4 address> <CIDR>")
        print(f"Example: python3 {sys.argv[0]} 192.168.30.125 24")
        return None

    ip_address = sys.argv[1]
    cidr_string = sys.argv[2]

    # Validate IPv4 address
    if not validate_ip(ip_address):
        print(f"\nError: '{ip_address}' is not a valid IPv4 address.")
        print("Expected format: xxx.xxx.xxx.xxx")
        print("Each octet must be an integer from 0 through 255.")
        return None

    # Validate CIDR
    try:
        cidr = int(cidr_string)
    except ValueError:
        print(f"\nError: '{cidr_string}' is not a valid CIDR value.")
        print("CIDR must be an integer from 0 through 32.")
        return None

    if not 0 <= cidr <= 32:
        print(f"\nError: CIDR value '{cidr}' is outside the valid range.")
        print("CIDR must be an integer from 0 through 32.")
        return None

    return ip_address, cidr


# Main program
def main():
    arguments = get_arguments()

    if arguments is None:
        return

    ip_address, cidr = arguments

    display_ip_info(ip_address, cidr)

    # I like whitespace before the linux prompt
    print()


if __name__ == "__main__":
    main()

