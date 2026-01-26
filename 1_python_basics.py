# importing library to support generation of random numbers
import random

try:

    # 1 create list of 100 random numbers from 0 to 1000

    # init list variable
    list_a = []

    # in loop populate list using range() for counter, append to add list element, [counter] randinit + to init element
    for i in range(100):
        list_a.append(i)
        list_a[i] = random.randint(0, 1000)

    #print(list_a)

    # 2 sort list from min to max (without using sort())
    # will be bubbling

    # get length of a list
    len_list_a = len(list_a)

    # for each element
    for i in range(len_list_a):
        # for unsorted elements
        for j in range(0, len_list_a - i - 1):
            # swap if bigger
            if list_a[j] > list_a[j + 1]:
                # internet says like this
                # list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
                # but i'll go with syntax i know for now
                tmp = list_a[j]
                list_a[j] = list_a[j + 1]
                list_a[j + 1] = tmp

    #print(list_a)

    # 3 calculate average for even and odd numbers

    # init totals and counters
    even_total = 0
    even_count = 0
    odd_total = 0
    odd_count = 0

    # in loop
    for i in range(len_list_a):
        # if divides by 2 without remainder, then count as even into total and counter
        if list_a[i] % 2 == 0:
            even_total = even_total + list_a[i]
            even_count = even_count + 1
        # otherwise as odd
        else:
            odd_total = odd_total + list_a[i]
            odd_count = odd_count + 1

    # 4 print both average result in console
    print("Average for even = " + str(even_total/even_count))
    print("Average for odd = " + str(odd_total/odd_count))

except ZeroDivisionError:
    print("ZeroDivisionError occured")
