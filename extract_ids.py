import re
import os

print("Extracting SteamID from voice_ban.dt\n")
print("Drag the file into this window and press Enter.")
file_path = input("File path: ").strip()
file_path = file_path.strip('"')
if not os.path.exists(file_path):
    print("\nError! Try again.")
    input("\nPress ENTER to exit.")
    exit()
with open(file_path, "r") as file:
    inside = file.read()
ids = re.findall(r"steamid = (\d+)", inside)
if len(ids) == 0:
    print("\nIDs not found! Check the file.")
    input("\nPress ENTER to exit.")
    exit()
print(f"Found {len(ids)} IDs:\n")
for id in ids:
    print(id)
input("\nPress ENTER to exit.")
