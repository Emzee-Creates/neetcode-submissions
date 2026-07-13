class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for string in strs:
            sorted_keys = tuple(sorted(string))
            if sorted_keys not in group:
                group[sorted_keys] = []
            group[sorted_keys].append(string)

        return list(group.values())

