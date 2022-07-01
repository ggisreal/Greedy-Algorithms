Class Solutoin:
    # A: tuple of integers
    # B: tuple of integers
    # return an integer
    def canCompleteCircuit(self, A, B):
        n = len(A)
        curr = start = 0
        for i, (g, c) in enumerate(zip(A * 2, B * 2):
            if i == start + n:
                return start
        curr += g - c
        if curr < 0:
            start = i + 1
            curr = 0
        return -1
