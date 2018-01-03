class BinaryWatch(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        timeList = []
        for h in range(12):
            for m in range(60):
                if((bin(h) + bin(m)).count('1') == num):
                    timeList.append('%d:%02d' % (h,m) )
        return timeList


if __name__ == '__main__':
    bw = BinaryWatch()
    print bw.readBinaryWatch(7)