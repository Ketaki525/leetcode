class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        n = len(nums)

        for i in range(0,n):
            if nums[i] == val:
                nums[i] = -1

        nums.sort(reverse = True)

        k = 0
        for i in range(0,n):
            if nums[i] != -1:
                k += 1
        return k

        