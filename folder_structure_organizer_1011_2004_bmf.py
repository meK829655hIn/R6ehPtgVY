# 代码生成时间: 2025-10-11 20:04:41
import os
import shutil
from gradio import Interface, File, Folder
from pathlib import Path

"""
File and folder structure organizer using Gradio framework.
This script allows a user to select a folder and automatically organizes its contents into subfolders.
"""

def organize_folder_contents(folder_path: Path):
    """
    Organize the contents of a given folder into subfolders.

    Args:
        folder_path (Path): The path to the folder to be organized.

    Returns:
        None
    """
    try:
        # Ensure the path exists
        if not folder_path.exists():
            raise FileNotFoundError(f"The folder {folder_path} does not exist.")

        # Create a dictionary to hold file extensions and their corresponding subfolders
        extension_subfolders = {}

        # Iterate over each file in the folder
        for file in folder_path.iterdir():
            if file.is_file():
                # Extract the file extension
                extension = file.suffix.lower()
                if extension not in extension_subfolders:
                    # Create a new subfolder for the file extension
                    extension_subfolder = folder_path / (extension[1:] + '_files')
                    extension_subfolder.mkdir(parents=True, exist_ok=True)
                    extension_subfolders[extension] = extension_subfolder

                # Move the file to the corresponding subfolder
                shutil.move(str(file), str(extension_subfolders[extension] / file.name))
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to create the Gradio interface for folder structure organizer.
    """
    def on_submit(folder: Folder):
        """
        Function to handle form submission.
        Organize the contents of the selected folder.
        """
        organize_folder_contents(folder)
        return True

    interface = Interface(
        fn=on_submit,
        inputs=Folder(label="Select a folder to organize"),
        outputs="text",
        title="Folder Structure Organizer",
        description="Automatically organize the contents of a folder into subfolders."
    )
    interface.launch()

if __name__ == "__main__":
    main()