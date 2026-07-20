class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_lis = []
        for i in range(0,len(arr)-1):
            maxi = 0
            for j in range(i+1,len(arr)):
                maxi = max(arr[j],maxi)
            new_lis.append(maxi)
            
        new_lis.append(-1)
        return new_lis
    
        