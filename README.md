# Zymmr Client

[![PyPI version](https://badge.fury.io/py/zymmr-client.svg)](https://pypi.org/project/zymmr-client/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

A Python client library for interacting with the Zymmr Project Management API.

## ✨ Features

- 🚀 Simple and intuitive API interface
- 🔐 Authentication handling (API key support)
- 📝 Full CRUD operations for projects, tasks, and resources
- 🔄 Error handling and retry mechanisms
- 💡 Type hints for better development experience
- 🧪 Comprehensive test coverage

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

# Initialize the client
client = ZymmrClient(
    base_url="https://your-zymmr-instance.com",
    api_key="your-api-key"
)

# Get all projects
projects = client.projects.list()

# Create a new task
task = client.tasks.create({
    "title": "My Task",
    "project_id": "project-123",
    "status": "open"
})

# Update a task
updated_task = client.tasks.update("task-123", {
    "status": "completed"
})

# Delete a task
client.tasks.delete("task-123")
```

## 🔧 Configuration

### Environment Variables
```bash
export ZYMMR_API_KEY="your-api-key"
export ZYMMR_BASE_URL="https://your-zymmr-instance.com"
```

### Configuration File
Create a `.zymmr` config file in your project root:
```json
{
    "base_url": "https://your-zymmr-instance.com",
    "api_key": "your-api-key",
    "timeout": 30,
    "retry_count": 3
}
```

## 📖 API Reference

### Projects
```python
# List all projects
projects = client.projects.list()

# Get a specific project
project = client.projects.get("project-id")

# Create a new project
project = client.projects.create({
    "name": "My Project",
    "description": "Project description"
})

# Update a project
project = client.projects.update("project-id", {"name": "Updated Name"})

# Delete a project
client.projects.delete("project-id")
```

### Tasks
```python
# List tasks (with optional filtering)
tasks = client.tasks.list(project_id="project-123", status="open")

# Get a specific task
task = client.tasks.get("task-id")

# Create a new task
task = client.tasks.create({
    "title": "Task Title",
    "project_id": "project-123",
    "assignee": "user-123"
})

# Update a task
task = client.tasks.update("task-id", {"status": "in-progress"})

# Delete a task
client.tasks.delete("task-id")
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

- Thanks to the Zymmr team for the excellent API
- Inspired by [frappe-client](https://github.com/frappe/frappe-client) architecture
- Built with modern Python packaging tools ([uv](https://github.com/astral-sh/uv))

---

⭐ **If you find this package useful, please consider giving it a star on GitHub!**

**Package available on PyPI:** [https://pypi.org/project/zymmr-client/](https://pypi.org/project/zymmr-client/)
