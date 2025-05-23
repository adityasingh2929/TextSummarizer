import os
from pathlib import Path  
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "TextSummarization"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Use pathlib for better path handling
    filedir = filepath.parent  # Get parent directory
    filename = filepath.name  # Get filename

    if filedir != Path():  # Create directory if not in root
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Ensure all files get created
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating an empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
