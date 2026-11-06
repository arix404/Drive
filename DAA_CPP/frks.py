
n = int(input("Enter number of items: "))

profit = []
weight = []

for i in range(n):
    p = int(input("Enter profit: "))
    w = int(input("Enter weight: "))
    profit.append(p)
    weight.append(w)

capacity = int(input("Enter knapsack capacity: "))

# Calculate profit/weight ratio
ratio = []

for i in range(n):
    ratio.append(profit[i] / weight[i])

# Sort items by ratio in descending order
items = sorted(zip(ratio, profit, weight), reverse=True)

total_profit = 0

for r, p, w in items:
    if capacity >= w:
        total_profit += p
        capacity -= w
    else:
        total_profit += r * capacity
        break

print("Maximum Profit:", total_profit)
