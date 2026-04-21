# This is a program to test whether the sqrt alternative algorithm works well or not.
# Version 1.6, fixed a bug in line 103, add fraction point to the output.

a = int(input("Input the integer part:"))
arec = int(input("Input the fraction part:"))
digit = int(input("Input the digit you want:"))
b = str(a)
arecstr = str(arec)

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

def div_arec(arec):
    if len(arecstr) % 2 == 1:
        return (len(arecstr) + 1) / 2
    else:
        return len(arecstr) / 2

ansfr_len = div_arec(arec)

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
        elif int(str(2*anspp) + str(9))*9 < int(rem):
            rem = str(int(rem) - int(str(2*anspp) + str(9))*9)
            ans = ans + str(9)
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

def ansarec(arecstr):
    ansstr = str(ansint)
    rem = str(int(b) - (ansint*ansint))
    if len(arecstr) % 2 == 0:
        for i in range(1, int(ansfr_len) + 1):
            rec_var = str(arecstr[2*i - 2]) + str(arecstr[2*i - 1])
            rem = rem + rec_var
            if int(str(2*int(ansstr)) + str(1)) > int(rem):
                ansstr = ansstr + str(0)
                rem = rem
            elif int(str(2*int(ansstr)) + str(9))*9 < int(rem):
                rem = int(rem) - int(str(2*int(ansstr)) + str(9))*9
                ansstr = ansstr + str(9)
            else:
                for j in range(1, 10):
                    ans_try = int(str(2*int(ansstr)) + str(j))*j
                    ans_trym = int(str(2*int(ansstr)) + str(j + 1))*(j + 1)
                    if ans_try <= int(rem) and ans_trym > int(rem):
                        ansstr = ansstr + str(j)
                        rem = str(int(rem) - ans_try)
                        break
                    else:
                        j = j + 1
    else:
        for i in range(1, int(ansfr_len)):
            rec_var = str(arecstr[2*i - 2]) + str(arecstr[2*i - 1])
            rem = str(rem) + str(rec_var)
            if int(str(2*int(ansstr)) + str(1)) > int(rem):
                ansstr = ansstr + str(0)
                rem = rem
            elif int(str(2*int(ansstr)) + str(9))*9 < int(rem):
                rem = int(rem) - int(str(2*int(ansstr)) + str(9))*9
                ansstr = ansstr + str(9)
            else:
                for j in range(1, 10):
                    ans_try = int(str(2*int(ansstr)) + str(j))*j
                    ans_trym = int(str(2*int(ansstr)) + str(j + 1))*(j + 1)
                    if ans_try <= int(rem) and ans_trym > int(rem):
                        ansstr = ansstr + str(j)
                        rem = str(int(rem) - ans_try)
                        break
                    else:
                        j = j + 1
        rem = str(rem) + arecstr[len(arecstr) - 1] + '0'
        if int(str(2*int(ansstr)) + str(1)) > int(rem):
            ansstr = ansstr + str(0)
            rem = rem
        elif int(str(2*int(ansstr)) + str(9))*9 < int(rem):
            rem = int(rem) - int(str(2*int(ansstr)) + str(9))*9
            ansstr = ansstr + str(9)
        else:
            for j in range(1, 10):
                ans_try = int(str(2*int(ansstr)) + str(j))*j
                ans_trym = int(str(2*int(ansstr)) + str(j + 1))*(j + 1)
                if ans_try <= int(rem) and ans_trym > int(rem):
                    ansstr = ansstr + str(j)
                    rem = str(int(rem) - ans_try)
                    break
                else:
                    j = j + 1
    return ansstr

finans = ansarec(arecstr)

def ansflo(finans):
    flo = ''
    ansc = int(finans)
    ori_var = int(str(b) + str(arecstr))
    ori_varp = int(str(b) + str(arecstr) + '0')
    if len(str(arecstr)) % 2 == 0:
        rem = str(ori_var - (ansc*ansc))
    else:
        rem = str(ori_varp - (ansc*ansc))
    i = 0
    while i <= digit - ansfr_len - 1:
        rem = rem + "00"
        if int(str(2*ansc) + str(1)) > int(rem):
            ansc = int(str(ansc) + str(0))
            flo = flo + str(0)
            rem = rem
            i = i + 1
        elif int(str(2*ansc) + str(9))*9 < int(rem):
            rem = str(int(rem) - int(str(2*ansc) + str(9))*9)
            ansc = int(str(ansc) + str(9))
            flo = flo + str(9)  
            i = i + 1
        else:
            for j in range(1, 10):
                ans_try = int(str(2*ansc) + str(j))*j
                ans_trym = int(str(2*ansc) + str(j + 1))*(j + 1)
                if ans_try <= int(rem) and ans_trym > int(rem):
                    ansc = int(str(ansc) + str(j))
                    flo = flo + str(j)
                    rem = str(int(rem) - ans_try)
                    break
                else:
                    j = j + 1
            i = i + 1
    return ansc

nopans = str(ansflo(finans))

def addpo(nopans):
    lenno = len(nopans)
    len_int = int(div_num(b))
    ans_int = nopans[:len_int]
    sans_int = str(ans_int)
    ans_fra = nopans[len_int:]
    sans_fra = str(ans_fra)
    return sans_int + '.' + sans_fra

print(addpo(nopans))
