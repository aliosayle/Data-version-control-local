from flask import Flask, request, jsonify
import os
import shutil
import datetime

app = Flask(__name__)

# Define the directory to store versions
version_directory = "dataset_versions"

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
    return f"Saved current dataset version as {version_path}"

def load_version(timestamp, output_path):
    # Find the directory corresponding to the given timestamp
    version_path = os.path.join(version_directory, timestamp)
    if not os.path.exists(version_path):
        return f"Version {timestamp} does not exist.", 404
    # Copy the version back to the specified output path
    dataset_filename = os.listdir(version_path)[0]
    dataset_version_path = os.path.join(version_path, dataset_filename)
    shutil.copy(dataset_version_path, output_path)
    return f"Loaded dataset version {timestamp} to {output_path}"

@app.route('/save', methods=['POST'])
def save():
    file = request.files['file']
    dataset_path = os.path.join("uploads", file.filename)
    if not os.path.exists("uploads"):
        os.makedirs("uploads")
    file.save(dataset_path)
    result = save_version(dataset_path)
    return jsonify({"message": result})

@app.route('/load', methods=['GET'])
def load():
    timestamp = request.args.get('timestamp')
    output_filename = request.args.get('output')
    output_path = os.path.join("downloads", output_filename)
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    result, status_code = load_version(timestamp, output_path)
    return jsonify({"message": result}), status_code

if __name__ == '__main__':
    app.run(debug=True)
