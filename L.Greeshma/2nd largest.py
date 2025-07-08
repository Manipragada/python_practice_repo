lst = [1, 10, 3, 3, 4, 5, 10, 1, 1, 3]

# Step 1: Remove duplicates
unique_vals = list(set(lst))

# Step 2: Sort in descending order
unique_vals.sort(reverse=True)

# Step 3: Get second largest if it exists
if len(unique_vals) >= 2:
    second_largest = unique_vals[1]
    print("Second largest:", second_largest)
else:
    print("Second largest does not exist.")
