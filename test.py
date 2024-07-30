import os
import shutil
import datetime
import pandas as pd

# Define the directory to store versions and the version history file
version_directory = "dataset_versions"
version_history_file = os.path.join(version_directory, "version_history.txt")

# Create the version directory if it doesn't exist
if not os.path.exists(version_directory):
    os.makedirs(version_directory)

def save_version(dataset_path):
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # Create a new directory for this version
    version_path = os.path.join(version_directory, timestamp)
    os.makedirs(version_path)
    # Copy the dataset to the new directory
    shutil.copy(dataset_path, version_path)
    # Log the version to the version history file
    with open(version_history_file, "a") as f:
        f.write(f"{timestamp}: Saved current dataset version\n")
    print(f"Saved current dataset version as {version_path}")

def load_version(timestamp, output_path):
    # Find the directory corresponding to the given timestamp
    version_path = os.path.join(version_directory, timestamp)
    if not os.path.exists(version_path):
        print(f"Version {timestamp} does not exist.")
        return
    # Copy the version back to the specified output path
    dataset_filename = os.listdir(version_path)[0]
    dataset_version_path = os.path.join(version_path, dataset_filename)
    shutil.copy(dataset_version_path, output_path)
    print(f"Loaded dataset version {timestamp} to {output_path}")

# Example usage
current_dataset_path = "earthquake_data.csv"

# Save the current version
save_version(current_dataset_path)

# Load a previous version
load_version("20230728_154530", "reverted_dataset.csv")
