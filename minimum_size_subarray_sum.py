'''
SIMILAR
----------------------------------------------------------
https://leetcode.com/problems/minimum-size-subarray-sum/

PROMPT
----------------------------------------------------------
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

def minSubArrayLen(target, nums):
        smallest = 0
        i = 0
        j = 0
        total = 0
        
        while i < len(nums):
            if i == j:
                if nums[i] >= target:
                    return 1
                total += nums[i]
                j += 1
                
            while j < len(nums) and i < len(nums):
                # print("nums[i]: ", nums[i])
                # print("nums[j]: ", nums[j])
                # print("total: ", total)
                if total >= target:
                    if j - i < smallest or smallest == 0:
                        smallest = j - i
                    # shift left iter to next number
                    total -= nums[i]
                    i += 1
                elif total > target:
                    # shieft left iter to next number
                    total -= nums[i]
                    i += 1
                else:
                    total += nums[j]
                    j += 1
                    
            # print("OUTER total: ", total) 
            if total >= target:
                    if j - i < smallest or smallest == 0:
                        smallest = j - i
                    # shift left iter to next number
                    total -= nums[i]
                    i += 1
            else:
                # shieft left iter to next number
                total -= nums[i]
                i += 1
                
        return smallest


'''
CODE ABOVE HERE
'''

print(minSubArrayLen(7, [2,3,1,2,4,3])) # should return 2
print(minSubArrayLen(4, [1, 4, 4])) # should return 1
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # should return 0
print(minSubArrayLen(11, [1,2,3,4,5])) # should return 3