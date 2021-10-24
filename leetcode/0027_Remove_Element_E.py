###
###0027. Remove Element
###Runtime: 21 ms, faster than 99.04% of Python3 online submissions for Remove Element.
###Memory Usage: 14 MB, less than 98.90% of Python3 online submissions for Remove Element.
###

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    
    count_none = 0
    for i in range(0, len(nums)):
        if nums[i] == val:
            nums[i] = None
            count_none += 1

    if count_none == 0:
        correct_element_index = len(nums)
    else:
        correct_element_index = 0
    if count_none > 0 and count_none < len(nums):
        for i in range(0, len(nums) - 1):
            if nums[i] != None:
                correct_element_index += 1
            if nums[i] == None and nums[i + 1] != None:
                nums[correct_element_index], nums[i + 1] = nums[i + 1], nums[i]
                correct_element_index += 1
    
    return correct_element_index


def test_val0_none3():
    nums = [0,1,3,5,7,0,4,0,2]
    result = 6
    f_result = removeElement(nums, 0)
    assert result == f_result

def test_val2_none3():
    nums = [0,1,2,2,3,0,4,2]
    result = 5
    f_result = removeElement(nums, 2)
    assert result == f_result

def test_all_none():
    nums = [0,0,0,0]
    result = 0
    f_result = removeElement(nums, 0)
    assert result == f_result

def test_all_correct():
    nums = [0,0,0,0]
    result = 4
    f_result = removeElement(nums, 1)
    assert result == f_result

def test_one_correct():
    nums = [0]
    result = 1
    f_result = removeElement(nums, 1)
    assert result == f_result

def test_one_none():
    nums = [0]
    result = 0
    f_result = removeElement(nums, 0)
    assert result == f_result
