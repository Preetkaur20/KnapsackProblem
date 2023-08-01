def fractional_knapsack(items, capacity):
    # Calculate value-to-weight ratio for each item
    for i, (weight, value) in enumerate(items):
        items[i] = (weight, value, value / weight)

    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    knapsack = []

    for weight, value, ratio in items:
        if capacity == 0:
            break

        # Take the whole item if possible
        if weight <= capacity:
            knapsack.append((weight, value))
            total_value += value
            capacity -= weight
        else:
            # Take a fraction of the item to fill the remaining capacity
            fraction = capacity / weight
            knapsack.append((capacity, value * fraction))
            total_value += value * fraction
            capacity = 0

    return total_value, knapsack

# Example usage:
items = [(10, 60), (20, 100), (30, 120)]
capacity = 50
max_value, knapsack_items = fractional_knapsack(items, capacity)

print("Maximum value in the knapsack:", max_value)
print("Selected items in the knapsack:")
for weight, value in knapsack_items:
    print(f"Weight: {weight}, Value: {value}")



