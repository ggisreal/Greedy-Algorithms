Class Solution:
    # @Param A: list of list of integers
    # @return an integer 
    def solve(self, A):
        data = []
        for s, e in A:
            data.append(s, 1)
            data.append(e, -1)
        curr = 0
        count = 0
        data.sort()
        for _, v in data:
            curr += v
            count = max(count, curr)
        
        return count
