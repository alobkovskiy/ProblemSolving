###
###881. Boats to Save People
###Runtime: 504 ms, faster than 76.97% of Python3 online submissions for Boats to Save People.
###Memory Usage: 19.5 MB, less than 16.67% of Python3 online submissions for Boats to Save People.
###
#1 <= people.length <= 50000
#1 <= people[i] <= limit <= 30000

from typing import List
import pytest

def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    lower = 0
    upper = len(people) - 1
    result = 0
    while lower <= upper:
        if people[upper] == limit:
            result += 1
            upper -= 1
            continue
        elif people[upper] < limit and people[lower] + people[upper] <= limit:
            result += 1
            upper -= 1
            lower += 1
            continue
        else:
            result += 1
            upper -= 1
            continue
    return result               
        

def test_22_6():
    people = [2, 2]
    limit = 6
    result = 1
    f_result = numRescueBoats(people, limit)
    assert result == f_result

#Input: people = [1,2], limit = 3
#Output: 1
#Explanation: 1 boat (1, 2)
def test_12_3():
    people = [1, 2]
    limit = 3
    result = 1
    f_result = numRescueBoats(people, limit)
    assert result == f_result

#Input: people = [3,2,2,1], limit = 3
#Output: 3
#Explanation: 3 boats (1, 2), (2) and (3)
def test_3221_3():
    people = [3,2,2,1]
    limit = 3
    result = 3
    f_result = numRescueBoats(people, limit)
    assert result == f_result


#Input: people = [3,5,3,4], limit = 5
#Output: 4
#Explanation: 4 boats (3), (3), (4), (5)
def test_3534_3():    
    people = [3,5,3,4]
    limit = 5
    result = 4
    f_result = numRescueBoats(people, limit)
    assert result == f_result

def test_11111_3():
    people = [1,1,1,1,1]
    limit = 2
    result = 3
    f_result = numRescueBoats(people, limit)
    assert result == f_result    

def test_2_2():
    people = [2]
    limit = 2
    result = 1
    f_result = numRescueBoats(people, limit)
    assert result == f_result    
