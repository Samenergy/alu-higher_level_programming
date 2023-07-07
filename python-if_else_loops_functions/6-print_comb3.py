#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == 0:
            print("{:01d}, ".format(j), end="")
        else:
            print("{:01d}{:01d}, ".format(i, j), end="")
print()
