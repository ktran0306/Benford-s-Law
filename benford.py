# Khoa Tran
# CSCI 236 3/18/2021
# Program 05 - Benford's Law
# 2.5 hours
# Grade version: B-version
# Major problems:
# average status of the program - It compiles

from protein_lengths import naa
import sys
import re

file = open(input("Input file: "))

lines = file.readlines()

def fibonacci():
    fib = [1, 1]
    for i in range(498):
        fib.append(fib[i] + fib[i + 1])
    with open('fib500.txt', 'w') as filehandle:
        for f in fib:
            filehandle.write('%s\n' % f)
    return fib

if __name__ == '__main__':
    fibonacci()
    one = 0
    two = 0
    thr = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0

    for line in lines:
        if line[0] == '1':
            one += 1
        elif line[0] == '2':
            two += 1
        elif line[0] == '3':
            thr += 1
        elif line[0] == '4':
            four += 1
        elif line[0] == '5':
            five += 1
        elif line[0] == '6':
            six += 1
        elif line[0] == '7':
            seven += 1
        elif line[0] == '8':
            eight += 1
        elif line[0] == '9':
            nine += 1

    total = one + two + thr + four + five + six + seven + eight + nine
    percent_first = round((one / total) * 100, 2)
    percent_second = round((two / total) * 100, 2)
    percent_third = round((thr / total) * 100, 2)
    percent_fourth = round((four / total) * 100, 2)
    percent_fifth = round((five / total) * 100, 2)
    percent_sixth = round((six / total) * 100, 2)
    percent_seventh = round((seven / total) * 100, 2)
    percent_eighth = round((eight / total) * 100, 2)
    percent_nine = round((nine / total) * 100, 2)
    total_percent = percent_nine + percent_eighth + percent_seventh + percent_sixth + percent_fifth + percent_fourth + percent_third + percent_second + percent_first


    print("county.txt")
    print("Digit   Count   Percent")
    print("1\t \t" + str(one) + "\t \t" + str(percent_first))
    print("2\t \t" + str(two) + "\t \t" + str(percent_second))
    print("3\t \t" + str(thr) + "\t \t" + str(percent_third))
    print("4\t \t" + str(four) + "\t \t" + str(percent_fourth))
    print("5\t \t" + str(five) + "\t \t" + str(percent_fifth))
    print("6\t \t" + str(six) + "\t \t" + str(percent_sixth))
    print("7\t \t" + str(seven) + "\t \t" + str(percent_seventh))
    print("8\t \t" + str(eight) + "\t \t" + str(percent_eighth))
    print("9\t \t" + str(nine) + "\t \t" + str(percent_nine))
    print("Total\t" + str(total) + "\t" + str(total_percent))

