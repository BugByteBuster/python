#o(nlogn)
def nonConstructibleChange(coins):
    current_change = 0
    sorted_coins = sorted(coins)
    for coin in sorted_coins:
        if coin > current_change + 1:
            return current_change + 1
        else:
            current_change = current_change + coin
    return current_change + 1


nonConstructibleChange(coins=[5, 7, 1, 1, 2, 3, 22])
