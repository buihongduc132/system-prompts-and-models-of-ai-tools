"""
Mathematical utility functions.

This module provides basic mathematical operations with comprehensive error handling
and logging capabilities.
"""

import logging
from typing import Union, Any

# Configure logging
logger = logging.getLogger(__name__)


def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers together with comprehensive error handling.
    
    This function accepts two numeric values (integers or floats) and returns
    their sum. It includes proper type checking, error handling, and logging.
    
    Args:
        a (Union[int, float]): The first number to add
        b (Union[int, float]): The second number to add
        
    Returns:
        Union[int, float]: The sum of the two input numbers
        
    Raises:
        TypeError: If either input is not a number (int or float)
        ValueError: If either input is NaN or infinite
        OverflowError: If the result would cause an overflow
        
    Examples:
        >>> add_numbers(2, 3)
        5
        >>> add_numbers(2.5, 3.7)
        6.2
        >>> add_numbers(-1, 1)
        0
        >>> add_numbers(0, 0)
        0
    """
    logger.debug(f"add_numbers called with arguments: a={a}, b={b}")
    
    # Type validation
    if not isinstance(a, (int, float)):
        error_msg = f"First argument must be a number (int or float), got {type(a).__name__}"
        logger.error(error_msg)
        raise TypeError(error_msg)
    
    if not isinstance(b, (int, float)):
        error_msg = f"Second argument must be a number (int or float), got {type(b).__name__}"
        logger.error(error_msg)
        raise TypeError(error_msg)
    
    # Check for NaN values
    import math
    if math.isnan(a):
        error_msg = "First argument cannot be NaN"
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    if math.isnan(b):
        error_msg = "Second argument cannot be NaN"
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    # Check for infinite values
    if math.isinf(a):
        error_msg = "First argument cannot be infinite"
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    if math.isinf(b):
        error_msg = "Second argument cannot be infinite"
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    try:
        # Perform the addition
        result = a + b
        
        # Check for overflow (result is infinite)
        if math.isinf(result):
            error_msg = f"Addition overflow: {a} + {b} results in infinite value"
            logger.error(error_msg)
            raise OverflowError(error_msg)
        
        logger.info(f"Successfully added {a} + {b} = {result}")
        return result
        
    except OverflowError:
        # Re-raise OverflowError without wrapping it
        raise
    except Exception as e:
        error_msg = f"Unexpected error during addition: {str(e)}"
        logger.error(error_msg)
        raise RuntimeError(error_msg) from e


def validate_number(value: Any) -> bool:
    """
    Validate if a value is a valid number for mathematical operations.
    
    Args:
        value (Any): The value to validate
        
    Returns:
        bool: True if the value is a valid number, False otherwise
    """
    # Check if it's a basic numeric type (int or float, but not complex)
    if not isinstance(value, (int, float)) or isinstance(value, complex):
        return False
    
    import math
    if math.isnan(value) or math.isinf(value):
        return False
    
    return True
