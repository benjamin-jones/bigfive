#!/usr/bin/env python

def sum_for(num):
    accum = 0

    # Obvious naive for loop summation
    for i in num:
        accum = accum + i

    return accum

def sum_while(num):
    #note: this is quite unpythonic
    accum = 0
    my_list = num

    # Essentially we're just doing the recusrive algorithm with
    # a while loop:
    #   -  Get the head of the list
    #   -  Add the head of the list to the accumulator
    #   -  Mutate the list to be only the tail
    #   -  Iterate
    while len(my_list) > 0:
        i = my_list[0]
        accum = accum + i
        my_list = my_list[1:]
    return accum    

def sum_recursive(num):
    # Our stopping condition is an empty list
    if not num:
        # Use the empty list condition to seed the accumulator with zero
        return 0
    # Get the head and the tail
    head, tail = num[0], num[1:]

    # Add the head to the recursive sum of the tail
    return head + sum_recursive(tail)

def main():
    my_list = [1, 2, 3, 4,5]
    answer = sum(my_list)

    if answer != sum_for(my_list) or answer != sum_while(my_list) or answer != sum_recursive(my_list):
        print("Incorrect implementation for:%d while:%d recur:%d" %(sum_for(my_list), sum_while(my_list), sum_recursive(my_list)))
        exit(0)

    print("PASS")
    exit(0)

main()
