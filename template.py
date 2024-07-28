import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "DSproject"

list_of_files = [
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/components/data_ingestion.py',
    f'src/{project_name}/components/data_tranformation.py',
    f'src/{project_name}/components/data_trainer.py',
    f'src/{project_name}/components/data_monitering.py',
    f'src/{project_name}/pipelines/tarining_pipeline.py',
    f'src/{project_name}/pipelines/prediction_pipeline.py',
    f'src/{project_name}/exception.py',
    f'src/{project_name}/logger.py',
    f'src/{project_name}/utilis.py',
    'app.py',
    'Dockerfile'
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)
    
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory:{filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'Creating empty file: {filepath}')
    
    else:
        logging.info(f'{filepath} is already exists')
        
        