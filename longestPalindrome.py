'''
SIMILAR
-------------------------------------------------------------------------
https://leetcode.com/problems/longest-palindromic-substring/

PROMPT
-------------------------------------------------------------------------
Given a string s, return the longest palindromic substring in s.
'''
import math

def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

def helper(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]

print(longestPalindrome("babad")) # Output: "bab" OR "aba"
print(longestPalindrome("cbbd")) # Output: "bb"
print(longestPalindrome("a")) # Output: "a"
print(longestPalindrome("ac")) # Output: "a"
print(longestPalindrome("ccc")) # Output: "ccc"
print(longestPalindrome("cccc")) # Output: "cccc"