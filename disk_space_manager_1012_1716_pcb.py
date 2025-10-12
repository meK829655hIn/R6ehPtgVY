# 代码生成时间: 2025-10-12 17:16:42
import os
import shutil
import gr
from gr import Blocks
from gr.Blocks import Markdown

"""
Disk Space Management Tool

This tool provides functionality to manage disk space by displaying
available and total disk space. It also allows users to clear
cache, temporary files, and recycle bin to free up space.
"""

def get_disk_usage(path="."):
    """
    Calculate the total and available disk space.
    
    Args:
        path (str): The path to calculate disk usage (default is current directory).
    
    Returns:
        tuple: A tuple containing total and available disk space in GB.
    """
    total, used, free = shutil.disk_usage(path)
    return (total // (2**30), free // (2**30))

def clear_cache():
    """
    Clear cache files.
    
    Raises:
        FileNotFoundError: If the cache directory does not exist.
    """
    cache_dir = os.path.join(os.path.expanduser("~"), ".cache")
    if os.path.exists(cache_dir):
        shutil.rmtree(cache_dir)
    else:
        raise FileNotFoundError("Cache directory not found.")

def clear_temp():
    """
    Clear temporary files.
    
    Raises:
        FileNotFoundError: If the temp directory does not exist.
    "