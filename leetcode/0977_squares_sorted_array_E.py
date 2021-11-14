###
###0977. Squares of a Sorted Array
###Runtime: 200 ms, faster than 98.09% of Python3 online submissions for Squares of a Sorted Array.
###Memory Usage: 15.9 MB, less than 91.27% of Python3 online submissions for Squares of a Sorted Array.
###

# import random
from typing import List

def sortedSquares(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    return sorted(nums)


def test_1():
    nums = [-4,-1,0,3,10]
    result = [0,1,9,16,100]
    f_result = sortedSquares(nums)
    assert result == f_result

def test_2():
    nums = [-7,-3,2,3,11]
    result = [4,9,9,49,121]
    f_result = sortedSquares(nums)
    assert result == f_result

# nums = [random.randint(-10000,100000) for i in range(100000)]
# f_result = sortedSquares(nums)
# print(f_result)
