#!/usr/bin/env python3
"""
Build script for bl_earth Blender extension
Creates a ZIP package suitable for installation in Blender
"""

import zipfile
import os
from pathlib import Path
import shutil

def create_extension_package():
    """Create a ZIP package for the Blender extension."""
    
    # Define the extension files to include
    extension_files = [
        "__init__.py",
        "blender_manifest.toml",
        "data.py",
        "earth.py", 
        "operators.py",
        "panels.py",
        "render.py",
        "textures/",
    ]
    
    # Create output directory
    output_dir = Path("dist")
    output_dir.mkdir(exist_ok=True)
    
    # Create the ZIP file
    zip_path = output_dir / "bl_earth-extension.zip"
    
    print(f"Creating extension package: {zip_path}")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_pattern in extension_files:
            path = Path(file_pattern)
            
            if path.is_file():
                # Add individual file
                zipf.write(path, path.name)
                print(f"Added: {path.name}")
            elif path.is_dir():
                # Add directory recursively
                for root, dirs, files in os.walk(path):
                    # Skip __pycache__ directories
                    dirs[:] = [d for d in dirs if d != "__pycache__"]
                    
                    for file in files:
                        if not file.endswith('.pyc'):
                            file_path = Path(root) / file
                            arcname = file_path.relative_to(Path("."))
                            zipf.write(file_path, arcname)
                            print(f"Added: {arcname}")
    
    print(f"\n✓ Extension package created: {zip_path}")
    print(f"  Install in Blender via Edit > Preferences > Extensions > Install from Disk")
    
    return zip_path

if __name__ == "__main__":
    create_extension_package()