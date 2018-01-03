class AddBinary(object):

    # transform binary str to binary type
    def getBinary(self, strBin):
        """
        :param strBin: str
        :return: bin
        """
        binRetValue = 0
        for aLetter in strBin :
            if aLetter == '1':
                binRetValue <<= 1
                binRetValue += 1
            else :
                binRetValue <<= 1

        return binRetValue

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        bA = self.getBinary(a)
        bB = self.getBinary(b)
        rv = bA+bB
        return bin(rv)[2:]

    def addBinaryOptimal(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # use python lib do str to binary
        return bin(int(a, base=2) + int(b, base=2))[2:]

if __name__ == '__main__':
    ab = AddBinary()
    print ab.addBinary('1010','1011')




