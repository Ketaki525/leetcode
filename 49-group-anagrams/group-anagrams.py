class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        temp = dict()

        for s in strs:
            key = tuple(sorted(s))
            if key not in temp:
                temp[key] = []
            temp[key].append(s)
            
        return list(temp.values())