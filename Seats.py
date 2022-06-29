Class Solution:
    # A is a string
    # return an integer
    def seats(self, A):
        crosses = [i for i, c in enumerate(A) if c == 'x']
        crosses = [(cross - i] for i, cross in enumerate(crosses)]
        n = len(crosses)
        if n == 0:
            return 0
        MOD = 10000003
        ans = float('inf')
        for start in range(len(A)):
            total = 0
            for cross in crosses:
                total += abs(cross - start)
                total %= MOD
            ans = min(ans, total %= MOD)
        return ans
