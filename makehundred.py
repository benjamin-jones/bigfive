#!/usr/bin/env python

def trinary_inc(number):
    base_vec = [1,0,0,0,0,0,0,0]
    carry = 0
    for i,(digit,base) in enumerate(zip(number,base_vec)):
        if digit+base+carry == 3:
            carry = 1
            number[i] = 0
            continue
        if digit+base+carry == 2:
            carry = 0
            number[i] = 2
            continue
        if digit+base+carry == 1:
            carry = 0
            number[i] = 1
            continue
        if digit+base+carry == 0:
            carry = 0
            number[i] = 0
            continue
    return number 
def apply_operation(operation, base_vector):
    accum = 0
    eval_string = ""
    my_operation = operation
    for i in base_vector:
        eval_string = eval_string + str(i)
        if my_operation:
            op = my_operation[0]
            my_operation = my_operation[1:]
        else:
            continue
        if op == 0:
            eval_string = eval_string + "+"
        if op == 1:
            eval_string = eval_string + "-"

    return eval(eval_string), eval_string 

def main():
    operation = [0,0,0,0,0,0,0,0]
    base_vector = range(1,10)
    for i in range(3**8):
        trial, string = apply_operation(operation, base_vector)

        if trial == 100:
            print("%s = 100" % string)
        operation = trinary_inc(operation)

main()
