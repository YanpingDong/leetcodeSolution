class BinaryNumberWithAlternatingBits(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = True
        currentBit = n & 1
        while n :
            n = n >> 1
            if(n) :
                nextBit = n & 1
                if currentBit == nextBit:
                    flag = False
                    break
                else:
                    currentBit = nextBit

        return flag

if __name__ == '__main__':
    bnwab = BinaryNumberWithAlternatingBits()
    print bnwab.hasAlternatingBits(10)