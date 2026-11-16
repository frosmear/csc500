#!/usr/bin/env python3
"""Day 2 - Capstone Part 1
Convert an IP address from a string to an integer.
"""

import socket

# Hardcoded IP address fromn example
hardcoded_ip_address = "192.168.30.125"

# Convert IP address to an integer function
def convertIP2int(ipstring):
    ip_integer = int.from_bytes(
        bytes(int(octet) for octet in ipstring.split(".")),
        byteorder="big"
    )
    return ip_integer

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

# Display the hardcoded integer value
print()
print("Example address from assignment")
print(f"Hardcoded IP Address: {hardcoded_ip_address}")
print(f"Integer Value: {convertIP2int(hardcoded_ip_address)}")

# Display local machine IP addresses and integer values
print("\nLocal Machine IP Addresses:")

for ip_address in getLocalIPs():
    print(f"IP Address: {ip_address}")
    print(f"Integer Value: {convertIP2int(ip_address)}")
