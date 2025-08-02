#!/usr/bin/env python3
"""
Example usage of the python_utilities package.

This script demonstrates how to use the add_numbers function
with various inputs and error handling scenarios.
"""

import logging
import sys
import os

# Add the parent directory to the path to import our module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from python_utilities.math_utils import add_numbers, validate_number


def main():
    """Main function demonstrating the add_numbers functionality."""
    
    # Configure logging to see the function's internal logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    print("=== Python Utilities - Add Numbers Function Demo ===\n")
    
    # Basic usage examples
    print("1. Basic Addition Examples:")
    examples = [
        (2, 3),
        (2.5, 3.7),
        (-1, 1),
        (0, 0),
        (10, -5),
        (1e6, 2e6),
        (0.1, 0.2)
    ]
    
    for a, b in examples:
        try:
            result = add_numbers(a, b)
            print(f"   {a} + {b} = {result}")
        except Exception as e:
            print(f"   Error adding {a} + {b}: {e}")
    
    print("\n2. Error Handling Examples:")
    
    # Type errors
    print("   Type Errors:")
    error_examples = [
        ("2", 3),
        (2, "3"),
        (None, 5),
        ([1, 2], 3),
        ({"a": 1}, 2)
    ]
    
    for a, b in error_examples:
        try:
            result = add_numbers(a, b)
            print(f"   {a} + {b} = {result}")
        except Exception as e:
            print(f"   ❌ {type(e).__name__}: {e}")
    
    # Value errors (NaN and infinity)
    print("\n   Value Errors (NaN and Infinity):")
    special_values = [
        (float('nan'), 3),
        (2, float('nan')),
        (float('inf'), 3),
        (2, float('-inf'))
    ]
    
    for a, b in special_values:
        try:
            result = add_numbers(a, b)
            print(f"   {a} + {b} = {result}")
        except Exception as e:
            print(f"   ❌ {type(e).__name__}: {e}")
    
    print("\n3. Number Validation Examples:")
    validation_examples = [
        5,
        3.14,
        "not a number",
        float('nan'),
        float('inf'),
        None,
        [1, 2, 3]
    ]
    
    for value in validation_examples:
        is_valid = validate_number(value)
        print(f"   validate_number({value}) = {is_valid}")
    
    print("\n4. Real-world Example - Calculate Total:")
    prices = [19.99, 25.50, 12.75, 8.25, 15.00]
    total = 0
    
    print(f"   Calculating total for prices: {prices}")
    for i, price in enumerate(prices):
        try:
            total = add_numbers(total, price)
            print(f"   Step {i+1}: {total:.2f}")
        except Exception as e:
            print(f"   Error adding price {price}: {e}")
    
    print(f"   Final total: ${total:.2f}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()

