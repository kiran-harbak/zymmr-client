# Zymmr Client

[![PyPI version](https://badge.fury.io/py/zymmr-client.svg)](https://pypi.org/project/zymmr-client/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

A robust Python client library for interacting with Zymmr Project Management API, built on **Frappe Framework v14**.

## ✨ Features

- 🚀 **Simple and Intuitive**: Clean API interface inspired by frappe-client but more robust
- 🔐 **Frappe Authentication**: Session-based authentication with username/password
- 📋 **Complete DocType Access**: Get any DocType from your Zymmr instance
- 🔄 **Robust Error Handling**: Custom exceptions for all Frappe API scenarios
- ⚡ **Retry Logic**: Exponential backoff for network failures
- 💡 **Type Safety**: Full type hints for excellent developer experience
- 🎯 **Production Ready**: Built for real-world Frappe applications

## 📦 Installation

### Using uv (Recommended)
```bash
uv add zymmr-client
```

### Using pip
```bash
pip install zymmr-client
```

### Using poetry
```bash
poetry add zymmr-client
```

## 🚀 Quick Start

```python
from zymmr_client import ZymmrClient

# Initialize the client with your Zymmr instance
client = ZymmrClient(
    base_url="https://zymmr.yourdomain.com",
    username="your-username",
    password="your-password"
)

# Get list of projects
projects = client.get_list("Project", 
                          fields=["name", "project_name", "status"],
                          limit_page_length=10)

# Get list of tasks with filters
tasks = client.get_list("Task",
                       fields=["name", "subject", "status", "priority"],
                       filters={"status": ["in", ["Open", "Working"]]},
                       order_by="priority desc")

# Get a specific document
project = client.get_doc("Project", "PROJ-001")

# Test connection
if client.ping():
    print("✅ Connected to Zymmr!")

# Get current user info
user_info = client.get_user_info()
print(f"Logged in as: {user_info['username']}")
```

## 🔧 Configuration

### Basic Configuration
```python
from zymmr_client import ZymmrClient

# Basic initialization
client = ZymmrClient(
    base_url="https://zymmr.yourdomain.com",
    username="your-username",
    password="your-password"
)

# With custom timeout and retry settings
client = ZymmrClient(
    base_url="https://zymmr.yourdomain.com", 
    username="your-username",
    password="your-password",
    timeout=60,          # Request timeout in seconds
    max_retries=5,       # Max retry attempts
    debug=True           # Enable debug logging
)
```

### Context Manager (Recommended)
```python
# Automatic session cleanup
with ZymmrClient(base_url, username, password) as client:
    projects = client.get_list("Project")
    # Session automatically closed when done
```

## 📖 API Reference

### Core Methods

#### `get_list(doctype, **kwargs)`
Get a list of documents from any Frappe DocType:

```python
# Basic usage
projects = client.get_list("Project")

# With specific fields
projects = client.get_list("Project", 
                          fields=["name", "project_name", "status"])

# With filters
open_tasks = client.get_list("Task", 
                            fields=["name", "subject", "priority"],
                            filters={"status": "Open"},
                            order_by="priority desc",
                            limit_page_length=50)

# Complex filters
recent_projects = client.get_list("Project",
                                 filters={
                                     "status": ["in", ["Active", "On Hold"]],
                                     "creation": [">", "2024-01-01"]
                                 })
```

#### `get_doc(doctype, name, fields=None)`
Get a specific document:

```python
# Get full document
project = client.get_doc("Project", "PROJ-001")

# Get specific fields only
task = client.get_doc("Task", "TASK-001", 
                     fields=["name", "subject", "status"])
```

#### Utility Methods

```python
# Test connection
is_connected = client.ping()

# Get current user information
user_info = client.get_user_info()

# Check authentication status
if client.is_authenticated:
    print("Client is authenticated")

# Clean session cleanup
client.close()
```

### Available DocTypes
Access any DocType from your Zymmr/Frappe instance:

```python
# Standard Frappe DocTypes
users = client.get_list("User")
doctypes = client.get_list("DocType")

# Zymmr-specific DocTypes (depends on your setup)
projects = client.get_list("Project")
tasks = client.get_list("Task")
issues = client.get_list("Issue")

# Custom DocTypes
custom_docs = client.get_list("Your Custom DocType")
```

## 🛠️ Development

This project uses `uv` for dependency management and packaging:

```bash
# Clone the repository
git clone https://github.com/kiran-harbak/zymmr-client.git
cd zymmr-client

# Install dependencies
uv sync

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=zymmr_client

# Lint code
uv run ruff check .

# Format code
uv run ruff format .

# Type check
uv run mypy src/

# Build package
uv build
```

### 🧪 Running Tests
```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=zymmr_client --cov-report=html

# Run specific test file
uv run pytest tests/test_client.py

# Run with verbose output
uv run pytest -v
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.

## 🐛 Issues

If you encounter any issues or have feature requests, please [create an issue](https://github.com/kiran-harbak/zymmr-client/issues) on GitHub.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Kiran Harbak**
- Email: kiran.harbak@amruts.com
- GitHub: [@kiran-harbak](https://github.com/kiran-harbak)

## 🙏 Acknowledgments

- Thanks to the Zymmr team for building on Frappe Framework
- Inspired by [frappe-client](https://github.com/frappe/frappe-client) but rebuilt for modern Python
- Built specifically for Frappe Framework v14 REST API
- Powered by [uv](https://github.com/astral-sh/uv) for fast dependency management

---

⭐ **If you find this package useful, please consider giving it a star on GitHub!**

**Package available on PyPI:** [https://pypi.org/project/zymmr-client/](https://pypi.org/project/zymmr-client/)
