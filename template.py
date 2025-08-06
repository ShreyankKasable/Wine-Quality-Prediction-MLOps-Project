import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "WineQuality"

list_of_files=[
".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
    "app.py"
]

for filePath in list_of_files:
    filePath = Path(filePath) # This is used to convert filepath string into proper path
    fileDir, fileName = os.path.split(filePath)

    if fileDir != "":
        os.makedirs(fileDir, exist_ok=True)
        logging.info(f"Creating directory {fileDir} for the file : {fileName}")

    if (not os.path.exists(filePath)) or (os.path.getsize(filePath) == 0):
        with open(filePath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filePath}")
    else:
        logging.info(f"{fileName} is already exists")
