class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        w1 = ''
        w2 = ''
        for i in word1:
            w1 = w1 + i
        for i in word2:
            w2 = w2 + i

        if (w1 == w2):
            return True
        else:
            return False