class ReverseBits(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        rvalue = 0

        for i in range(0,32):
            rvalue <<= 1
            rvalue += n & 1
            n >>= 1

        return rvalue

if __name__ == '__main__':
    rb = ReverseBits()
    print rb.reverseBits( 2147483648 ) # print 1