#!/usr/bin/env python

def sum_for(num):
    accum = 0
    for i in num:
        accum = accum + i

    return accum

def sum_while(num):
    #note: this is quite unpythonic
    accum = 0
    my_list = num
    while len(my_list) > 0:
        i = my_list[0]
        accum = accum + i
        my_list = my_list[1:]
    return accum    

def sum_recursive(num):
    if not num:
        return 0
    head, tail = num[0], num[1:]
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
