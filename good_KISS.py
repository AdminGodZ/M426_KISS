# Good Implementation following KISS Principle
# This file shows a simple way to calculate shopping cart total

"""
KISS Implementation Plan:

Simple Shopping Cart Calculator
- Takes a list of prices
- Adds them up
- Applies a discount if total is over 100
- Returns final total

Why this is good KISS:
1. Simple list for prices
2. One function that does one thing
3. Clear logic without unnecessary steps
4. Easy to understand and modify
5. No complex classes needed

Example structure:

def calculate_total(prices):
    # Sum all prices
    # Apply discount if needed
    # Return total
    pass

Example usage:
prices = [10.99, 24.99, 5.99]
total = calculate_total(prices)
print(f"Total: ${total:.2f}")
"""
