from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #double pointer: one moves 1 at a time another 2 steps
        #both starts at zero
        # s(1step) & f(2 steops)
        # forced to buy or sell?
        #so pairwise: if i+1 > i then buy on i and sell on i+1
        # print out profit
        profit = 0
        for i in range (0, len(prices)-1):
            
            if(prices[i] < prices[i+1]):
                
                profit += prices[i+1] - prices [i]
            else: continue
        return profit
        
def main():
    prices = [7, 3, 2, 1, 9, 5]
    sol = Solution()
    results = sol.maxProfit(prices)
    print({results})
main()
