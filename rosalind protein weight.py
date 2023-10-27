import math
import numpy

seq = str(input('Enter seq1:'))

le=len(seq)
fin=[]
sum=0
for i in range(0,le):
    if seq[i] == "A" :
        sum = sum + 71.03711   
    elif seq[i] == "C" :
        sum = sum + 103.00919 
    elif seq[i] == "D" :
        sum = sum + 115.02694 
    elif seq[i] == "E" :
        sum = sum + 129.04259 
    elif seq[i] == "F" :
        sum = sum + 147.06841 
    elif seq[i] == "G" :
        sum = sum + 57.02146
    elif seq[i] == "H" :
        sum = sum + 137.05891 
    elif seq[i] == "I" :
        sum = sum + 113.08406
    elif seq[i] == "K" :
        sum = sum + 128.09496 
    elif seq[i] == "L" :
        sum = sum + 113.08406 
    elif seq[i] == "M" :
        sum = sum + 131.04049 
    elif seq[i] == "N" :
        sum = sum + 114.04293 
    elif seq[i] == "P" :
        sum = sum + 97.05276 
    elif seq[i] == "Q" :
        sum = sum + 128.05858 
    elif seq[i] == "R" :
        sum = sum + 156.10111 
    elif seq[i] == "S" :
        sum = sum + 87.03203 
    elif seq[i] == "T" :
        sum = sum + 101.04768 
    elif seq[i] == "V" :
        sum = sum + 99.06841 
    elif seq[i] == "W" :
        sum = sum + 186.07931 
    else :
        sum = sum + 163.06333 
    

print(sum)
