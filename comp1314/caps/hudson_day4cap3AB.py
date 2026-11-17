#!/usr/bin/env python3
"""Day 4 - Capstone Part 3AB
Convert IP addresses to integers and calculate network addresses.
"""

import socket

# Hardcoded IP address from example
hardcoded_ip_address = "192.168.30.125"
hardcoded_cidr = 24

# Part A - Convert IP address to an integer
def convertIP2int(ipstring):
    ip_integer = int.from_bytes(
        bytes(int(octet) for octet in ipstring.split(".")),
        byteorder="big"
    )
    return ip_integer

# Part B - Calculate network ID, first, last, and broadcast addresses
def calculateNetwork(ip_integer, cidr):
    host_bits = 32 - cidr
    host_mask = (1 << host_bits) - 1
    network_mask = (0xFFFFFFFF << host_bits) & 0xFFFFFFFF

    network_id = ip_integer & network_mask
    broadcast = network_id | host_mask
    first = network_id + 1
    last = broadcast - 1

    return network_id, first, last, broadcast

# Convert integer to IP address string
def convertInt2IP(ip_integer):
    return socket.inet_ntoa(ip_integer.to_bytes(4, byteorder="big"))

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
def printIPInfo(ip_address, cidr):
    ip_integer = convertIP2int(ip_address)

    network_id, first, last, broadcast = calculateNetwork(
        ip_integer, cidr
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

    # Display local machine IP addresses and network information
    print()
    print("Local Machine IP Addresses")

    for ip_address in getLocalIPs():
        printIPInfo(ip_address, hardcoded_cidr)

    # I like whitespace before the linux prompt
    print()

if __name__ == "__main__":
    main()

