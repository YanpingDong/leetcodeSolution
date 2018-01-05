class PowerOfTwo(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and bin(n).count('1') == 1

    def isPowerOfTwoOptimal(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not(n&n-1)


if __name__ == '__main__':
    pot = PowerOfTwo()
    print pot.isPowerOfTwo(10)
    print pot.isPowerOfTwo(16)
    print pot.isPowerOfTwoOptimal(10)
    print pot.isPowerOfTwoOptimal(16)
