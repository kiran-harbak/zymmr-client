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
                          fields=["name", "title", "status"],
                          limit_page_length=10)

# Get list of work items with filters
work_items = client.get_list("Work Item",
                           fields=["key", "title", "status", "priority"],
                           filters={"status": ["in", ["Open", "In Progress"]]},
                           order_by="priority desc")

# Get a specific document
project = client.get_doc("Project", "PROJ-001")

# Create a new work item
new_work_item = client.insert("Work Item", {
    "title": "Fix authentication bug",
    "project": "PROJ-001",
    "type": "Bug",
    "priority": "High"
})

# Update work item status
client.update("Work Item", new_work_item["name"], {
    "status": "In Progress",
    "assignee": "developer@company.com"
})

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
                          fields=["name", "title", "status"])

# With filters
open_work_items = client.get_list("Work Item", 
                                 fields=["key", "title", "priority"],
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
work_item = client.get_doc("Work Item", "WI-123", 
                          fields=["key", "title", "status"])
```

#### `insert(doctype, data)`
Create a new document:

```python
# Create a new work item
work_item = client.insert("Work Item", {
    "title": "Implement user dashboard",
    "project": "PROJ-001",
    "type": "Story",
    "priority": "Medium",
    "description": "Create a user dashboard with key metrics"
})

# Create a new project
project = client.insert("Project", {
    "title": "Mobile App Development",
    "key": "MAD",
    "description": "iOS and Android mobile application",
    "lead": "pm@company.com"
})

# Create a time log
time_log = client.insert("Time Log", {
    "work_item": "WI-123",
    "time": "2h 30m",
    "description": "Implemented authentication logic",
    "is_billable": True
})
```

#### `update(doctype, name, data)`
Update an existing document:

```python
# Update work item status and assignee
client.update("Work Item", "WI-123", {
    "status": "In Progress",
    "assignee": "developer@company.com",
    "start_date": "2024-01-15"
})

# Update project end date
client.update("Project", "PROJ-001", {
    "end_date": "2024-12-31",
    "status": "Active"
})

# Update time log
client.update("Time Log", "TL-456", {
    "time": "3h",
    "description": "Updated: Fixed authentication and added tests"
})
```

#### `delete(doctype, name)`
Delete a document:

```python
# Delete a work item
success = client.delete("Work Item", "WI-123")
if success:
    print("Work item deleted successfully")

# Delete a time log
client.delete("Time Log", "TL-456")

# Delete a project (be careful!)
client.delete("Project", "OLD-PROJ")
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

# Zymmr-specific DocTypes
projects = client.get_list("Project")
work_items = client.get_list("Work Item")  # Main work tracking entity
time_logs = client.get_list("Time Log")
sprints = client.get_list("Sprint")

# Custom DocTypes (based on your Zymmr setup)
custom_docs = client.get_list("Your Custom DocType")
```

## 🎯 **Common Workflows**

### **Complete Work Item Lifecycle**
```python
# 1. Create a new work item
work_item = client.insert("Work Item", {
    "title": "Add user notifications",
    "project": "PROJ-001",
    "type": "Feature",
    "priority": "Medium",
    "description": "Implement email and in-app notifications"
})

print(f"Created work item: {work_item['key']}")

# 2. Start working on it
client.update("Work Item", work_item["name"], {
    "status": "In Progress",
    "assignee": "developer@company.com",
    "actual_start_date": "2024-01-15"
})

# 3. Log time while working
client.insert("Time Log", {
    "work_item": work_item["key"],
    "time": "2h",
    "description": "Implemented notification service",
    "is_billable": True
})

# 4. Complete the work item
client.update("Work Item", work_item["name"], {
    "status": "Done",
    "completion_date": "2024-01-16T14:30:00"
})
```

### **Project Management Operations**
```python
# Create a new project
project = client.insert("Project", {
    "title": "Customer Portal",
    "key": "CP",
    "description": "Self-service customer portal",
    "lead": "pm@company.com",
    "start_date": "2024-01-01",
    "end_date": "2024-06-30"
})

# Add work items to the project
work_items = [
    {"title": "User authentication", "type": "Story", "priority": "High"},
    {"title": "Dashboard design", "type": "Story", "priority": "Medium"},
    {"title": "Payment integration", "type": "Feature", "priority": "High"}
]

for item_data in work_items:
    item_data["project"] = project["key"]
    client.insert("Work Item", item_data)

# Get project progress
project_work_items = client.get_list("Work Item", 
                                   filters={"project": project["key"]},
                                   fields=["key", "title", "status"])

print(f"Project {project['key']} has {len(project_work_items)} work items")
```

### **Time Tracking & Reporting**
```python
from datetime import datetime, timedelta

# Get time logs for the last week
last_week = datetime.now() - timedelta(days=7)
recent_logs = client.get_list("Time Log",
                             filters={"date": [">", last_week.isoformat()]},
                             fields=["work_item", "time", "author", "is_billable"])

# Calculate total billable hours
total_billable = sum(
    float(log["time"].replace("h", "").replace("m", "")) 
    for log in recent_logs 
    if log["is_billable"]
)

print(f"Total billable hours this week: {total_billable}")
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

- Inspired by [frappe-client](https://github.com/frappe/frappe-client) but rebuilt for modern Python
- Powered by [uv](https://github.com/astral-sh/uv) for fast dependency management

---

⭐ **If you find this package useful, please consider giving it a star on GitHub!**

**Package available on PyPI:** [https://pypi.org/project/zymmr-client/](https://pypi.org/project/zymmr-client/)
