import collections
class Solution:
    def __init__(self):
        self.table = collections.defaultdict(int) 

    def twoSum(self,nums,target):
        for i,num in enumerate(nums):
            complement = target - nums[i]
            if complement in self.table:
                return [i,self.table[complement]]
            else:
                self.table[nums[i]] = i

s = Solution()
print(s.twoSum([2,7,11,15],9))
