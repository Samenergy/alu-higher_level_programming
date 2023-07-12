#!/usr/bin/python3
def print_list_integer(my_list=[]):
    unique_nums = set(my_list)
    for num in unique_nums:
        print("{:d}".format(num))
my_list = [1, 2, 3, 4, 5, 1, 2, 3]
print_list_integer(my_list)
