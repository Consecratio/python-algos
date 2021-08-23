'''
SIMILAR
----------------------------------------------------------
https://leetcode.com/discuss/general-discussion/657507/Sliding-Window-for-Beginners-Problems-or-Template-or-Sample-Solutions

PROMPT
----------------------------------------------------------
Parking spots [2, 3, 7, 15]
Number of cars that need to be covered k = 3
Find smallest length needed to cover k cars
'''

def slidingWindow(spots, k):
    length = float('inf')
    for i in range(len(spots) - k):
        if (spots[i + k - 1] - spots[i]) < length:
            length = spots[i + k - 1] - spots[i] + 1
    
    return length
        

'''
CODE ABOVE HERE
'''

print(slidingWindow([2, 3, 7, 15], 3)) # should return 6