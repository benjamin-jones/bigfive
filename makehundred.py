#!/usr/bin/env python

# This function increments a trinary vector using a simple
# carry propgation algorithm 
def trinary_inc(number):
    # Start in the 1s column and work your way down
    base_vec = [1,0,0,0,0,0,0,0]
    carry = 0
    for i,(digit,base) in enumerate(zip(number,base_vec)):
        # We've overflowed, set the carry,
        # reset the digit and continue
        if digit+base+carry == 3:
            carry = 1
            number[i] = 0
            continue
        # Otherwse, just add the corresponding digits
        # and reset the carry
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

# This function applies a set of operations on the base vector
# by building the string of operations and then abusing
# python to directly evaluate the expression
def apply_operation(operation, base_vector):
    eval_string = ""
    my_operation = operation

    # Iterate over each number in the base vector
    for i in base_vector:

        # Concat the next number
        eval_string = eval_string + str(i)

        # Sanity check on the remaining operations
        if my_operation:
            # grab the next operation
            op = my_operation[0]
            my_operation = my_operation[1:]
        else:
            continue

        # Arbitrarity, 0 ~= +, 1 ~= -, 2 ~= concat
        if op == 0:
            eval_string = eval_string + "+"
        if op == 1:
            eval_string = eval_string + "-"
        # No need to do 2, because it will happen in the
        # next loop iteration

    # Abusing python to directly evaluate the expression >:)
    return eval(eval_string), eval_string 

def main():
    
    # There are three operations, so we treat the operations vector as a trinary number
    operation = [0,0,0,0,0,0,0,0]

    # Our vector of [1...9]
    base_vector = range(1,10)

    # Since there are only 3**8 possible cominations, just brute force it
    for i in range(3**8):
        # Here we try to apply a possibe combination of operations on the base vector
        # and measure the result
        trial, string = apply_operation(operation, base_vector)

        # Check if the trial succeeds
        if trial == 100:
            print("%s = 100" % string)

        # Generate another candidate set of operations
        operation = trinary_inc(operation)

main()
