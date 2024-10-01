class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        n = len(word1)
        m = len(word2)
        res = ""
        while i < min(n,m):
            res += word1[i] + word2[i]
            i += 1
        if n > m:
            while i < n:
                res += word1[i]
                i += 1
        if m > n:
            while i < m:
                res += word2[i]
                i += 1
        return res
        