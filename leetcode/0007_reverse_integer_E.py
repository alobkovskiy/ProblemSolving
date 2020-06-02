###
###0007. Reverse Integer
###
###Runtime: 32 ms ( better than 63.4% )
###Memory Usage: 12.7 MB ( better than ?% )
###

import pytest

def reverse(x: int) -> int:
    sign = False
    max_int = (2 ** 31) - 1
    if x < 0:
        sign = True
        max_int = max_int + 1        
    s = str(abs(x))        
    result = int(s[::-1])
    if result > max_int:
        result = 0
    if sign:
        result = result * -1
    return result    

#Input: 123
#Output: 321
def test_123():
    s = 123
    result = 321
    f_result = reverse(s)
    assert result == f_result

#Input: -123
#Output: -321
def test_minus123():
    s = -123
    result = -321
    f_result = reverse(s)
    assert result == f_result

#Input: 120
#Output: 21
def test_120():
    s = 120
    result = 21
    f_result = reverse(s)
    assert result == f_result