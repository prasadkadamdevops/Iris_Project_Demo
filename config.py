import os

PORT_NUMBER = 5004

# Update file paths to match the correct file name
MODEL_FILE_PATH = os.path.join("data", "iris.pkl")
JSON_FILE_PATH = os.path.join("data", "data.json")

# Print current working directory and paths to check if they are correct
print("Current Working Directory:", os.getcwd())
print("Model File Path:", MODEL_FILE_PATH)
print("JSON File Path:", JSON_FILE_PATH)

