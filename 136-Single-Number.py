class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter

        counter = Counter(nums)

        for i,j in counter.items():
            if j == 1:
                return i