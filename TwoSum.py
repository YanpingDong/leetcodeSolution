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


if __name__ == '__main__':
    ts = TwoSum()
    print ts.twoSum([3,2,4],6)