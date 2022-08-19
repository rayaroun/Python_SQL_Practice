from collections import defaultdict
from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(set(s)) != len(set(t)):
            return False
        
        
        d = defaultdict(str)
        
        print(d)
        # return True if len(set(s)) == len(set(t)) else False

        for i,ch in enumerate(s):

            d[ch] += t[i]

        # print(d)


        for value in d.values():
            if len(set(value)) > 1 :
                return False
        
        return True



# this one was good 





x = Solution()


print(x.isIsomorphic("bbbaaaba", "aaabbbba"))