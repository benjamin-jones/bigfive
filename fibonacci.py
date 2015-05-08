#!/usr/bin/env python

def fib():
    i, j = 0, 1
    while True:
        yield i
        i,j = j, i + j

def main():
    fib_gen = fib()

    for i in range(101):
        print fib_gen.next(),

main()
