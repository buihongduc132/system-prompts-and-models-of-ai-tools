"""
Comprehensive unit tests for math_utils module.

This module contains extensive tests for the add_numbers function,
covering normal cases, edge cases, and error conditions.
"""

import unittest
import math
import logging
from unittest.mock import patch
import sys
import os

# Add the parent directory to the path to import our module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from python_utilities.math_utils import add_numbers, validate_number


class TestAddNumbers(unittest.TestCase):
    """Test cases for the add_numbers function."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Configure logging for tests
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger('python_utilities.math_utils')
    
    def test_add_positive_integers(self):
        """Test addition of positive integers."""
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(10, 20), 30)
        self.assertEqual(add_numbers(1, 1), 2)
    
    def test_add_negative_integers(self):
        """Test addition of negative integers."""
        self.assertEqual(add_numbers(-2, -3), -5)
        self.assertEqual(add_numbers(-10, -20), -30)
        self.assertEqual(add_numbers(-1, -1), -2)
    
    def test_add_mixed_sign_integers(self):
        """Test addition of integers with different signs."""
        self.assertEqual(add_numbers(-2, 3), 1)
        self.assertEqual(add_numbers(10, -5), 5)
        self.assertEqual(add_numbers(-10, 10), 0)
    
    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(5, 0), 5)
        self.assertEqual(add_numbers(0, -3), -3)
    
    def test_add_floats(self):
        """Test addition of floating-point numbers."""
        self.assertAlmostEqual(add_numbers(2.5, 3.7), 6.2, places=10)
        self.assertAlmostEqual(add_numbers(-1.5, 2.5), 1.0, places=10)
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3, places=10)
    
    def test_add_mixed_types(self):
        """Test addition of integers and floats."""
        self.assertAlmostEqual(add_numbers(2, 3.5), 5.5, places=10)
        self.assertAlmostEqual(add_numbers(2.5, 3), 5.5, places=10)
        self.assertAlmostEqual(add_numbers(-2, 3.5), 1.5, places=10)
    
    def test_add_large_numbers(self):
        """Test addition of large numbers."""
        large_num = 10**15
        self.assertEqual(add_numbers(large_num, large_num), 2 * large_num)
        self.assertEqual(add_numbers(large_num, 1), large_num + 1)
    
    def test_add_small_numbers(self):
        """Test addition of very small numbers."""
        small_num = 1e-15
        self.assertAlmostEqual(add_numbers(small_num, small_num), 2 * small_num, places=20)
        self.assertAlmostEqual(add_numbers(small_num, 0), small_num, places=20)
    
    def test_type_error_first_argument(self):
        """Test TypeError for invalid first argument type."""
        with self.assertRaises(TypeError) as context:
            add_numbers("2", 3)
        self.assertIn("First argument must be a number", str(context.exception))
        
        with self.assertRaises(TypeError):
            add_numbers(None, 3)
        
        with self.assertRaises(TypeError):
            add_numbers([1, 2], 3)
        
        with self.assertRaises(TypeError):
            add_numbers({"a": 1}, 3)
    
    def test_type_error_second_argument(self):
        """Test TypeError for invalid second argument type."""
        with self.assertRaises(TypeError) as context:
            add_numbers(2, "3")
        self.assertIn("Second argument must be a number", str(context.exception))
        
        with self.assertRaises(TypeError):
            add_numbers(2, None)
        
        with self.assertRaises(TypeError):
            add_numbers(2, [1, 2])
        
        with self.assertRaises(TypeError):
            add_numbers(2, {"a": 1})
    
    def test_nan_values(self):
        """Test ValueError for NaN inputs."""
        with self.assertRaises(ValueError) as context:
            add_numbers(float('nan'), 3)
        self.assertIn("First argument cannot be NaN", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            add_numbers(2, float('nan'))
        self.assertIn("Second argument cannot be NaN", str(context.exception))
    
    def test_infinite_values(self):
        """Test ValueError for infinite inputs."""
        with self.assertRaises(ValueError) as context:
            add_numbers(float('inf'), 3)
        self.assertIn("First argument cannot be infinite", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            add_numbers(2, float('inf'))
        self.assertIn("Second argument cannot be infinite", str(context.exception))
        
        with self.assertRaises(ValueError):
            add_numbers(float('-inf'), 3)
        
        with self.assertRaises(ValueError):
            add_numbers(2, float('-inf'))
    
    def test_overflow_error(self):
        """Test OverflowError for results that would overflow."""
        # Create a scenario that would result in infinity
        very_large = sys.float_info.max
        with self.assertRaises(OverflowError) as context:
            add_numbers(very_large, very_large)
        self.assertIn("Addition overflow", str(context.exception))
    
    @patch('python_utilities.math_utils.logger')
    def test_logging_success(self, mock_logger):
        """Test that successful operations are logged."""
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)
        mock_logger.debug.assert_called_with("add_numbers called with arguments: a=2, b=3")
        mock_logger.info.assert_called_with("Successfully added 2 + 3 = 5")
    
    @patch('python_utilities.math_utils.logger')
    def test_logging_error(self, mock_logger):
        """Test that errors are logged."""
        with self.assertRaises(TypeError):
            add_numbers("invalid", 3)
        mock_logger.error.assert_called()
    
    def test_return_type_preservation(self):
        """Test that return type is appropriate for inputs."""
        # Integer + Integer should return integer when possible
        result = add_numbers(2, 3)
        self.assertIsInstance(result, int)
        
        # Any float involved should return float
        result = add_numbers(2.0, 3)
        self.assertIsInstance(result, float)
        
        result = add_numbers(2, 3.0)
        self.assertIsInstance(result, float)
        
        result = add_numbers(2.5, 3.7)
        self.assertIsInstance(result, float)


class TestValidateNumber(unittest.TestCase):
    """Test cases for the validate_number helper function."""
    
    def test_valid_integers(self):
        """Test validation of valid integers."""
        self.assertTrue(validate_number(0))
        self.assertTrue(validate_number(1))
        self.assertTrue(validate_number(-1))
        self.assertTrue(validate_number(1000))
    
    def test_valid_floats(self):
        """Test validation of valid floats."""
        self.assertTrue(validate_number(0.0))
        self.assertTrue(validate_number(1.5))
        self.assertTrue(validate_number(-2.7))
        self.assertTrue(validate_number(1e-10))
    
    def test_invalid_types(self):
        """Test validation of invalid types."""
        self.assertFalse(validate_number("1"))
        self.assertFalse(validate_number(None))
        self.assertFalse(validate_number([1]))
        self.assertFalse(validate_number({"a": 1}))
        # Note: In Python, bool is a subclass of int, so True/False are valid numbers
        # We'll test with other invalid types instead
        self.assertFalse(validate_number(complex(1, 2)))
    
    def test_invalid_special_values(self):
        """Test validation of special float values."""
        self.assertFalse(validate_number(float('nan')))
        self.assertFalse(validate_number(float('inf')))
        self.assertFalse(validate_number(float('-inf')))


class TestIntegration(unittest.TestCase):
    """Integration tests for the math_utils module."""
    
    def test_multiple_operations(self):
        """Test multiple sequential operations."""
        result1 = add_numbers(1, 2)
        result2 = add_numbers(result1, 3)
        result3 = add_numbers(result2, 4)
        self.assertEqual(result3, 10)
    
    def test_chained_operations_with_floats(self):
        """Test chained operations with floating-point numbers."""
        result1 = add_numbers(1.1, 2.2)
        result2 = add_numbers(result1, 3.3)
        self.assertAlmostEqual(result2, 6.6, places=10)
    
    def test_real_world_scenario(self):
        """Test a real-world scenario like calculating a total."""
        prices = [19.99, 25.50, 12.75, 8.25]
        total = 0
        for price in prices:
            total = add_numbers(total, price)
        self.assertAlmostEqual(total, 66.49, places=2)


if __name__ == '__main__':
    # Configure logging for test runs
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Run the tests
    unittest.main(verbosity=2)
