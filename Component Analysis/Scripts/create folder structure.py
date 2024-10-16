#create folder structure

import os

def create_folder_structure(base_path, folder_structure):
    """
    Create a folder structure based on the provided dictionary.
    
    :param base_path: The base path where the folder structure will be created.
    :param folder_structure: A dictionary representing the folder structure.
    """
    for folder, subfolders in folder_structure.items():
        # Create the main folder
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")
        
        # Recursively create subfolders
        if isinstance(subfolders, dict):
            create_folder_structure(path, subfolders)

# Define your custom folder structure as a dictionary
custom_structure = {
    'LRI CFD': {
        'NX': {
            'MODELS': {},
            'EXPS': {},
            'EXPORTS': {}
        },
    },
}

# Get the user's Documents folder
user_home = os.path.expanduser("~")
documents_path = os.path.join(user_home, 'Documents')

# Create the folder structure in the Documents folder
create_folder_structure(documents_path, custom_structure)