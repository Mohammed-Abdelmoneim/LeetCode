class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int(''.join(map(str, digits))) +1
        ls = []
        for i in str(n):
            ls.append(int(i))
        return ls