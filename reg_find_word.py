import re

handle = open("romeo.txt")
for line in handle:
    line = line.rstrip()
    # line = line.split()  # TypeError: expected string or bytes-like object
    if re.search("the ", line):
        print(line)


