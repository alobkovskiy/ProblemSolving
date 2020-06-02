###
###0001. Two Sum
###Runtime: 5948 ms  (better than 8.96%)
###Memory Usage: 14 MB (better than 65.35%)
###

import pytest
from typing import List

#brute force accepted
def twoSum(nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if target == nums[i] + nums[j]:
                result.append(i)
                result.append(j)
                break
        if len(result) > 0:
            break
    return result


#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
def test_t1():
    nums = [2, 7, 11, 15]
    target = 9
    result = [0, 1]        
    f_result = twoSum(nums, target)
    assert result == f_result