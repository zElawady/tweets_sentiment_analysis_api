import os
from pathlib import Path



list_of_files = [
     "Artifacts",
     "DataSets",
     "NoteBooks",
     "src/__init__.py",
     "src/controllers/__init__.py",
     "src/controllers/app_router.py",
     "src/controllers/base_router.py",
     "src/core/__init__.py",
     "src/core/backend.py",
     "src/models/__init__.py",
     "src/models/input_output_schema.py",
     "src/utils/__init__.py",
     "src/utils/config.py",
     "src/utils/inference.py",
     "src/utils/text_processor.py",
     "src/view/__init__.py",
     "src/view/frontend.py",
     "src/requirements.txt",
     
     "README.md",
     "License.txt"
     
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(name=filedir, exist_ok=True)
        
    if (not os.path.exists(filepath)):
        if filename in ["Artifacts", "DataSets", "NoteBooks"]:
            os.makedirs(name=filepath, exist_ok=True)
        else:
            with open(file=filepath, mode="w") as f:
                pass
    else:
        print(f"{filepath} is already exists")