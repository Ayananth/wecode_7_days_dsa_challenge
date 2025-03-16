class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums.extend([0] * zeros)  