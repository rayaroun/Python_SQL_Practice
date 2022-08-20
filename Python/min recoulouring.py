class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        i=0
        recolour = k

        while i <= len(blocks)-k:

            tmp_str = blocks[i:i+k]

            w_count = tmp_str.count('W')

            if w_count < recolour:
                recolour = w_count

            i+=1
            

        return recolour


    
s = Solution()

print(s.minimumRecolors("WBWBBBW", 2))