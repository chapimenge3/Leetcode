class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, len(prices) - 1
        mx = 0
        while i < j:
            dif = prices[j] - prices[i]
            if prices[j] < prices[i]:
                i += 1
            else:
                j -= 1

            if dif > 0:
                mx = max(mx, dif)
        
        return mx
            
