class Solution:
    def romanToInt(self, s: str) -> int:
        holder = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }  
        res = 0
        for i in range(len(s)):
            if i < len(s) -1 and holder[s[i]] < holder[s[i+1]]:
                res -= holder[s[i]]
            else:
                res += holder[s[i]]
        return res