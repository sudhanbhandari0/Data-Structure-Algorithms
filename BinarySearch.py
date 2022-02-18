class Solution:
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1
        
        while(start<=end):
            mid = (end+start) //2
            if (nums[mid] ==target):
                return mid
            if (target <= nums[mid]):
                end = mid -1
            
            else:
                start = mid + 1
        return -1
               
nums = [-1,0,3,5,9,12]
target = 9