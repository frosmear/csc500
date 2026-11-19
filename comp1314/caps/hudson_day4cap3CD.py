#!/usr/bin/env python3
"""Day 4 - Capstone Part 3 A-D
Convert IP addresses, calculate network addresses, and display results.
"""

# Hardcoded IP address from example
hardcoded_ip_address = "192.168.30.125"
hardcoded_cidr = 24

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
    ip_str = ".".join(
        str((ip_num >> shift) & 0xFF)
        for shift in (24, 16, 8, 0)
    )
    return ip_str


# Part D - Display IP address and network information
def pretty_print(my_tuple):
    """Display IP and network information from a five-integer tuple."""
    ip_integer, network_id, first, last, broadcast = my_tuple

    ip_str = str(make_ip_str(ip_integer))
    network_str = str(make_ip_str(network_id))
    first_str = str(make_ip_str(first))
    last_str = str(make_ip_str(last))
    broadcast_str = str(make_ip_str(broadcast))

    print()
    print(f"Integer Value:    {str(ip_integer)} ({ip_str})")
    print(f"Network ID:       {str(network_id)} ({network_str})")
    print(f"First Address:    {str(first)} ({first_str})")
    print(f"Last Address:     {str(last)} ({last_str})")
    print(f"Broadcast:        {str(broadcast)} ({broadcast_str})")


# Main program
def main():

    # Display example address from assignment
    print()
    print("Example address from assignment")

    ip_integer = make_ip_num(hardcoded_ip_address)
    ip_str = make_ip_str(ip_integer)
    my_tuple = calculate(hardcoded_ip_address, hardcoded_cidr)
    status = pretty_print(my_tuple)

    # I like whitespace before the prompt
    print()


if __name__ == "__main__":
    main()

