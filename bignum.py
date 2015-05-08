#!/usr/bin/env python

class IntNum:
    def __init__(self, val):
        self.val = val
    def __lt__(rhs, lhs):
        msbr = int(str(rhs.val)[0])
        msbl = int(str(lhs.val)[0])
        if msbl < msbr:
            return True
        return False
    def __str__(self):
        return str(self.val)


def main():
    nums = [50, 2, 1, 9]
    list_of_IntNums = [IntNum(x) for x in nums]
    list_of_IntNums.sort()

    print "".join(str(x.val) for x in list_of_IntNums)
    
    

main()
