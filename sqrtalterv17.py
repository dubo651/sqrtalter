# This is a program to test whether the sqrt alternative algorithm works well or not.
# Version 1.7, fixed sqrt(0.x) bug and simplified code.
# This code is modified from Version 1.6 By GEMINI AI.

def solve():
    try:
        a_str = input("Input the integer part:").strip()
        arec_str = input("Input the fraction part:").strip()
        digit = int(input("Input the digit you want:").strip())
    except (EOFError, ValueError):
        return

    if len(a_str) % 2 == 1:
        a_str = '0' + a_str
    
    arec_padded = arec_str
    if len(arec_padded) % 2 == 1:
        arec_padded += '0'
    
    combined = a_str + arec_padded
    extra_pairs = digit - (len(arec_padded) // 2)
    if extra_pairs > 0:
        combined += '00' * extra_pairs
    
    res_digits = ""
    root = 0
    rem = 0
    
    for i in range(0, len(combined), 2):
        pair = int(combined[i:i+2])
        rem = rem * 100 + pair

        d = 0
        for test_d in range(1, 10):
            if (20 * root + test_d) * test_d <= rem:
                d = test_d
            else:
                break
        
        rem -= (20 * root + d) * d
        root = root * 10 + d
        res_digits += str(d)
    
    split_idx = len(a_str) // 2
    ans_int = res_digits[:split_idx].lstrip('0')
    if not ans_int:
        ans_int = "0"
        
    ans_fra = res_digits[split_idx:]
    
    if ans_fra:
        print(f"{ans_int}.{ans_fra}")
    else:
        print(f"{ans_int}.0")

if __name__ == "__main__":
    solve()
