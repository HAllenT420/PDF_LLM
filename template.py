import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "PDF_LLM"  # Replace this with your actual project name

list_of_files = [
    f"src/{project_name}/data_ingestion/extract_text.py",
    f"src/{project_name}/data_transformation/preprocess.py",
    f"src/{project_name}/data_transformation/embeddings.py",
    f"src/{project_name}/model/setup_llm.py",
    f"src/{project_name}/chat_pipeline/chat_pipeline.py",
    f"src/{project_name}/utils/config.py",
    f"src/{project_name}/app.py",
    f"tests/test_ingestion.py",
    f"tests/test_transformation.py",
    f"tests/test_pipeline.py",
    "data/pdfs/.gitkeep",
    "data/embeddings/.gitkeep",
    "requirements.txt",
    "Dockerfile",
    "app.py",  # Entry point for the project
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

