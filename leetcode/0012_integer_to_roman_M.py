###
###0012. Integer to Roman
###Runtime: 44 ms, faster than 92.78% of Python3 online submissions for Integer to Roman.
###Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Integer to Roman.
###

import pytest

def countRoman(dc, p, d):
    if p < 4:
        r = dc[d]*p
    elif p in [4,5,9]:
        r = dc[p*d]
    else:
        r = dc[5*d] + dc[d]*(p-5)
    return r
    
def intToRoman(num: int) -> str:
    result = ""
    d = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"            
    }        
    
    p1 = num % 10
    p2 = num % 100
    p3 = num % 1000
    p4 = num % 10000

    p2 = (p2 - p1) // 10
    p3 = (p3 - p2 - p1) // 100
    p4 = (p4 - p3 - p2 - p1) // 1000
            
    r4 = r3 = r2 = r1 = ""
    
    if p4 > 0:
        r4 = d[1000]*p4
        
    if p3 > 0:
        r3 = countRoman(d, p3, 100)

    if p2 > 0:
        r2 = countRoman(d, p2, 10)

    r1 = countRoman(d, p1, 1)
    
    return r4 + r3 + r2 + r1
        
        
def test_60():
    num = 60
    result = 'LX'
    f_result = intToRoman(num)
    assert result == f_result


def test_3999():
    num = 3999
    result = 'MMMCMXCIX'
    f_result = intToRoman(num)
    assert result == f_result


def test_3():
    num = 3
    result = 'III'
    f_result = intToRoman(num)
    assert result == f_result


def test_4():
    num = 4
    result = 'IV'
    f_result = intToRoman(num)
    assert result == f_result


def test_9():
    num = 9
    result = 'IX'
    f_result = intToRoman(num)
    assert result == f_result


def test_58():
    num = 58
    result = 'LVIII'
    f_result = intToRoman(num)
    assert result == f_result


def test_1994():
    num = 1994
    result = 'MCMXCIV'
    f_result = intToRoman(num)
    assert result == f_result