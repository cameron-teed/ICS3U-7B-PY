#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Dec 2019
# This program tell you if it is a pallindrom

import random
import string


def checker(pallindrom, lenght):
    # Checks if it is a pallindrom

    # process
    # formats the word
    new = []
    pallindrom = pallindrom.replace(" ", "")
    pallindrom = pallindrom.lower()
    pallindrom = pallindrom.replace(".", "")

    # reverses word
    for loop_counter in range(lenght):
        word = lenght - loop_counter
        word2 = word - 1
        new.append(pallindrom[word2:word])

    # converts list to string
    new = "".join(new)

    # checks if the reversed string is the same as the original string
    if new == pallindrom:
        yes = True
        return yes
    else:
        no = False
        return no


def main():
    # Get pallindorm and tells you if it is a pallindrom

    # input
    pallindrom = input("Please put in a pallindrom: ")
    lenght = len(pallindrom)
    checker1 = checker(pallindrom, lenght)

    # output
    if checker1 is True:
        print("That is a pallindrom.")
    if checker1 is False:
        print("That is not a pallindrom")


if __name__ == "__main__":
    main()
