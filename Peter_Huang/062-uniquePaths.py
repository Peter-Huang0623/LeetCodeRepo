class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        


if __name__ == "__main__":
    s = Solution()
    res = s.uniquePaths(23, 12)
    print(res)