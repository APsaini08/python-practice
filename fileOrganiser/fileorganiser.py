import os
import shutil

# Map extensions to folder names
EXTENSION_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".cpp", ".java", ".js", ".html", ".css", ".php"],
    "Others": []  # Anything not listed goes here
}

def organize_files(target_folder):
    # Check if folder exists
    if not os.path.isdir(target_folder):
        print("Error: The given folder path does not exist!")
        return

    # List all files
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Find matching category
        folder_name = "Others"
        for category, extensions in EXTENSION_MAP.items():
            if ext in extensions:
                folder_name = category
                break

        # Create target folder if not exists
        category_folder = os.path.join(target_folder, folder_name)
        os.makedirs(category_folder, exist_ok=True)

        # Move file
        shutil.move(file_path, os.path.join(category_folder, filename))
        print(f"Moved: {filename} -> {folder_name}/")

if __name__ == "__main__":
    path = input("Enter the folder path to organize: ").strip()
    organize_files(path)
    print("Organization complete!")
