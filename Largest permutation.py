Class Solution:
    # @Param A: list of integers
    # @Param B: integer
    # @return a list of integers
    
    def (self, A, B):
        i = 0
        max_ = len(A)
        dic = {x:i for i, x in enumerate(A)}
        while B and i < len(A):
            j = dic[max_]
            if i == j:
                pass
            else:
                A[i], A[j] = A[j], A[i]
                dic[A[i]], dic[A[j]] = dic[A[j]], dic[A[j]]
                B -= 1
            i += 1
            max_ -= 1
        return A
