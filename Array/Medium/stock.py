# Buy and sell stock at maximum profit

def maxprofit(arr):
    n = len(arr)
    profit = 0

    for i in range(n-1):
        for j in range(i+1, n):
            profit = max(profit, arr[j]-arr[i])

    print("The maximum profit is ",profit)


if __name__ == "__main__":
    prices = [10,15,7,8,56,9,32,45]

    maxprofit(prices)