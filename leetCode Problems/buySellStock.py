def maxProfit(prices):
    min_price = float("inf")
    max_profit = 0
    for price in prices:
        #Update min price if current price is lower
        if (price < min_price):
            min_price = price
        #Calculate profit if we sold today
        max_profit = max(max_profit,price - min_price)
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
