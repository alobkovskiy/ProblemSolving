###
###0424. Longest Repeating Character Replacement
###Runtime: 128 ms, faster than 61.50% of Python3 online submissions for Longest Repeating Character Replacement.
###Memory Usage: 13.8 MB, less than 12.50% of Python3 online submissions for Longest Repeating Character Replacement.
###
###
import pytest

def length_of_longest_substring(s, k):
    result = -1

    if k == len(s):
        result = k
    
    freq_map = {}
    max_repeated = 0
    win_start = 0

    for i in range(len(s)):
        
        if s[i] not in freq_map:
            freq_map[s[i]] = 0
        freq_map[s[i]] += 1

        max_repeated = max(max_repeated, freq_map[s[i]])

        if i + 1 - win_start - max_repeated > k:
            freq_map[s[win_start]] -= 1
            win_start += 1

        result = max(result, i + 1 - win_start)            

    return result


def test_aabccbb_k2():
    s = 'aabccbb'
    k = 2
    result = 5
    f_result = length_of_longest_substring(s, k)
    assert f_result == result


def test_abbcb_k1():
    s = 'abbcb'
    k = 1
    result = 4
    f_result = length_of_longest_substring(s, k)
    assert f_result == result


def test_abccde_k1():
    s = 'abccde'
    k = 1
    result = 3
    f_result = length_of_longest_substring(s, k)
    assert f_result == result


def test_aabbbc_k2():
    s = 'aabbbc'
    k = 2
    result = 5
    f_result = length_of_longest_substring(s, k)
    assert f_result == result


def test_aaabbab_k2():
    s = 'aaabbab'
    k = 2
    result = 6
    f_result = length_of_longest_substring(s, k)
    assert f_result == result


def test_aaab_k0():
    s = 'aaab'
    k = 0
    result = 3
    f_result = length_of_longest_substring(s, k)
    assert f_result == result


def test_aaaa_k2():
    s = 'aaaa'
    k = 2
    result = 4
    f_result = length_of_longest_substring(s, k)
    assert f_result == result
