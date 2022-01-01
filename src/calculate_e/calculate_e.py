from argparse import ArgumentParser
from sys import setrecursionlimit
from math import factorial



def calculate_e(n: int) -> float:
    if n == 0:
        return 1
    else:
        return 1/factorial(n) + calculate_e(n-1)


def main():
    parser = ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--reclimit", type=int, default=1000)
    args = parser.parse_args()

    setrecursionlimit(args.reclimit)
    print(calculate_e(args.n))


if __name__ == "__main__":
    main()
