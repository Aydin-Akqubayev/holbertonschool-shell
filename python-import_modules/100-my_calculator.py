#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():

    list_argument = *sys.argv[1:]
    print(list_argument)
    if len(list_argument) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")

    else:
        f_n = int(list_argument[0])
        op = list_argument[1]
        s_n = int(list_argument[2])

        if op in '+':
            print("{} + {} = {}".format(f_n, s_n, add(f_n, s_n)))

        elif op in '-':
            print("{} + {} = {}".format(f_n, s_n, sub(f_n, s_n)))

        elif op in '*':
            print("{} + {} = {}".format(f_n, s_n, mul(f_n, s_n)))

        elif op in '/':
            print("{} + {} = {}".format(f_n, s_n, div(f_n, s_n)))

        else:
            print("Unknown operator. Available operators: +, -, * and /")

if __name__ == "__main__":
    main()


