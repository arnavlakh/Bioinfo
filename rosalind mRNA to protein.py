import math
import numpy

seq1 = str(input('Enter seq1:'))
fin = []
out = []
for i in range(0, len(seq1), 3):
    out.append(seq1[i:i+3])

le=len(out)
 
for i in range(0,le):
    if out[i] == "UUU" or out[i]=="UUC" :
        fin.append("F")    
    elif out[i] == "CUU" or out[i] == "CUC" or out[i] == "CUA" or out[i] == "CUG" or out[i] == "UUA" or out[i] == "UUG" :
        fin.append("L")
    elif out[i] == "AUU" or out[i] == "AUC" or out[i] == "AUA" :
        fin.append("I")
    elif out[i] == "GUU" or out[i] == "GUC" or out[i] == "GUA" or out[i] == "GUG":
        fin.append("V")
    elif out[i] == "UCU" or out[i] == "UCC" or out[i] == "UCA" or out[i] == "UCG" or out[i] == "AGU" or out[i] == "AGC" :
        fin.append("S")
    elif out[i] == "CCU" or out[i] == "CCC" or out[i] == "CCA" or out[i] == "CCG" :
        fin.append("P")
    elif out[i] == "ACU" or out[i] == "ACC" or out[i] == "ACA" or out[i] == "ACG" :
        fin.append("T")
    elif out[i] == "GCU" or out[i] == "GCC" or out[i] == "GCA" or out[i] == "GCG" :
        fin.append("A")
    elif out[i] == "CGU" or out[i] == "CGC" or out[i] == "CGA" or out[i] == "CGG" or out[i] == "AGA" or out[i] == "AGG" :
        fin.append("R")
    elif out[i] == "GGU" or out[i] == "GGC" or out[i] == "GGA" or out[i] == "GGG" :
        fin.append("G")
    elif out[i] == "AAA" or out[i] == "AAG" :
        fin.append("K")
    elif out[i] == "UGU" or out[i] == "UGC" :
        fin.append("C")
    elif out[i] == "CAA" or out[i] == "CAG" :
        fin.append("Q")
    elif out[i] == "UAU" or out[i] == "UAC" :
        fin.append("Y")
    elif out[i] == "GAA" or out[i] == "GAG" :
        fin.append("E")
    elif out[i] == "CAU" or out[i] == "CAC" :
        fin.append("H")
    elif out[i] == "AAU" or out[i] == "AAC" :
        fin.append("N")
    elif out[i] == "GAU" or out[i] == "GAC" :
        fin.append("D")
    elif out[i] == "UAG" or out[i] == "UGA" or out[i] == "UAA":
        fin.append("stop")
    elif out[i] == "UGG":
        fin.append("W")
    elif out[i] == "AUG":
        fin.append("M")

print(fin)
print(''.join(fin))

