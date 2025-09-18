# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2024-09-18

### Added
- **Complete Frappe Framework v14 integration** - Built specifically for Frappe-based applications
- **Robust authentication system** - Session-based authentication with username/password
- **`get_list()` method** - Full implementation of Frappe's REST API endpoint with:
  - Field selection with JSON array support
  - Complex filtering with JSON object support
  - Ordering and pagination
  - Group by functionality
- **`get_doc()` method** - Fetch individual documents by name
- **Utility methods**: `ping()`, `get_user_info()`, connection testing
- **Context manager support** - Automatic session cleanup
- **Comprehensive error handling** - Custom exceptions for all Frappe API scenarios:
  - `ZymmrAuthenticationError` for auth failures
  - `ZymmrPermissionError` for access denied
  - `ZymmrNotFoundError` for missing resources
  - `ZymmrValidationError` for Frappe validation failures
  - `ZymmrServerError` for server-side issues
- **Retry logic** - Exponential backoff for network failures
- **Debug logging** - Detailed request/response logging when enabled
- **Type safety** - Full type hints throughout the codebase

### Changed  
- **BREAKING**: Complete API rewrite - moved from resource-based API to Frappe-style DocType access
- **BREAKING**: Authentication changed from API keys to username/password (Frappe standard)
- **README.md** - Updated with actual implementation examples and usage patterns
- **Package description** - Now reflects Frappe Framework v14 integration

### Fixed
- Authentication verification issues with Frappe's user ID system
- Session management and cookie handling
- Error handling and response parsing
- Import statements and package structure

### Technical Details
- Built on `requests` library with session management
- Follows Frappe REST API patterns: `GET /api/resource/{doctype}`
- Session-based auth via `POST /api/method/login`
- Production-ready with proper error handling and retries

## [0.1.1] - 2024-09-17

### Added
- Initial package structure with uv
- Basic project metadata and configuration
- MIT License and GitHub repository setup

## [0.1.0] - 2024-09-17

### Added
- Initial project setup
- Basic package scaffolding
- Project metadata configuration
