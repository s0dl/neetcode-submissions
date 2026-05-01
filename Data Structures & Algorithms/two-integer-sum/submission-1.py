class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = dict()
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in numsHash.keys():
                return [numsHash[compl], i]
            numsHash[nums[i]] = i
        return []