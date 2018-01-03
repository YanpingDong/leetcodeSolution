class NumberOfOneBits(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        count = 0
        while n:
            count += n & 1
            n = n >> 1

        return count

if __name__ == '__main__':
    noob = NumberOfOneBits()
    print noob.hammingWeight(11)  #the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3