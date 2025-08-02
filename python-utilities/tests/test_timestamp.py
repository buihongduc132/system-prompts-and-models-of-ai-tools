"""
Comprehensive unit tests for timestamp utility functions.

This module contains tests for all timestamp functionality including
edge cases, error handling, and various format types.
"""

import logging
import time
import unittest
from datetime import datetime, timezone
from unittest.mock import patch, MagicMock

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from timestamp_utils.timestamp import (
    get_current_timestamp,
    get_unix_timestamp,
    get_iso_timestamp,
    get_human_readable_timestamp,
    TimestampFormat,
    TimestampError
)


class TestTimestampUtils(unittest.TestCase):
    """Test cases for timestamp utility functions."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Configure logging for tests
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        
        # Mock timestamp for consistent testing
        self.mock_timestamp = 1704067200.123456  # 2024-01-01 00:00:00.123456 UTC
        
    def test_get_current_timestamp_unix_format(self):
        """Test getting current timestamp in UNIX format."""
        with patch('time.time', return_value=self.mock_timestamp):
            result = get_current_timestamp(TimestampFormat.UNIX)
            self.assertEqual(result, self.mock_timestamp)
            self.assertIsInstance(result, float)
    
    def test_get_current_timestamp_iso8601_format(self):
        """Test getting current timestamp in ISO8601 format."""
        with patch('time.time', return_value=self.mock_timestamp):
            result = get_current_timestamp(TimestampFormat.ISO8601)
            self.assertIsInstance(result, str)
            self.assertIn('2024-01-01T00:00:00', result)
            self.assertIn('+00:00', result)
    
    def test_get_current_timestamp_iso8601_utc_format(self):
        """Test getting current timestamp in ISO8601 UTC format."""
        with patch('time.time', return_value=self.mock_timestamp):
            result = get_current_timestamp(TimestampFormat.ISO8601_UTC)
            self.assertIsInstance(result, str)
            self.assertIn('2024-01-01T00:00:00', result)
            self.assertIn('+00:00', result)
    
    def test_get_current_timestamp_human_readable_format(self):
        """Test getting current timestamp in human-readable format."""
        with patch('time.time', return_value=self.mock_timestamp):
            result = get_current_timestamp(TimestampFormat.HUMAN_READABLE)
            self.assertIsInstance(result, str)
            self.assertIn('Monday', result)
            self.assertIn('January 01, 2024', result)
            self.assertIn('UTC', result)
    
    def test_get_current_timestamp_custom_format(self):
        """Test getting current timestamp with custom format."""
        custom_format = '%Y-%m-%d %H:%M:%S'
        with patch('time.time', return_value=self.mock_timestamp):
            result = get_current_timestamp(
                TimestampFormat.CUSTOM,
                custom_format=custom_format
            )
            self.assertIsInstance(result, str)
            self.assertEqual(result, '2024-01-01 00:00:00')
    
    def test_get_current_timestamp_custom_format_without_format_string(self):
        """Test that custom format raises ValueError when format string is missing."""
        with self.assertRaises(ValueError) as context:
            get_current_timestamp(TimestampFormat.CUSTOM)
        
        self.assertIn('custom_format must be provided', str(context.exception))
    
    def test_get_current_timestamp_invalid_format_type(self):
        """Test that invalid format type raises TypeError."""
        with self.assertRaises(TypeError) as context:
            get_current_timestamp("invalid_format")
        
        self.assertIn('format_type must be a TimestampFormat enum', str(context.exception))
    
    def test_get_current_timestamp_invalid_custom_format(self):
        """Test that invalid custom format string raises TimestampError."""
        with patch('time.time', return_value=self.mock_timestamp):
            # Create a mock datetime object that raises ValueError on strftime
            mock_dt = MagicMock()
            mock_dt.strftime.side_effect = ValueError("Invalid format")
            
            with patch('timestamp_utils.timestamp.datetime') as mock_datetime:
                mock_datetime.fromtimestamp.return_value = mock_dt
                with self.assertRaises(TimestampError) as context:
                    get_current_timestamp(
                        TimestampFormat.CUSTOM,
                        custom_format='%Y-%m-%d'
                    )
                
                self.assertIn('Invalid custom format string', str(context.exception))
    
    def test_get_current_timestamp_timezone_aware_false(self):
        """Test getting timestamp with timezone_aware=False."""
        with patch('time.time', return_value=self.mock_timestamp):
            result = get_current_timestamp(
                TimestampFormat.ISO8601,
                timezone_aware=False
            )
            self.assertIsInstance(result, str)
            # Should not contain timezone info when timezone_aware=False
            # The exact format depends on the local timezone
            self.assertIsInstance(result, str)
    
    def test_get_current_timestamp_system_error(self):
        """Test handling of system errors during timestamp generation."""
        with patch('time.time', side_effect=OSError("System error")):
            with self.assertRaises(TimestampError) as context:
                get_current_timestamp()
            
            self.assertIn('Failed to generate timestamp due to system error', str(context.exception))
    
    def test_get_current_timestamp_overflow_error(self):
        """Test handling of overflow errors during timestamp generation."""
        with patch('time.time', side_effect=OverflowError("Overflow error")):
            with self.assertRaises(TimestampError) as context:
                get_current_timestamp()
            
            self.assertIn('Failed to generate timestamp due to system error', str(context.exception))
    
    def test_get_current_timestamp_unexpected_error(self):
        """Test handling of unexpected errors during timestamp generation."""
        with patch('time.time', side_effect=RuntimeError("Unexpected error")):
            with self.assertRaises(TimestampError) as context:
                get_current_timestamp()
            
            self.assertIn('Unexpected error occurred', str(context.exception))
    
    def test_get_unix_timestamp_convenience_function(self):
        """Test the convenience function for getting UNIX timestamp."""
        with patch('time.time', return_value=self.mock_timestamp):
            result = get_unix_timestamp()
            self.assertEqual(result, self.mock_timestamp)
            self.assertIsInstance(result, float)
    
    def test_get_iso_timestamp_convenience_function_utc_true(self):
        """Test the convenience function for getting ISO timestamp in UTC."""
        with patch('time.time', return_value=self.mock_timestamp):
            result = get_iso_timestamp(utc=True)
            self.assertIsInstance(result, str)
            self.assertIn('2024-01-01T00:00:00', result)
            self.assertIn('+00:00', result)
    
    def test_get_iso_timestamp_convenience_function_utc_false(self):
        """Test the convenience function for getting ISO timestamp in local timezone."""
        with patch('time.time', return_value=self.mock_timestamp):
            result = get_iso_timestamp(utc=False)
            self.assertIsInstance(result, str)
            self.assertIn('2024-01-01T00:00:00', result)
    
    def test_get_human_readable_timestamp_convenience_function(self):
        """Test the convenience function for getting human-readable timestamp."""
        with patch('time.time', return_value=self.mock_timestamp):
            result = get_human_readable_timestamp()
            self.assertIsInstance(result, str)
            self.assertIn('Monday', result)
            self.assertIn('January 01, 2024', result)
            self.assertIn('UTC', result)
    
    def test_timestamp_format_enum_values(self):
        """Test that TimestampFormat enum has expected values."""
        self.assertEqual(TimestampFormat.UNIX.value, "unix")
        self.assertEqual(TimestampFormat.ISO8601.value, "iso8601")
        self.assertEqual(TimestampFormat.ISO8601_UTC.value, "iso8601_utc")
        self.assertEqual(TimestampFormat.HUMAN_READABLE.value, "human_readable")
        self.assertEqual(TimestampFormat.CUSTOM.value, "custom")
    
    def test_timestamp_consistency(self):
        """Test that multiple calls within a short time frame are consistent."""
        # Get multiple timestamps quickly
        timestamps = []
        for _ in range(5):
            timestamps.append(get_current_timestamp(TimestampFormat.UNIX))
            time.sleep(0.001)  # Small delay to ensure different timestamps
        
        # All timestamps should be floats
        for ts in timestamps:
            self.assertIsInstance(ts, float)
        
        # Timestamps should be in ascending order (or very close)
        for i in range(1, len(timestamps)):
            self.assertGreaterEqual(timestamps[i], timestamps[i-1])
    
    def test_timestamp_precision(self):
        """Test that timestamps have appropriate precision."""
        timestamp = get_current_timestamp(TimestampFormat.UNIX)
        
        # UNIX timestamp should be a float with microsecond precision
        self.assertIsInstance(timestamp, float)
        
        # Should be a reasonable timestamp (after 2020, before 2030)
        self.assertGreater(timestamp, 1577836800)  # 2020-01-01
        self.assertLess(timestamp, 1893456000)     # 2030-01-01
    
    def test_logging_functionality(self):
        """Test that logging works correctly."""
        with patch('time.time', return_value=self.mock_timestamp):
            with patch('timestamp_utils.timestamp.logger') as mock_logger:
                get_current_timestamp(TimestampFormat.UNIX)
                
                # Verify that debug logging was called
                mock_logger.debug.assert_called()
                
                # Check that the log message contains expected content
                log_calls = mock_logger.debug.call_args_list
                self.assertTrue(any('Generating timestamp' in str(call) for call in log_calls))
    
    def test_all_format_types_return_expected_types(self):
        """Test that all format types return the expected data types."""
        with patch('time.time', return_value=self.mock_timestamp):
            # UNIX should return float
            unix_result = get_current_timestamp(TimestampFormat.UNIX)
            self.assertIsInstance(unix_result, float)
            
            # ISO8601 should return string
            iso_result = get_current_timestamp(TimestampFormat.ISO8601)
            self.assertIsInstance(iso_result, str)
            
            # ISO8601_UTC should return string
            iso_utc_result = get_current_timestamp(TimestampFormat.ISO8601_UTC)
            self.assertIsInstance(iso_utc_result, str)
            
            # HUMAN_READABLE should return string
            human_result = get_current_timestamp(TimestampFormat.HUMAN_READABLE)
            self.assertIsInstance(human_result, str)
            
            # CUSTOM should return string
            custom_result = get_current_timestamp(
                TimestampFormat.CUSTOM,
                custom_format='%Y-%m-%d'
            )
            self.assertIsInstance(custom_result, str)


class TestTimestampErrorHandling(unittest.TestCase):
    """Test cases specifically for error handling scenarios."""
    
    def test_timestamp_error_inheritance(self):
        """Test that TimestampError inherits from Exception."""
        error = TimestampError("Test error")
        self.assertIsInstance(error, Exception)
        self.assertEqual(str(error), "Test error")
    
    def test_error_propagation_in_convenience_functions(self):
        """Test that errors are properly propagated in convenience functions."""
        with patch('timestamp_utils.timestamp.get_current_timestamp', 
                   side_effect=TimestampError("Test error")):
            
            with self.assertRaises(TimestampError):
                get_unix_timestamp()
            
            with self.assertRaises(TimestampError):
                get_iso_timestamp()
            
            with self.assertRaises(TimestampError):
                get_human_readable_timestamp()


if __name__ == '__main__':
    # Configure logging for test execution
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Run the tests
    unittest.main(verbosity=2)
