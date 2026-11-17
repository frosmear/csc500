#!/usr/bin/env python3
"""Day 4 - Capstone Part 4
Convert IP addresses, calculate network addresses, and display results.
"""

import socket

# Hardcoded IP address from example
hardcoded_ip_address = "192.168.30.125"
hardcoded_cidr = 24

# Part A - Convert IP address to integer
def convertIP2int(ipstring):
    ip_integer = int.from_bytes(
        bytes(int(octet) for octet in ipstring.split(".")),
        byteorder="big"
    )
    return ip_integer


# Part B - Calculate network ID, first, last, and broadcast addresses
def calculate(ip_integer, cidr):
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
    ip_str = socket.inet_ntoa(ip_num.to_bytes(4, byteorder="big"))
    return ip_str


# Part D - Display IP address and network information
def pretty_print(my_tuple):
    """Display IP and network information from a five-integer tuple."""
    ip_integer, network_id, first, last, broadcast = my_tuple

    labels = (
        "Integer Value:",
        "Network ID:",
        "First Address:",
        "Last Address:",
        "Broadcast:"
    )

    print()

    for label, ip_num in zip(labels, my_tuple):
        print(f"{label:<17} {str(ip_num)} ({make_ip_str(ip_num)})")


# Determine local machine IP addresses
def getLocalIPs():
    local_ips = set()
    hostname = socket.gethostname()

    try:
        for result in socket.getaddrinfo(hostname, None, socket.AF_INET):
            ip_address = result[4][0]
            if not ip_address.startswith("127."):
                local_ips.add(ip_address)
    except socket.gaierror:
        pass

    return sorted(local_ips)


# Display IP address and network information
def display_ip_info(ip_address, cidr):
    ip_integer = convertIP2int(ip_address)
    my_tuple = calculate(ip_integer, cidr)

    print(f"\nIP Address: {ip_address}/{cidr}")
    pretty_print(my_tuple)


# Main program
def main():

    # Display example address from assignment
    print()
    print("Example address from assignment")
    display_ip_info(hardcoded_ip_address, hardcoded_cidr)

    # Display local machine IP addresses and network information
    print()
    print("Local Machine IP Addresses")

    for ip_address in getLocalIPs():
        display_ip_info(ip_address, hardcoded_cidr)

    # I like whitespace before the linux prompt
    print()


if __name__ == "__main__":
    main()

