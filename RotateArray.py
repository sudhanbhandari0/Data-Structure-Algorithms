class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        if len(nums) > k:
            nums[:] = nums[-k:] + nums[:-k]
            
        else:
             for i in range(k):
                    nums[:]=nums[-1:]+nums[:-1]

        
        """
        Do not return anything, modify nums in-place instead.
        """