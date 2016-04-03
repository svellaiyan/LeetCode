'''Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total=reduce(lambda x, y: x*y,nums)
        newNums=[]
        for n in range(0,len(nums)):
            if nums[n]==0:
                b = [x for i,x in enumerate(nums) if i!=n] 
                newNums.append(reduce(lambda x, y: x*y,b))
                continue
            newNums.append(total/nums[n])
        return newNums
