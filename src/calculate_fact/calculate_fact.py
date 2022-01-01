#!/usr/bin/env python
from sys import setrecursionlimit
from argparse import ArgumentParser


def calculate_fact(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * calculate_fact(n-1)


def main():
    parser = ArgumentParser()
    parser.add_argument("--reclimit", type=int, default=1000, help="Set recursion limit (Default 1000)")
    parser.add_argument("ns", type=int, nargs="+", help="")
    args = parser.parse_args()
    setrecursionlimit(args.reclimit)

    for n in args.ns:
        print(n, calculate_fact(n))


if __name__ == "__main__":
    main()


