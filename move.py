import os
import shutil
import time


def move_files(extensions, folder_name):
    extensions = [ext.strip() for ext in extensions.split(",")]
    num_moved = 0
    total_files = 0

    def move_files_recursively(folder_path):
        nonlocal num_moved
        nonlocal total_files
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_name, file_ext = os.path.splitext(file)
                file_ext = file_ext.replace(".", "")
                total_files += 1
                if file_ext in extensions:
                    new_folder = os.path.join(os.path.dirname(folder_path), folder_name)
                    os.makedirs(new_folder, exist_ok=True)
                    src = os.path.join(root, file)
                    dst = os.path.join(new_folder, file)
                    shutil.move(src, dst)
                    num_moved += 1

    print("Processing...")
    move_files_recursively("Unknown folder")
    print(f"\n{num_moved} files were moved.")
    print("Process completed!")


# Solicitar ao usuário as extensões dos arquivos
extensions = input("Enter the file extensions separated by commas: ")
folder_name = input("Enter the folder name (press enter to keep the default name): ")
if not folder_name:
    folder_name = extensions.split(",")[0]

move_files(extensions, folder_name)


