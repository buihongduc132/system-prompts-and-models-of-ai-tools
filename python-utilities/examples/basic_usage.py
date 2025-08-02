#!/usr/bin/env python3
"""
Basic usage examples for timestamp utilities.

This script demonstrates how to use the timestamp utility functions
in various scenarios.
"""

import logging
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from timestamp_utils import get_current_timestamp, TimestampFormat
from timestamp_utils.timestamp import (
    get_unix_timestamp,
    get_iso_timestamp,
    get_human_readable_timestamp,
    TimestampError
)


def main():
    """Demonstrate basic usage of timestamp utilities."""
    
    # Configure logging to show debug information
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    print("🕒 Timestamp Utilities Demo")
    print("=" * 50)
    
    # 1. Basic UNIX timestamp
    print("\n1. UNIX Timestamp:")
    unix_time = get_current_timestamp()
    print(f"   Default (UNIX): {unix_time}")
    print(f"   Type: {type(unix_time)}")
    
    # 2. ISO8601 formats
    print("\n2. ISO8601 Formats:")
    iso_time = get_current_timestamp(TimestampFormat.ISO8601)
    iso_utc_time = get_current_timestamp(TimestampFormat.ISO8601_UTC)
    print(f"   ISO8601: {iso_time}")
    print(f"   ISO8601 UTC: {iso_utc_time}")
    
    # 3. Human-readable format
    print("\n3. Human-Readable Format:")
    human_time = get_current_timestamp(TimestampFormat.HUMAN_READABLE)
    print(f"   Human-readable: {human_time}")
    
    # 4. Custom formats
    print("\n4. Custom Formats:")
    custom_formats = [
        ('%Y-%m-%d', 'Date only'),
        ('%Y-%m-%d %H:%M:%S', 'Date and time'),
        ('%B %d, %Y', 'Month name format'),
        ('%A, %B %d, %Y at %I:%M %p', 'Full descriptive format')
    ]
    
    for fmt, description in custom_formats:
        try:
            custom_time = get_current_timestamp(TimestampFormat.CUSTOM, custom_format=fmt)
            print(f"   {description}: {custom_time}")
        except TimestampError as e:
            print(f"   Error with format '{fmt}': {e}")
    
    # 5. Convenience functions
    print("\n5. Convenience Functions:")
    print(f"   get_unix_timestamp(): {get_unix_timestamp()}")
    print(f"   get_iso_timestamp(): {get_iso_timestamp()}")
    print(f"   get_iso_timestamp(utc=False): {get_iso_timestamp(utc=False)}")
    print(f"   get_human_readable_timestamp(): {get_human_readable_timestamp()}")
    
    # 6. Error handling demonstration
    print("\n6. Error Handling:")
    
    # Missing custom format
    try:
        get_current_timestamp(TimestampFormat.CUSTOM)
    except ValueError as e:
        print(f"   ValueError (missing custom format): {e}")
    
    # Invalid format type
    try:
        get_current_timestamp("invalid_format")
    except TypeError as e:
        print(f"   TypeError (invalid format type): {e}")
    
    # Invalid custom format string
    try:
        get_current_timestamp(TimestampFormat.CUSTOM, custom_format='%invalid%')
    except TimestampError as e:
        print(f"   TimestampError (invalid custom format): {e}")
    
    # 7. Performance comparison
    print("\n7. Performance Comparison:")
    import time
    
    formats_to_test = [
        (TimestampFormat.UNIX, "UNIX"),
        (TimestampFormat.ISO8601, "ISO8601"),
        (TimestampFormat.HUMAN_READABLE, "Human-readable")
    ]
    
    iterations = 1000
    
    for fmt, name in formats_to_test:
        start_time = time.time()
        for _ in range(iterations):
            get_current_timestamp(fmt)
        end_time = time.time()
        
        avg_time = (end_time - start_time) / iterations * 1000  # Convert to milliseconds
        print(f"   {name}: {avg_time:.4f} ms per call (avg over {iterations} calls)")
    
    print("\n✅ Demo completed successfully!")


if __name__ == "__main__":
    main()

