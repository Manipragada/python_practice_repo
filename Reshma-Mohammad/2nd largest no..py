numbers = [1, 10, 3, 3, 4, 5, 10, 1, 1, 3]

# Use set to remove duplicates
unique_numbers = list(set(numbers))

# Sort in descending order
unique_numbers.sort(reverse=True)

# Get the second largest
if len(unique_numbers) >= 2:
    second_largest = unique_numbers[1]
    print("Second largest number:", second_largest)
else:
    print("List does not have a second largest number.")
