
# Assignment No. 4: 0/1 Knapsack Using Dynamic Programming
# Aim: To solve the 0/1 Knapsack problem and analyze
# its time and space complexity.

def knapsack(weights, profits, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the table using dynamic programming
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected items by tracing the DP table
    selected_items = []
    w = capacity

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]

    selected_items.reverse()

    return dp[n][capacity], selected_items, dp


# Main program
n = int(input("Enter the number of items: "))

weights = []
profits = []

for i in range(n):
    print(f"\nItem {i + 1}:")
    weight = int(input("Enter weight: "))
    profit = int(input("Enter profit: "))

    if weight <= 0:
        raise ValueError("Item weight must be positive.")

    weights.append(weight)
    profits.append(profit)

capacity = int(input("\nEnter knapsack capacity: "))

if capacity < 0:
    raise ValueError("Capacity cannot be negative.")

max_profit, selected_items, dp = knapsack(
    weights, profits, capacity
)

print("\nDynamic Programming Table:")
for row in dp:
    print(row)

print("\nSelected Items:", selected_items)
print("Maximum Profit:", max_profit)

print("\nTime Complexity: O(n * W)")
print("Space Complexity: O(n * W)")
