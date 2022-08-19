#this is an effort to find a more efficient way to find the pivot. The left sum and the right sum doesn't have to be recalculated every time.  


class Solution(object):
    def pivotIndex(self, nums):

        ls, rs  = 0, sum(nums)

        for i , num in enumerate(nums):

            rs -= num

            if ls == rs:
                return i

            ls+=num

        return -1 

    
