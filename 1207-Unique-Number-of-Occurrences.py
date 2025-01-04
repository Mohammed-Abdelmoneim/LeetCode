class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter

        freq_map = Counter(arr)
        freq_set = set(freq_map.values())

        return len(freq_map) == len(freq_set)