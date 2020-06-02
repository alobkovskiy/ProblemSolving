###
###0008. String to Integer (atoi)
###
###Runtime: 32 ms, faster than 94.51% of Python3 online submissions for String to Integer (atoi).
###Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for String to
###

import pytest

def myAtoi(str: str) -> int:
    s = str.strip()               
    max_int_neg = (2 ** 31)
    max_int_pos = (2 ** 31) - 1
    is_digit_without_sign = s[1:].isdigit()
    is_minus_sign_exist = s.startswith("-")
    if s.startswith("+") or is_minus_sign_exist:
        s = s[1:]            
    if len(s) == 0:
        return 0          
    if s[0].isdigit():
        k = len(s)
        for i in range(len(s)):
            if not s[i].isdigit():
                k = i
                break
        s_digit = s[:k]            
        if is_minus_sign_exist:
            if int(s_digit) > max_int_neg:
                return max_int_neg *-1
            else:
                return int(s_digit)*-1
        else:
            if int(s_digit) > max_int_pos:
                return max_int_pos
            else:
                return int(s_digit)
    else:
        return 0        

#Input: "42"
#Output: 42
def test_t1():
    s = '42'    
    result = 42
    f_result = myAtoi(s)
    assert result == f_result


#Input: "   -42"
#Output: -42
#Explanation: The first non-whitespace character is '-', which is the minus sign.
#             Then take as many numerical digits as possible, which gets 42.
def test_t2():
    s = '  -42'
    result = -42
    f_result = myAtoi(s)
    assert result == f_result


#Input: "4193 with words"
#Output: 4193
#Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
def test_t3():
    s = '4193 with words'
    result = 4193
    f_result = myAtoi(s)
    assert result == f_result


#Input: "words and 987"
#Output: 0
#Explanation: The first non-whitespace character is 'w', which is not a numerical 
#             digit or a +/- sign. Therefore no valid conversion could be performed.
def test_t4():
    s = 'words and 987'
    result = 0
    f_result = myAtoi(s)
    assert result == f_result


#Input: "-91283472332"
#Output: -2147483648
#Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#             Thefore INT_MIN (−231) is returned.
def test_t5():
    s = '-91283472332'
    result = -2147483648
    f_result = myAtoi(s)
    assert result == f_result

def test_t6():
    s = '  -0012a23'
    result = -12
    f_result = myAtoi(s)
    assert result == f_result        

def test_t7():
    s = '+'
    result = 0
    f_result = myAtoi(s)
    assert result == f_result        

def test_t8():
    s = '      -11919730356x'
    result = -2147483648
    f_result = myAtoi(s)
    assert result == f_result        