from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        mag_dic = defaultdict(int)
        
        for ch in set(magazine):
            mag_dic[ch] = 0

        for c in magazine:
            mag_dic[c] += 1


        for r in ransomNote:
            if mag_dic[r] == 0:
                return False
            else:
                mag_dic[r] -= 1

        return True



s = Solution()
print(s.canConstruct("aa", "aab"))