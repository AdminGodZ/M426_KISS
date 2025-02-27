# Bad Implementation (Not following KISS)
# This file shows an overcomplicated way to calculate shopping cart total

"""
Anti-KISS Implementation Plan:

Overcomplicated Shopping Cart Calculator
- Same task: calculate total price and apply discount
- But with unnecessary complexity

Why this is bad KISS:
1. Uses a class when a function would do
2. Stores prices in complex dictionary instead of list
3. Splits simple math into multiple methods
4. Adds unnecessary validation
5. Creates custom exceptions for no reason

Example structure:

class ShoppingCartItem:
    def __init__(self, price, item_id, category):
        # Unnecessary attributes
        pass

class ShoppingCartManager:
    def __init__(self):
        # Complex dictionary structure
        self.items = {}
        
    def add_item(self, item):
        # Unnecessary validation
        pass
        
    def calculate_subtotal(self):
        # Could be one line, split into many
        pass
        
    def apply_discount(self, subtotal):
        # Overcomplicated discount logic
        pass
        
    def get_total(self):
        # Calls multiple methods for simple math
        pass

Example usage:
manager = ShoppingCartManager()
manager.add_item(ShoppingCartItem(10.99, "A1", "food"))
total = manager.get_total()
