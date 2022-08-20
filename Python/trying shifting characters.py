
from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        
        for shift in shifts:

            i,j = shift[0],shift[1]

            if shift[2] == 1:
                k = 1
            else:
                k = -1


            ls = list(s)

            for it in range(i,j+1):

                val = ord(ls[it])+k
                
                if val > 122:
                    temp = 96 + (val - 122)
                    ls[it] = chr(ord(chr(temp)))
                elif val < 97:
                    temp = 123 - (97 - val)
                    ls[it] = chr(ord(chr(temp)))
                else:
                    ls[it] = chr(ord(ls[it]) + k)

            s = ''.join(ls)

        return s


s = Solution()

print(s.shiftingLetters("abc", [[0,1,0],[1,2,1],[0,2,1]]))

        #  = ''.join(chr(ord(char)+1) for char in string) 