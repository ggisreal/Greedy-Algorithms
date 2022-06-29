Class Solution:
    # @Param A: List of integers
    # @return an integer
    
    def bulb(self, A):
        cost = 0
        
        for b in A:
            if cost % 2 == 0: b = b
            else: b = not b
                
            if b % 2 == 1: continue
            else: cost += 1
        
        return cost
