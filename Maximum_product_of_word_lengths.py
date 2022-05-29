class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lookup = defaultdict(int)
        
        for w in words:
            bitw = 0
            for c in w:
                bitw |= (1<<ord(c)-97)
            lookup[w] = bitw
            
        def dont_share(s,t):
            if lookup[s] & lookup[t]:
                return False
            return True
        
        maxx = 0
        for i in words:
            for j in words:
                if dont_share(i,j):
                    maxx = max(maxx, len(i)*len(j))
                    
        return maxx            