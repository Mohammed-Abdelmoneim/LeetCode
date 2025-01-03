class Solution:
    def reverseWords(self, s: str) -> str:
        strSplit = s.split()[::-1]
        newStr = ' '.join(strSplit)
        return newStr