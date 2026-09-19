class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        Outp = 0
        for price in prices:
            buy = min(buy, price)
            sell = price
            earn = sell - buy
            Outp = max(Outp, earn)
        return Outp