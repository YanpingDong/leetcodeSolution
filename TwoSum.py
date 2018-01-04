class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsLen = len(nums)
        for i in range(0, numsLen):
            firstNum = nums[i]
            for k in range(i+1, numsLen):
                secondNum = nums[k]
                if target == firstNum + secondNum:
                    return [i,k]

    def twoSumOptimal(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remainder={}
        numsLen = len(nums)
        for i in range(0, numsLen):
            num = nums[i]
            if( remainder.has_key(num) ):
                return [remainder[num], i]
            else:
                remainder[target-num] = i

if __name__ == '__main__':
    ts = TwoSum()
    print ts.twoSum([3, 2, 4], 6)
    print ts.twoSumOptimal([2, 5, 5, 11], 10)
    print ts.twoSumOptimal([3, 2, 4], 6)
    print ts.twoSumOptimal([3, 3], 6)

