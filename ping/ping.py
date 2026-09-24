import subprocess

print("=" * 60)
print("NETWORK PING TEST")
print("=" * 60)

address = input("\nEnter IP address or hostname: ").strip()

if not address:
    print("No address entered.")
    input("\nPress ENTER to close...")
    exit()

print(f"\nTesting connectivity to: {address}")
print("-" * 60)

try:
    result = subprocess.run(
        ["ping", "-n", "4", address],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    print(result.stdout)

    if result.returncode == 0:
        print("RESULT: Host is reachable.")
    else:
        print("RESULT: No response from host.")
        print("Possible reasons:")
        print("- Host is offline")
        print("- No route to destination")
        print("- Firewall is blocking ICMP/Ping")
        print("- Incorrect IP address or hostname")

except Exception as e:
    print(f"Error running ping: {e}")

input("\nPress ENTER to close...")