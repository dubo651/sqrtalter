# This is a program to test whether the squart algorithm is True or not, written in Python
# Version 1.0, only support 4 digits integer and the output is 2 digits.

a = int(input("Input the integer:"))
b = str(a)

def fir_num(b):
    if len(b) % 2 == 1:
        return b[0]
    else:
        return str(b[0]) + str(b[1])

def firblo(x):
    i = 1
    while i < 10:
        k = i*i
        j = (i + 1)*(i + 1)
        if k <= int(x) and j > int(x):
            return i
        else:
            i = i + 1

def multi(p, q):
    if int(str(p) + "1") >= q:
        return 0
    else:
        i = 1
        while i < 10:
            val = str(p) + str(i)
            gval = int(val)
            valp = str(p) + str(i + 1)
            gvalp = int(valp)
            if gval*i <= q and gvalp*(i + 1) > q:
                return i
            else:
                i = i + 1

def main(b):
    temp1 = fir_num(b)
    ans = firblo(temp1)
    temp2 = 2*int(ans)
    rem = int(temp1) - (int(ans)*int(ans))        
    digs = str(b[2]) + str(b[3])
    if rem == 0:
        temp3 = digs
    else:
        temp3 = str(rem) + digs
    fitemp3 = int(temp3)
    ans2 = multi(temp2, fitemp3)
    return int(str(ans) + str(ans2))

main(b)
