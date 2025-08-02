"""
Timestamp utility module for generating current timestamps.

This module provides functions to get the current timestamp in various formats
with comprehensive error handling and logging capabilities.
"""

import logging
import time
from datetime import datetime, timezone
from enum import Enum
from typing import Optional, Union

# Configure logging
logger = logging.getLogger(__name__)


class TimestampFormat(Enum):
    """Enumeration of supported timestamp formats."""
    
    UNIX = "unix"
    ISO8601 = "iso8601"
    ISO8601_UTC = "iso8601_utc"
    HUMAN_READABLE = "human_readable"
    CUSTOM = "custom"


class TimestampError(Exception):
    """Custom exception for timestamp-related errors."""
    pass


def get_current_timestamp(
    format_type: TimestampFormat = TimestampFormat.UNIX,
    custom_format: Optional[str] = None,
    timezone_aware: bool = True
) -> Union[int, float, str]:
    """
    Get the current timestamp in the specified format.
    
    Args:
        format_type (TimestampFormat): The format to return the timestamp in.
            Defaults to TimestampFormat.UNIX.
        custom_format (Optional[str]): Custom format string for datetime formatting.
            Only used when format_type is TimestampFormat.CUSTOM.
        timezone_aware (bool): Whether to include timezone information.
            Defaults to True.
    
    Returns:
        Union[int, float, str]: The current timestamp in the requested format.
            - UNIX: Returns float (seconds since epoch)
            - ISO8601: Returns str (ISO 8601 formatted string)
            - ISO8601_UTC: Returns str (ISO 8601 formatted string in UTC)
            - HUMAN_READABLE: Returns str (human-readable format)
            - CUSTOM: Returns str (custom formatted string)
    
    Raises:
        TimestampError: If there's an error generating the timestamp.
        ValueError: If custom_format is required but not provided.
        TypeError: If invalid format_type is provided.
    
    Examples:
        >>> get_current_timestamp()
        1704067200.123456
        
        >>> get_current_timestamp(TimestampFormat.ISO8601)
        '2024-01-01T00:00:00.123456+00:00'
        
        >>> get_current_timestamp(TimestampFormat.HUMAN_READABLE)
        'Monday, January 01, 2024 at 12:00:00 AM UTC'
        
        >>> get_current_timestamp(TimestampFormat.CUSTOM, custom_format='%Y-%m-%d %H:%M:%S')
        '2024-01-01 00:00:00'
    """
    try:
        logger.debug(f"Generating timestamp with format: {format_type}")
        
        # Validate input parameters
        if not isinstance(format_type, TimestampFormat):
            raise TypeError(f"format_type must be a TimestampFormat enum, got {type(format_type)}")
        
        if format_type == TimestampFormat.CUSTOM and custom_format is None:
            raise ValueError("custom_format must be provided when using TimestampFormat.CUSTOM")
        
        # Get current time
        current_time = time.time()
        
        if format_type == TimestampFormat.UNIX:
            logger.debug(f"Returning UNIX timestamp: {current_time}")
            return current_time
        
        # Convert to datetime object
        if timezone_aware:
            dt = datetime.fromtimestamp(current_time, tz=timezone.utc)
        else:
            dt = datetime.fromtimestamp(current_time)
        
        if format_type == TimestampFormat.ISO8601:
            result = dt.isoformat()
            logger.debug(f"Returning ISO8601 timestamp: {result}")
            return result
        
        elif format_type == TimestampFormat.ISO8601_UTC:
            dt_utc = dt.astimezone(timezone.utc)
            result = dt_utc.isoformat()
            logger.debug(f"Returning ISO8601 UTC timestamp: {result}")
            return result
        
        elif format_type == TimestampFormat.HUMAN_READABLE:
            result = dt.strftime("%A, %B %d, %Y at %I:%M:%S %p %Z")
            logger.debug(f"Returning human-readable timestamp: {result}")
            return result
        
        elif format_type == TimestampFormat.CUSTOM:
            try:
                result = dt.strftime(custom_format)
                logger.debug(f"Returning custom formatted timestamp: {result}")
                return result
            except ValueError as e:
                raise TimestampError(f"Invalid custom format string '{custom_format}': {e}")
        
        else:
            raise TimestampError(f"Unsupported format type: {format_type}")
    
    except (OSError, OverflowError) as e:
        logger.error(f"System error while generating timestamp: {e}")
        raise TimestampError(f"Failed to generate timestamp due to system error: {e}")
    
    except (ValueError, TypeError) as e:
        # Re-raise ValueError and TypeError as-is for proper error handling
        raise
    
    except Exception as e:
        logger.error(f"Unexpected error while generating timestamp: {e}")
        raise TimestampError(f"Unexpected error occurred: {e}")


def get_unix_timestamp() -> float:
    """
    Get the current UNIX timestamp (seconds since epoch).
    
    This is a convenience function that calls get_current_timestamp()
    with TimestampFormat.UNIX.
    
    Returns:
        float: The current UNIX timestamp.
    
    Raises:
        TimestampError: If there's an error generating the timestamp.
    
    Examples:
        >>> get_unix_timestamp()
        1704067200.123456
    """
    return get_current_timestamp(TimestampFormat.UNIX)


def get_iso_timestamp(utc: bool = True) -> str:
    """
    Get the current timestamp in ISO 8601 format.
    
    This is a convenience function that calls get_current_timestamp()
    with ISO8601 or ISO8601_UTC format.
    
    Args:
        utc (bool): Whether to return the timestamp in UTC. Defaults to True.
    
    Returns:
        str: The current timestamp in ISO 8601 format.
    
    Raises:
        TimestampError: If there's an error generating the timestamp.
    
    Examples:
        >>> get_iso_timestamp()
        '2024-01-01T00:00:00.123456+00:00'
        
        >>> get_iso_timestamp(utc=False)
        '2024-01-01T00:00:00.123456-05:00'
    """
    format_type = TimestampFormat.ISO8601_UTC if utc else TimestampFormat.ISO8601
    return get_current_timestamp(format_type)


def get_human_readable_timestamp() -> str:
    """
    Get the current timestamp in human-readable format.
    
    This is a convenience function that calls get_current_timestamp()
    with TimestampFormat.HUMAN_READABLE.
    
    Returns:
        str: The current timestamp in human-readable format.
    
    Raises:
        TimestampError: If there's an error generating the timestamp.
    
    Examples:
        >>> get_human_readable_timestamp()
        'Monday, January 01, 2024 at 12:00:00 AM UTC'
    """
    return get_current_timestamp(TimestampFormat.HUMAN_READABLE)
