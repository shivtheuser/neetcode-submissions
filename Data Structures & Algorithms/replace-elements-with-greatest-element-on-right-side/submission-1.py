class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_most = -1
        for i in range(len(arr)-1,-1,-1):
            current = arr[i]
            if i == len(arr)-1:
                arr[i] = right_most
                right_most = max(right_most,current)
            else:
                arr[i] = right_most
                right_most = max(right_most,current)
        return arr