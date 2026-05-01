class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = dict()
        tMap = dict()

        for char in s:
            if char not in sMap:
                sMap[char] = 1
            else:
                sMap[char] += 1
        
        for char in t:
            if char not in tMap:
                tMap[char] = 1
            else:
                tMap[char] += 1
        
        if sMap == tMap:
            return True
        else:
            return False