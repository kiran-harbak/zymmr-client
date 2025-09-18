"""Zymmr Client - Python library for Zymmr Project Management API.

A modern, robust Python client for interacting with Zymmr's REST API,
built on top of Frappe Framework v14.

Example usage:
    ```python
    from zymmr_client import ZymmrClient
    
    # Initialize client
    client = ZymmrClient(
        base_url="https://zymmr.yourdomain.com",
        username="your-username", 
        password="your-password"
    )
    
    # Get list of projects
    projects = client.get_list("Project", fields=["name", "status"])
    
    # Get specific document
    project = client.get_doc("Project", "PROJ-001")
    ```
"""

__version__ = "0.1.1"
__author__ = "Kiran Harbak"
__email__ = "kiran.harbak@amruts.com"

# Main exports
from .client import ZymmrClient
from .exceptions import (
    ZymmrAPIError,
    ZymmrAuthenticationError, 
    ZymmrPermissionError,
    ZymmrNotFoundError,
    ZymmrValidationError,
    ZymmrServerError,
    ZymmrConnectionError,
    ZymmrTimeoutError
)

__all__ = [
    "ZymmrClient",
    "ZymmrAPIError",
    "ZymmrAuthenticationError",
    "ZymmrPermissionError", 
    "ZymmrNotFoundError",
    "ZymmrValidationError",
    "ZymmrServerError",
    "ZymmrConnectionError",
    "ZymmrTimeoutError",
]


def main() -> None:
    """CLI entry point."""
    print(f"Zymmr Client v{__version__}")
    print("Python client library for Zymmr Project Management API")
    print("\nFor usage examples, visit: https://github.com/kiran-harbak/zymmr-client")
