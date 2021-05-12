#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program calculates factorial


def main():
    print("This program calculates the factorial.\n")

    try:
        integer = int(input("Insert a positive integer:"))
        loop = 0
        result = 1
        if integer >= 0:
            while loop < integer:
                loop = loop + 1
                result = result * loop
            print("\n{0}! = {1}".format(integer, result))
        else:
            print(
                "\nThis input is invalid, please, insert a positive integer."
            )
    except Exception:
        print("\nThis input is invalid, please, insert an integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
