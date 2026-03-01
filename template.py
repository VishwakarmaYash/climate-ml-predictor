import os

# Base project folder
base_folder = "climate-web-app"

# Folder structure
folders = [
    "client",
    "server/routes",
    "server/controllers",
    "server/model",
    "ml-model",
    "dataset"
]

# Files to create
files = {
    "server/app.js": "",
    "ml-model/train.py": "",
    "ml-model/predict.py": "",
    "ml-model/model.pkl": ""   # Empty placeholder
}

def create_structure():
    print("Creating project structure...\n")

    # Create base folder
    os.makedirs(base_folder, exist_ok=True)

    # Create folders
    for folder in folders:
        path = os.path.join(base_folder, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")

    # Create files
    for file_path, content in files.items():
        full_path = os.path.join(base_folder, file_path)
        with open(full_path, "w") as f:
            f.write(content)
        print(f"Created file: {full_path}")

    print("\n✅ Project structure created successfully!")

if __name__ == "__main__":
    create_structure()