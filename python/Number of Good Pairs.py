#Number of Good Pairs
#Input: nums = [1,2,3,1,1,3]
#Output: 4
#Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
   def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] == nums[j]):
                    count += 1
        return count
