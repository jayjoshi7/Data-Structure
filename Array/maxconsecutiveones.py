#Given a binary array, find the maximum number of consecutive 1s in this array.

#Example 1:
#Input: [1,1,0,1,1,1]
#Output: 3

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = max_cnt = 0
        
        for i in nums:
            if (i == 1):
                cnt+=1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
        return max(max_cnt, cnt)
