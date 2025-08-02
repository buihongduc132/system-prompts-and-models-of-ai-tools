# Python Utilities

A comprehensive Python package providing utility functions for common mathematical operations with robust error handling and logging.

## Features

- ✅ **Type Safety**: Full type hints for Python 3.8+ compatibility
- ✅ **Error Handling**: Comprehensive error handling for edge cases
- ✅ **Logging**: Built-in logging for debugging and monitoring
- ✅ **Testing**: Extensive unit test coverage
- ✅ **Documentation**: Complete docstrings following PEP 257
- ✅ **PEP 8 Compliant**: Follows Python style guidelines

## Installation

Since this is a local utility package, you can import it directly:

```python
from python_utilities import add_numbers
```

## Usage

### Basic Addition

```python
from python_utilities.math_utils import add_numbers

# Add two integers
result = add_numbers(2, 3)
print(result)  # Output: 5

# Add two floats
result = add_numbers(2.5, 3.7)
print(result)  # Output: 6.2

# Add mixed types
result = add_numbers(2, 3.5)
print(result)  # Output: 5.5
```

### Error Handling

The function includes comprehensive error handling:

```python
from python_utilities.math_utils import add_numbers

# Type errors
try:
    add_numbers("2", 3)
except TypeError as e:
    print(f"Error: {e}")

# Value errors (NaN, infinity)
try:
    add_numbers(float('nan'), 3)
except ValueError as e:
    print(f"Error: {e}")

# Overflow errors
try:
    import sys
    very_large = sys.float_info.max / 2
    add_numbers(very_large, very_large)
except OverflowError as e:
    print(f"Error: {e}")
```

### Logging

Enable logging to see detailed operation information:

```python
import logging
from python_utilities.math_utils import add_numbers

# Configure logging
logging.basicConfig(level=logging.INFO)

# This will log the operation
result = add_numbers(2, 3)
```

## API Reference

### `add_numbers(a, b)`

Add two numbers together with comprehensive error handling.

**Parameters:**
- `a` (Union[int, float]): The first number to add
- `b` (Union[int, float]): The second number to add

**Returns:**
- `Union[int, float]`: The sum of the two input numbers

**Raises:**
- `TypeError`: If either input is not a number (int or float)
- `ValueError`: If either input is NaN or infinite
- `OverflowError`: If the result would cause an overflow

**Examples:**
```python
>>> add_numbers(2, 3)
5
>>> add_numbers(2.5, 3.7)
6.2
>>> add_numbers(-1, 1)
0
```

### `validate_number(value)`

Validate if a value is a valid number for mathematical operations.

**Parameters:**
- `value` (Any): The value to validate

**Returns:**
- `bool`: True if the value is a valid number, False otherwise

## Testing

Run the comprehensive test suite:

```bash
# Run tests from the project root
python -m pytest tests/ -v

# Or run with unittest
python -m unittest tests.test_math_utils -v

# Run with coverage
python -m coverage run -m unittest tests.test_math_utils
python -m coverage report
```

### Test Coverage

The test suite includes:

- ✅ Basic addition operations (integers, floats, mixed types)
- ✅ Edge cases (zero, negative numbers, very large/small numbers)
- ✅ Error conditions (invalid types, NaN, infinity, overflow)
- ✅ Logging verification
- ✅ Integration tests
- ✅ Real-world scenarios

## Development

### Code Style

This package follows PEP 8 style guidelines. You can check compliance with:

```bash
flake8 python_utilities/
black --check python_utilities/
```

### Type Checking

Type hints are included for all functions. Check with:

```bash
mypy python_utilities/
```

## Requirements

- Python 3.8+
- No external dependencies (uses only standard library)

## License

This code is provided as-is for educational and utility purposes.

## Contributing

When contributing:

1. Follow PEP 8 style guidelines
2. Add comprehensive tests for new functionality
3. Include proper type hints
4. Update documentation
5. Ensure all tests pass

## Changelog

### Version 1.0.0
- Initial implementation of `add_numbers` function
- Comprehensive error handling and logging
- Full test suite with extensive coverage
- Complete documentation

