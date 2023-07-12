#!/usr/bin/python3
def print_list_integer(my_list=[]):
    seen_nums = set()
    for num in my_list:
        if num not in seen_nums:
            print("{:d}".format(num))
            seen_nums.add(num)
my_list = [1, 2, 3]
print_list_integer(my_list)
