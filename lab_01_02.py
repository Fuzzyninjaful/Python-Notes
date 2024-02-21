"""
Lab 01.02 - Sorting Files
"""
from prelude import clear

clear()

FILENAME = "students.txt"
with open(FILENAME, encoding = "utf8") as infile:
    names = infile.readlines()

print(f"Original order: {names}")

with open(FILENAME, mode = "w", encoding = "utf8") as outfile:
    sorted_names = sorted(names)
    outfile.writelines(sorted_names)

print(f"Sorted Order: {sorted_names}")
