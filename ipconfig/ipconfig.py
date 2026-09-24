import subprocess

print("=" * 70)
print("IPCONFIG /ALL - NETWORK INFORMATION")
print("=" * 70)

try:
    result = subprocess.run(
        ["ipconfig", "/all"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    print(result.stdout)

except Exception as e:
    print(f"Error running ipconfig: {e}")

print("\n" + "=" * 70)
print("NETWORK INFORMATION EXPLANATION")
print("=" * 70)

print("""
IPv4 Address
    The IP address assigned to the network interface.

Subnet Mask
    Defines the network and host portions of the IPv4 address.

Default Gateway
    The router used to reach other networks and the Internet.

DNS Servers
    Servers used to translate domain names into IP addresses.

DHCP
    Determines whether the IP configuration is assigned automatically.

Physical Address
    The MAC address of the network interface.

Adapter
    A physical or virtual network interface such as Ethernet,
    Wi-Fi, VMware, VPN or other virtual adapters.
""")

input("\nPress ENTER to close...")