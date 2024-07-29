import module_ListFunction as mlf

# Create lists using list comprehension for various scenarios
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
odd_numbers = [x for x in range(1, 21) if x % 2 != 0]
squares = [x**2 for x in range(1, 11)]
mixed_numbers = [3, 5, 7, 2, 9, 4, 1, 8, 6]

# Demonstrate the use of module_ListFunction functions
print("Even numbers:", even_numbers)
print("Max:", mlf.find_max(even_numbers))
print("Min:", mlf.find_min(even_numbers))
print("Sum:", mlf.calculate_sum(even_numbers))
print("Average:", mlf.calculate_average(even_numbers))
print("Median:", mlf.find_median(even_numbers))

print("\nOdd numbers:", odd_numbers)
print("Max:", mlf.find_max(odd_numbers))
print("Min:", mlf.find_min(odd_numbers))
print("Sum:", mlf.calculate_sum(odd_numbers))
print("Average:", mlf.calculate_average(odd_numbers))
print("Median:", mlf.find_median(odd_numbers))

print("\nSquares:", squares)
print("Max:", mlf.find_max(squares))
print("Min:", mlf.find_min(squares))
print("Sum:", mlf.calculate_sum(squares))
print("Average:", mlf.calculate_average(squares))
print("Median:", mlf.find_median(squares))

print("\nMixed numbers:", mixed_numbers)
print("Max:", mlf.find_max(mixed_numbers))
print("Min:", mlf.find_min(mixed_numbers))
print("Sum:", mlf.calculate_sum(mixed_numbers))
print("Average:", mlf.calculate_average(mixed_numbers))
print("Median:", mlf.find_median(mixed_numbers))
