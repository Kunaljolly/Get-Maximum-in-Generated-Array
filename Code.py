class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        t = [0,1]
        for x in range(2,n+1):
            if x%2 ==0:
                t.append(t[x//2])
                print(t[x//2])
            else:
                t.append(t[x//2]+t[(x//2)+1])
                print(t[x//2]+t[(x//2)+1])

        return max(t)
