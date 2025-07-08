numbers = [1, 2, 3, 4, 5, 6]

# Step 1: Get even numbers
even_numbers = [n for n in numbers if n % 2 == 0]

# Step 2: Calculate sum of squares of even numbers
sum_of_squares = sum(n**2 for n in even_numbers)

print("Even numbers:", even_numbers)
print("Sum of squares of even numbers:", sum_of_squares)
