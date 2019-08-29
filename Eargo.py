class Solution:
    def change(self, amount):
        arr = set([25, 10, 5, 1])
        #resultant arr which gives the values of the number of coins of each denomination
        res = []

        # we iterate over the coin denominations we have
        for coin_val in arr:
            # if amount >= coin_val, do integer division to find out the number of coins
            if amount >= coin_val:
                #add to array the number of coins which we get by amount//coin_val
                res.append(amount//coin_val)
            else:
                # if coin value is greater than amount we add 0 to the res array
                res.append(0)
            #find out the remaining amount
            amount = amount % coin_val
        return res
        

if __name__=="__main__":
    solution = Solution()
    print(solution.change(83))
    print(solution.change(1000))
    print(solution.change(7))
    print(solution.change(3))
