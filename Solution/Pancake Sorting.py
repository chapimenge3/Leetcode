class Solution:

    def flip(self, arr, r, n):
        l = arr[:n]
        ll = l[:r+1][::-1] + l[r+1:]
        rev = ll[::-1] + arr[n:]
        return rev 

            
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        l = sorted(arr)
        
        if l == arr:
            return []
        
        res = []
        
        while n > 1:
            mx = max(arr[:n])
            ind = arr.index(mx)
            
            arr = self.flip(arr, ind, n)
            if ind:
                res.append(ind+1)
            
            res.append(n)
            n -= 1
        
        return res
        
        