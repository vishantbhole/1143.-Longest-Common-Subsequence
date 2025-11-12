
#1143. Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1 , -1):
            for j in range(len(text2) - 1, -1, -1):
