import os
import shutil
import datetime
import pandas as pd

version_directory = "dataset_versions"
version_history_file = os.path.join(version_directory, "version_history.txt")

# Create the version directory if it doesn't exist
if not os.path.exists(version_directory):
    os.makedirs(version_directory)

def save_version():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    version_path = os.path.join(version_directory, timestamp)
    os.makedirs(version_path)

    for file in os.listdir():
        if file.endswith(".csv"):
            shutil.copy(file, version_path)

    with open(version_history_file, "a") as f:
        f.write(f"{timestamp}: Saved current dataset version\n")
    print(f"Saved current dataset version as {version_path}")

def load_version(timestamp, output_directory):
    # Find the directory corresponding to the given timestamp
    version_path = os.path.join(version_directory, timestamp)
    if not os.path.exists(version_path):
        print(f"Version {timestamp} does not exist.")
        return
    
    # Copy the version back to the specified output directory
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file in os.listdir(version_path):
        dataset_version_path = os.path.join(version_path, file)
        shutil.copy(dataset_version_path, output_directory)
    
    print(f"Loaded dataset version {timestamp} to {output_directory}")

def main():
    action = input("Do you want to save a snapshot or restore a previous version? (save/restore): ").strip().lower()

    if action == "save":
        save_version()
    elif action == "restore":
        timestamp = input("Enter the timestamp of the version you want to restore (YYYYMMDD_HHMMSS): ").strip()
        output_directory = input("Enter the directory where you want to restore the files: ").strip()
        load_version(timestamp, output_directory)
    else:
        print("Invalid action. Please choose 'save' or 'restore'.")

if __name__ == "__main__":
    main()
