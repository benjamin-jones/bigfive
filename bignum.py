#!/usr/bin/env python

# This class wraps up an integer and overrides the '<'
# operator so that we can sort on the criteria that 
# matters for the exercise, namely the most significant
# digit
class IntNum:
    def __init__(self, val):
        self.val = val

    # Here we extract the most significant digit
    # of the interger and make a comparison
    # based on its value:

    # The purpose is that sorting on this criteria
    # will always produce the largest possible number
    def __lt__(rhs, lhs):
        msbr = int(str(rhs.val)[0])
        msbl = int(str(lhs.val)[0])
        if msbl < msbr:
            return True
        return False
    def __str__(self):
        return str(self.val)


def main():
    # The example vector, but works on any list really
    nums = [50, 2, 1, 9]

    # Convert our ints into our wrapper class for easy comparison
    list_of_IntNums = [IntNum(x) for x in nums]
    # Sort using our new evaluation criteria
    list_of_IntNums.sort()

    # Build the string from the correctly sorted list of ints
    print "".join(str(x.val) for x in list_of_IntNums)
    
    

main()
