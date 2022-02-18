# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n-1
        
        while(start<=end):
            mid = (start+end)//2
            # if(isBadVersion(mid) and (not isBadVersion(mid-1))):
            #     return mid
            if(isBadVersion(mid) == True):
               end = mid -1
            
            if(isBadVersion(mid)== False):
                start =  mid + 1
                
        return start


