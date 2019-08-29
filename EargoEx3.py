class Solution:
    #prices is the input array of the prices
    def stockPrice(self, prices):
        #if we do not have prices, we return 0
        if not prices: return 0

        #let smallest price be the first element of the array
        smallest = prices[0]
        #initialize profit to 0
        profit = 0
        # ans[0] will have the day when we should buy and ans[1] will have day when we can sell
        ans = [1, 1]

        for i in range(1, len(prices)):
            #if the current price is more than smallest, find profit
            if prices[i] > smallest:
                #if current profit is greater than max profit then change it
                if prices[i] - smallest > profit:
                    profit = prices[i] - smallest
                    #update selling day
                    ans[1] = i+1
            #update the smallest price found so far
            if prices[i] < smallest:
                smallest = prices[i]
                #update buying day
                ans[0] = i+1
        #ultimately return the profit

        if ans[0] == ans[1]: return "You can neither get a profit nor a loss."
        if ans[0] > ans[1]: return "You can never get a profit with these prices."
        return "You can buy on day " + str(ans[0]) + " and sell on day " + str(ans[1]) + " to get a max profit of " + str(profit) + "."



if __name__=='__main__':
    solution = Solution()
    print(solution.stockPrice([3, 8, 8, 55, 38, 1, 7, 42, 54, 53]))
    print(solution.stockPrice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(solution.stockPrice([20, 19, 18, 17, 16, 15, 14, 13, 12, 11]))
    print(solution.stockPrice([2, 1, 3, 4, 6, 45, 9, 34, 21, 100]))
    print(solution.stockPrice([4, 4, 4, 4, 4, 4, 4, 4, 4, 4]))
