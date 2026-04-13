# This is a program to test whether the squart algorithm is True or not, written in python
# Version 1.2, supports integer and the digit of the output can be defined by user.

a = int(input("Input the integer:"))
digit = int(input("Input the digit of the output:"))
b = str(a)

def fir_num(b):
    if len(b) % 2 == 1:
        return b[0]
    else:
        return str(b[0]) + str(b[1])

def div_num(b):
    if len(b) % 2 == 1:
        return (len(b) + 1) / 2
    else:
        return len(b) / 2

def firblo(x):
    i = 1
    while i < 10:
        k = i*i
        j = (i + 1)*(i + 1)
        if k <= int(x) and j > int(x):
            return i
        else:
            i = i + 1

def anspro(b):
    ans = ''
    ans_len = div_num(b)
    fir_var = fir_num(b)
    fir_dig = str(firblo(fir_var))
    ans = ans + fir_dig
    fir_rem = int(fir_num(b)) - int(fir_dig)*int(fir_dig)
    rem = fir_rem
    anspp = int(ans)
    for i in range(2, int(ans_len + 1)):
        if len(b) % 2 == 1:
            rec_var = str(b[2*i - 3]) + str(b[2*i - 2])
        else:
            rec_var = str(b[2*i - 2]) + str(b[2*i - 1])
        rem = str(rem) + rec_var
        if int(str(2*anspp) + str(1)) > int(rem):
            ans = ans + str(0)
            rem = rem
        else:
            for j in range(1, 10):
                ans_try = int(str(2*anspp) + str(j))*j
                ans_trym = int(str(2*anspp) + str(j + 1))*(j + 1)
                if ans_try <= int(rem) and ans_trym > int(rem):
                    ans = ans + str(j)
                    rem = str(int(rem) - ans_try)
                    break
                else:
                    j = j + 1
        i = i + 1
        anspp = int(ans)
    return ans

ansint = int(anspro(b))

def ansflo(ansint):
    flo = ''
    ansc = str(ansint)
    rem = str(int(b) - (ansint*ansint))
    i = 0
    while i <= digit - 1:
        rem = rem + "00"
        if int(str(2*int(ansc)) + str(1)) > int(rem):
            ansc = ansc + str(0)
            flo = flo + str(0)
            rem = rem
            i = i + 1
        else:
            for j in range(1, 10):
                ans_try = int(str(2*int(ansc)) + str(j))*j
                ans_trym = int(str(2*int(ansc)) + str(j + 1))*(j + 1)
                if ans_try <= int(rem) and ans_trym > int(rem):
                    ansc = ansc + str(j)
                    flo = flo + str(j)
                    rem = str(int(rem) - ans_try)
                    break
                else:
                    j = j + 1
            i = i + 1
    return flo

def finans(b):
    financ = anspro(b) + '.' + ansflo(ansint)
    return financ
    
finans(b)
