#!/usr/bin/env python3
"""
Dependency installer for bl_earth Blender extension
"""

import subprocess
import sys
from pathlib import Path

def install_dependencies():
    """Install required Python packages for the bl_earth extension."""
    
    requirements = [
        "ecmwf-opendata",
        "cfgrib", 
        "eccodes",
        "findlibs",
        "numpy",
        "pandas", 
        "pycodestyle",
        "python-dateutil",
        "matplotlib",
        "requests",
        "xarray",
    ]
    
    print("Installing dependencies for bl_earth extension...")
    
    for package in requirements:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"✓ Successfully installed {package}")
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to install {package}: {e}")
            continue
    
    print("\nDependency installation complete!")
    print("You can now enable the bl_earth extension in Blender.")

if __name__ == "__main__":
    install_dependencies()