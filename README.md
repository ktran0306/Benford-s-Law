# Benford-s-Law
Benford's Law is an observation about the distribution of the frequencies of the first digits of the numbers in many different data sets. It is frequently 
found that the first digits are not uniformly distributed, but follow the logarithmic distribution

P(d)=log10(d+1d).

That is, numbers starting with 1 are more common than those starting with 2, and so on, with those starting with 9 the least common. The probabilities are given below:


Digit	Probability
1	    0.301
2	    0.176
3	    0.125
4	    0.097
5	    0.079
6	    0.067
7	    0.058
8	    0.051
9	    0.046

Benford's Law is most accurate for data sets which span several orders of magnitude, and can be proved to be exact for some infinite sequences of numbers.

Write a Python program that analyzes a set of integers to see how closely it follows Benford's Law. If you need some help thinking about how to do this, here is an excellent article that shows you how to do this in Excel. Get the name of the input file from the command line. Name this program benford.py. 

(a) Demonstrate that the first digits of the first 500 Fibonacci numbers (see this Example) follow Benford's Law quite closely. 
You will need to generate these numbers and put them in a file or look them up and copy/paste them into a file. 
MAKE SURE YOU HAVE THE CORRECT NUMBERS. Name the file fib500.txt. Submit this file to CodePost. NOTE: the fibonacci sequence starts with 0, 1, 1, 2, 3, 5 .......

(b) The length of the amino acid sequences of 500 randomly-chosen proteins are provided in the file protein_lengths.py. 
This file contains a list, naa. Write a quick program to convert this list into a text file you can read into your benford.py program. 

The attached test file (county.txt) contains election 2020 voting results from one US county. 

Your output should be formatted as follows. A heading line followed by 9 lines with each digit, 1-9, followed by the percentage.

Here is how your output should look using the attached test file (county.txt). Use tabs between columns. 

county.txt
Digit   Count   Percent
1       953     30.32
2       594     18.9
3       374     11.9
4       308     9.8
5       213     6.78
6       211     6.71
7       182     5.79
8       152     4.84
9       156     4.96
Total   3143    100.0
