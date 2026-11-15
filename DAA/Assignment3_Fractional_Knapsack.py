
# Assignment No. 3: Fractional Knapsack Using Greedy Method
# Aim: To solve the Fractional Knapsack problem and analyze
# its time and space complexity.

def fractional_knapsack(values, weights, capacity):
    n = len(values)

    # Calculate profit-to-weight ratio for each item
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i], i + 1))

    # Sort items by decreasing profit-to-weight ratio
    items.sort(reverse=True)

    total_profit = 0.0
    selected_items = []

    for ratio, value, weight, item_no in items:
        if capacity <= 0:
            break

        if weight <= capacity:
            # Take the complete item
            capacity -= weight
            total_profit += value
            selected_items.append((item_no, 1.0, value))
        else:
            # Take the fraction that fits
            fraction = capacity / weight
            profit = value * fraction
            total_profit += profit
            selected_items.append((item_no, fraction, profit))
            capacity = 0

    return total_profit, selected_items


# Main program
n = int(input("Enter the number of items: "))

values = []
weights = []

for i in range(n):
    print(f"\nItem {i + 1}:")
    value = float(input("Enter profit/value: "))
    weight = float(input("Enter weight: "))

    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")

    values.append(value)
    weights.append(weight)

capacity = float(input("\nEnter knapsack capacity: "))

if capacity < 0:
    raise ValueError("Capacity cannot be negative.")

max_profit, selected_items = fractional_knapsack(
    values, weights, capacity
)

print("\nSelected Items:")
for item_no, fraction, profit in selected_items:
    print(
        f"Item {item_no}: Fraction taken = {fraction:.2f}, "
        f"Profit obtained = {profit:.2f}"
    )

print(f"\nMaximum Profit: {max_profit:.2f}")

print("\nTime Complexity: O(n log n)")
print("Auxiliary Space Complexity: O(n)")
    
