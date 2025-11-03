# 代码生成时间: 2025-11-03 23:59:46
import os
import shutil
import gr
from gr import Interface

"""
This module provides a simple data backup and restore functionality using Grap
"""

class DataBackupRestore:

    def __init__(self, backup_path, restore_path):
        """
        Initializes the DataBackupRestore class with the given backup and restore paths.
        """
        self.backup_path = backup_path
        self.restore_path = restore_path

    def backup_data(self):
        """
        Creates a backup of the data by copying the files to the backup location.
        """
        try:
            # Ensure the backup directory exists
            os.makedirs(self.backup_path, exist_ok=True)
            # Copy data from original location to backup location
            for file in os.listdir(self.restore_path):
                shutil.copy(os.path.join(self.restore_path, file), self.backup_path)
            print("Data backup successful.")
        except Exception as e:
            print(f"Error during backup: {e}")

    def restore_data(self):
        """
        Restores the data from the backup location to the original location.
        """
        try:
            # Copy data from backup location to original location
            for file in os.listdir(self.backup_path):
                shutil.copy(os.path.join(self.backup_path, file), self.restore_path)
            print("Data restore successful.")
        except Exception as e:
            print(f"Error during restore: {e}")

    def handle_backup(self, input_file):
        """
        Handles the backup process based on the input file.
        """
        self.backup_data()
        return "Backup completed successfully."

    def handle_restore(self, input_file):
        """
        Handles the restore process based on the input file.
        """
        self.restore_data()
        return "Restore completed successfully."

# Define paths
backup_path = "./backup"
restore_path = "./restore"

# Create an instance of DataBackupRestore
data_manager = DataBackupRestore(backup_path, restore_path)

# Create a Grap interface
iface = Interface("Data Backup and Restore Service")

# Add backup and restore buttons
iface.add("Select backup", "text", "", data_manager.handle_backup)
iface.add("Select restore", "text", "", data_manager.handle_restore)

# Run the Grap interface
iface.launch()
