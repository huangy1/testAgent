# tools.py
from typing import List
from langchain_core.tools import tool
import os

@tool
def read_file(filename: str) -> str:
    """Read content from a file."""
    try:
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

@tool
def list_files(path: str = ".") -> List[str]:
    """List files in a directory."""
    try:
        return os.listdir(path)
    except Exception as e:
        return [f"Error listing files: {e}"]

@tool
def rename_file(old_name: str, new_name: str) -> str:
    """Rename a file."""
    try:
        os.rename(old_name, new_name)
        return f"File renamed from {old_name} to {new_name}"
    except Exception as e:
        return f"Error renaming file: {e}"