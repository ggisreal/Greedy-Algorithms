Class Solution:
    # @Param A: list of integers
    # @ return an integer
    
    def maxp(self, A):
        A = sorted()
        
        hi3 = A[-1] * A[-2] * A[-3]
        lo2hi1 = A[-1] * A[0] * A[1]
    
    return max(hi1, lo2hi1)
