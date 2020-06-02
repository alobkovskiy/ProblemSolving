###
###1253. Reconstruct a 2-Row Binary Matrix
###
###Runtime: 816 ms, faster than 21.54% of Python3 online submissions for Reconstruct a 2-Row Binary Matrix.
###Memory Usage: 23.1 MB, less than 100.00% of Python3 online submissions for Reconstruct a 2-Row Binary Matrix.
###

from typing import List
import pytest


def reconstructMatrix(upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
    arr_len = len(colsum)
    arr = [[0] * arr_len for i in range(2)]
    up_count = 0
    low_count = 0
    is_empty = False
    for k,v in enumerate(colsum):
        if v == 2:
            if up_count < upper and low_count < lower:
                arr[0][k] = 1
                arr[1][k] = 1
                up_count += 1
                low_count += 1
            else:
                is_empty = True
                continue
            
    for k,v in enumerate(colsum):
        if v == 1:
            if up_count < upper:
                arr[0][k] = 1
                up_count += 1
            elif low_count < lower:
                arr[1][k] = 1
                low_count += 1
            else:
                is_empty = True
                continue
    if is_empty or up_count < upper or low_count < lower: arr = []
        
    return arr          


#Input: upper = 2, lower = 1, colsum = [1,1,1]
#Output: [[1,1,0],[0,0,1]]
#Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.
def test_t1():
    upper = 2
    lower = 1
    colsum = [1,1,1]
    result = [[1,1,0],[0,0,1]]
    f_result = reconstructMatrix(upper, lower, colsum)
    assert result == f_result


#Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
#Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
def test_t2():
    upper = 5
    lower = 5
    colsum = [2,1,2,0,1,0,1,2,0,1]
    result = [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
    f_result = reconstructMatrix(upper, lower, colsum)
    assert result == f_result


def test_t3():
    upper = 4
    lower = 7
    colsum = [2,1,2,2,1,1,1]
    result = []
    f_result = reconstructMatrix(upper, lower, colsum)
    assert result == f_result
