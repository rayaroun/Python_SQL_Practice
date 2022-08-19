from multiprocessing import reduction


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        temp = []

        for i, num in enumerate(nums):
            
            if i == 0:
                temp.append(nums[i])
            
            else:
                temp.append(num+temp[i-1])
        
        return temp


