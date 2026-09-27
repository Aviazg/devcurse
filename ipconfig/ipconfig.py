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
test 5
""")

input("\nPress ENTER to close...")