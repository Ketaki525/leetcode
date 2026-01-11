class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {val: nums.count(val) for val in set(nums)}
        
        sort_dict = {key: val for key,val in sorted(d.items(), key = lambda item : item[1], reverse=True)}
        res = list(sort_dict.keys())[:k]

        return res