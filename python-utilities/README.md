# Timestamp Utilities

A simple, robust Python utility for generating current timestamps in various formats with comprehensive error handling and logging.

## Features

- 🕒 **Multiple Format Support**: UNIX, ISO8601, Human-readable, and custom formats
- 🛡️ **Comprehensive Error Handling**: Robust error handling with custom exceptions
- 📝 **Extensive Logging**: Built-in logging for debugging and monitoring
- 🧪 **Fully Tested**: 100% test coverage with comprehensive unit tests
- 🐍 **Python 3.8+ Compatible**: Works with modern Python versions
- 📚 **Type Hints**: Full type annotation support
- 🚀 **Zero Dependencies**: Uses only Python standard library

## Installation

```bash
pip install -e .
```

For development dependencies:
```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from timestamp_utils import get_current_timestamp, TimestampFormat

# Get UNIX timestamp (default)
unix_time = get_current_timestamp()
print(unix_time)  # 1704067200.123456

# Get ISO8601 formatted timestamp
iso_time = get_current_timestamp(TimestampFormat.ISO8601)
print(iso_time)  # '2024-01-01T00:00:00.123456+00:00'

# Get human-readable timestamp
readable_time = get_current_timestamp(TimestampFormat.HUMAN_READABLE)
print(readable_time)  # 'Monday, January 01, 2024 at 12:00:00 AM UTC'

# Get custom formatted timestamp
custom_time = get_current_timestamp(
    TimestampFormat.CUSTOM, 
    custom_format='%Y-%m-%d %H:%M:%S'
)
print(custom_time)  # '2024-01-01 00:00:00'
```

## API Reference

### Main Functions

#### `get_current_timestamp(format_type, custom_format, timezone_aware)`

Get the current timestamp in the specified format.

**Parameters:**
- `format_type` (TimestampFormat): The format to return the timestamp in
- `custom_format` (Optional[str]): Custom format string for datetime formatting
- `timezone_aware` (bool): Whether to include timezone information (default: True)

**Returns:**
- `Union[int, float, str]`: The current timestamp in the requested format

**Raises:**
- `TimestampError`: If there's an error generating the timestamp
- `ValueError`: If custom_format is required but not provided
- `TypeError`: If invalid format_type is provided

### Convenience Functions

#### `get_unix_timestamp()`
Returns the current UNIX timestamp as a float.

#### `get_iso_timestamp(utc=True)`
Returns the current timestamp in ISO 8601 format.

#### `get_human_readable_timestamp()`
Returns the current timestamp in human-readable format.

### Supported Formats

- **UNIX**: Seconds since epoch (float)
- **ISO8601**: ISO 8601 formatted string with timezone
- **ISO8601_UTC**: ISO 8601 formatted string in UTC
- **HUMAN_READABLE**: Human-readable format
- **CUSTOM**: Custom format using strftime patterns

### Error Handling

The library provides comprehensive error handling:

- `TimestampError`: Custom exception for timestamp-related errors
- Handles system errors (OSError, OverflowError)
- Validates input parameters
- Provides detailed error messages

## Examples

### Basic Usage

```python
from timestamp_utils import get_current_timestamp, TimestampFormat

# Different format examples
formats = [
    TimestampFormat.UNIX,
    TimestampFormat.ISO8601,
    TimestampFormat.ISO8601_UTC,
    TimestampFormat.HUMAN_READABLE
]

for fmt in formats:
    timestamp = get_current_timestamp(fmt)
    print(f"{fmt.value}: {timestamp}")
```

### Custom Formatting

```python
from timestamp_utils import get_current_timestamp, TimestampFormat

# Various custom formats
custom_formats = [
    '%Y-%m-%d',                    # 2024-01-01
    '%Y-%m-%d %H:%M:%S',          # 2024-01-01 00:00:00
    '%B %d, %Y',                  # January 01, 2024
    '%A, %B %d, %Y at %I:%M %p'   # Monday, January 01, 2024 at 12:00 AM
]

for fmt in custom_formats:
    timestamp = get_current_timestamp(TimestampFormat.CUSTOM, custom_format=fmt)
    print(f"Custom '{fmt}': {timestamp}")
```

### Error Handling

```python
from timestamp_utils import get_current_timestamp, TimestampFormat, TimestampError

try:
    # This will raise a ValueError
    timestamp = get_current_timestamp(TimestampFormat.CUSTOM)
except ValueError as e:
    print(f"ValueError: {e}")

try:
    # This will raise a TimestampError for invalid format
    timestamp = get_current_timestamp(
        TimestampFormat.CUSTOM, 
        custom_format='%invalid_format%'
    )
except TimestampError as e:
    print(f"TimestampError: {e}")
```

### Logging

```python
import logging
from timestamp_utils import get_current_timestamp

# Configure logging to see debug messages
logging.basicConfig(level=logging.DEBUG)

# This will log debug information
timestamp = get_current_timestamp()
```

## Development

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=timestamp_utils --cov-report=html

# Run specific test file
python -m pytest tests/test_timestamp.py -v
```

### Code Quality

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint code
flake8 src/ tests/

# Type checking
mypy src/
```

### Test Coverage

The library maintains 100% test coverage with comprehensive tests for:

- All format types
- Error conditions
- Edge cases
- Convenience functions
- Logging functionality
- Type validation

## Requirements

- Python 3.8 or higher
- No external dependencies (uses only Python standard library)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## Changelog

### Version 1.0.0
- Initial release
- Support for multiple timestamp formats
- Comprehensive error handling
- Full test coverage
- Type hints and documentation

