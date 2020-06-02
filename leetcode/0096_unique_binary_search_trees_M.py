###
###96. Unique Binary Search Trees
###Runtime: 28 ms, faster than 83.66% of Python3 online submissions for Unique Binary Search Trees.
###Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Unique Binary Search Trees.
###
###
#Input: 3
#Output: 5
#Explanation:
#Given n = 3, there are a total of 5 unique BST's:

#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3

'''
##
1 = 1
2 = 2
3 = 5  (2 1 ...) 
4 = 14 (5 2 ...) 
5 = 42 (14 5 4 ...)  
6 = 132 (42 14 10 ...) 
7 = 429 (132 42 28 25 ...) 
8 = 1430 (429 132 84 70 ... ) 
  [0:1430 1:429 2:132 3:84 4:70]  
  [0:1 1:2 2:5 3:14 4:42 5:132 6:429 7:1430]
9 =  (1430 429 264 210 196 ...) 

............
[0:1] => 2
    1) 1  = a[0]*1

[0:1 1:2] => 3 | 2
    1) 2  = a[1]*1
    2) 1  = a[0]*1    
       2  = a[1]*1
    
[0:1 1:2 2:5] => 4 | 2
    1) 5  = a[2]*1
    2) 2  = a[1]*1
       2  = a[1]*1
       5  = a[2]*1
    
[0:1 1:2 2:5 3:14] => 5 | 3
    1) 14   = a[3]*1
    2) 5    = a[2]*1
    3) 2    = a[1]*2
       5    = a[2]*1
       14   = a[3]*1

[0:1 1:2 2:5 3:14 4:42] => 6 | 3
    1) 42  = a[4]*1
    2) 14   = a[3]*1
    3) 10   = a[2]*2

[0:1 1:2 2:5 3:14 4:42 5:132] => 7 | 4
    1) 132  = a[5]*1
    2) 42   = a[4]*1
    3) 28   = a[3]*2
    4) 25   = a[2]*5

[0:1 1:2 2:5 3:14 4:42 5:132 6:429] => 8 | 4
    1) 429  = a[6]*1
    2) 132  = a[5]*1
    3) 84   = a[4]*2
    4) 70   = a[3]*5


[0:1 1:2 2:5 3:14 4:42 5:132 6:429 7:1430] => 9
    1) 1430 = a[7]*1 
    2) 429  = a[6]*1 
    3) 264  = a[5]*2
    4) 210  = a[4]*5
    5) 196  = a[3]*14
[0:1430 1:429 2:264 3:210 4:196]

'''


import pytest
from typing import List

def calcTree(v: int, arr: List[int], coef: List[int]) -> List[int]:
    if v == 1:  
        arr.append(v)
        coef.append(v)
        return arr
    arr = calcTree(v-1, arr, coef)        
    coef.append(arr[len(arr)-1])
    odd = v % 2 
    N = v // 2
    p = len(arr)-1
    
    s = 0
    k = N
    i = 0
    while k > 0:
        s = s + arr[p] * coef[i] * 2           
        k -= 1
        p -= 1
        i += 1
    
    if odd == 1:
        s = s + arr[p] * coef[i]
        
    arr.append(s)
    return arr       

#computed, not generated
def numTrees(n: int) -> int:
    r = 0
    odd = n % 2 
    N = n // 2 + odd
    coef_array = []
    res_array = []        
    res_array = calcTree(n, res_array, coef_array)
    
    return res_array[len(res_array)-1]
        


def test_3():
    n = 3
    result = 5
    f_result = numTrees(n)
    assert result == f_result

def test_8():
    n = 8
    result = 1430
    f_result = numTrees(n)
    assert result == f_result
