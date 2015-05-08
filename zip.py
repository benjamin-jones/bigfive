#!/usr/bin/env python


def main():

    my_list = []
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    
    for i,j in zip(list2,list1):
        my_list.append(i)
        my_list.append(j)
    print(my_list)

main()
