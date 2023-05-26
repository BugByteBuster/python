#redo
def nonConstructibleChange(coins):
    coins = sorted(coins)
    current_change = 0
    for i in coins:
        if i > current_change + 1:
            return current_change + 1
        current_change += i
    return current_change + 1