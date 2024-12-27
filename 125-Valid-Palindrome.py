class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str = s.lower()
        res = ''
        for i in str:
            if (i in 'abcdefghijklmnopqrstuvwxyz0123456789'):
                res =  res + i


        if (res == res[::-1]):
            return True
        else:
            return False