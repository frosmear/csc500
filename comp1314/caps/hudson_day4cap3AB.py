#!/usr/bin/env python3
"""Day 4 - Capstone Part 3AB
Convert IP addresses to integers and calculate network addresses.
"""

# Hardcoded IP address from example
hardcoded_ip_address = "192.168.30.125"
hardcoded_cidr = 24

# Part A - Convert IP address to an integer
def make_ip_num(ip_str):
    ip_num = int.from_bytes(
        bytes(int(octet) for octet in ip_str.split(".")),
        byteorder="big"
    )
    return ip_num

# Part B - Calculate network ID, first, last, and broadcast addresses
def calculate(ip_str, cidr):
    IPaddress = make_ip_num(ip_str)

    host_bits = 32 - cidr
    host_mask = (1 << host_bits) - 1
    network_mask = (0xFFFFFFFF << host_bits) & 0xFFFFFFFF

    NetworkID = IPaddress & network_mask
    Broadcast = NetworkID | host_mask
    Firsthost = NetworkID + 1
    Lasthost = Broadcast - 1

    return IPaddress, NetworkID, Firsthost, Lasthost, Broadcast

# Convert integer to IP address string
def convertInt2IP(ip_integer):
    return ".".join(
        str((ip_integer >> shift) & 0xFF)
        for shift in (24, 16, 8, 0)
    )

# Display IP address and network information
def printIPInfo(ip_address, cidr):
    ip_integer, network_id, first, last, broadcast = calculate(
        ip_address, cidr
    )

    print()
    print(f"IP Address:       {ip_address}/{cidr}")
    print(f"Integer Value:    {ip_integer} ({ip_address})")
    print(f"Network ID:       {network_id} ({convertInt2IP(network_id)})")
    print(f"First Address:    {first} ({convertInt2IP(first)})")
    print(f"Last Address:     {last} ({convertInt2IP(last)})")
    print(f"Broadcast:        {broadcast} ({convertInt2IP(broadcast)})")

# Main program
def main():
    # Display the hardcoded integer value and network information
    print()
    print("Example address from assignment")
    printIPInfo(hardcoded_ip_address, hardcoded_cidr)

    # I like whitespace before the prompt
    print()

if __name__ == "__main__":
    main()

