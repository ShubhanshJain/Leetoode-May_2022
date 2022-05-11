class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        def helper(n, vowel):
            if n == 0:
                return 1
            
            res = 0
            for x in range(vowel, 5):
                res += helper(n-1, x)
            return res
        
        return helper(n, 0)