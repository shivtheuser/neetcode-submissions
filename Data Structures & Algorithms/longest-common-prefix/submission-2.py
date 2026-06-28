class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j = 0
        ans = ""
        while j<len(strs[0]):
            i = 0
            ch = strs[i][j]
            while i<len(strs):
                if j>=len(strs[i]) or ch != strs[i][j]:
                    return ans
                i+=1
            ans += ch
            j+=1
        return ans