# Changelog

All notable changes to the timestamp utilities project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-08-02

### Added
- Initial release of timestamp utilities package
- Support for multiple timestamp formats:
  - UNIX timestamp (seconds since epoch)
  - ISO8601 format with timezone support
  - ISO8601 UTC format
  - Human-readable format
  - Custom format with strftime patterns
- Comprehensive error handling with custom `TimestampError` exception
- Extensive logging support for debugging and monitoring
- Type hints for all functions and parameters
- Convenience functions for common use cases:
  - `get_unix_timestamp()`
  - `get_iso_timestamp()`
  - `get_human_readable_timestamp()`
- Full test coverage with 23 comprehensive unit tests
- Example scripts demonstrating usage
- Development tools configuration (black, isort, mypy, flake8)
- Makefile for common development tasks
- Complete documentation with API reference and examples

### Features
- Zero external dependencies (uses only Python standard library)
- Python 3.8+ compatibility
- Timezone-aware timestamp generation
- Robust error handling for system errors and invalid inputs
- Performance optimized for high-frequency usage
- Comprehensive logging with configurable levels

### Documentation
- Complete README with installation and usage instructions
- API reference with detailed parameter descriptions
- Code examples for all supported formats
- Error handling examples
- Development setup instructions
- Contributing guidelines

