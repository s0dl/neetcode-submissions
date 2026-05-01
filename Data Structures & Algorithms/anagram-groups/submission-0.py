class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()
        results = []
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str not in hash_map:
                hash_map[sorted_str] = [string]
            else:
                hash_map[sorted_str].append(string)
        for sorted_str in hash_map.keys():
            results.append(hash_map[sorted_str])

        return results
            