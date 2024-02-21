"""
Lab 01.01 - Files and Lists
"""

from prelude import clear

clear()

with open("names.txt", encoding= "utf8") as file:
    names: list[str] = [line.rstrip("\n") for line in file.readlines()]

longest_name = max(names, key = len)
shortest_name = min(names, key = len)

print(f"Longest name is: {longest_name}")
print(f"Shortest name is: {shortest_name}")
