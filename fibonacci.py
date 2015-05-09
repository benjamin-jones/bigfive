#!/usr/bin/env python

# Use a generator rather than naive recursive implemenation
# fib(100) would take forever otherwise
def fib():
    # Initialize i and j (the first two in the sequence)
    i, j = 0, 1
    
    # Since we want to be able to arbitrarily generate numbers
    # the iteration must continue indefinitely
    while True:
        # Yield the answer
        yield i

        # Update the generator according to the fibonacci recurrance relation
        i,j = j, i + j

def main():
    # Instantiate the generator
    fib_gen = fib()

    # Get the first 100 numbers in the set
    for i in range(101):
        print fib_gen.next(),

main()
