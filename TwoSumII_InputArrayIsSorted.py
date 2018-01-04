class TwoSumIIInputArrayIsSorted(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        remainder = {}
        numsLen = len(numbers)
        for i in range(0, numsLen):
            num = numbers[i]
            if (remainder.has_key(num)):
                return [remainder[num]+1, i+1]
            else:
                remainder[target - num] = i

if __name__ == '__main__':
    ts = TwoSumIIInputArrayIsSorted()
    print ts.twoSum([2, 3, 4], 6)
    print ts.twoSum([3, 2, 4], 6)
    print ts.twoSum([2, 5, 5, 11], 10)
    print ts.twoSum([3, 3], 6)