import json
import requests
import os

# API Endpoints
CURRENT_QUIZ_URL = "https://www.jsonkeeper.com/b/LLQT"
USER_QUIZ_URL = "https://api.jsonserve.com/rJvd7g"
HISTORICAL_QUIZ_URL = "https://api.jsonserve.com/XgAgFJ"

# Directory to save the JSON files
DATA_DIR = "data"

# Ensure the directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Function to fetch data from API and save to file inside the data folder
def fetch_data(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(DATA_DIR, filename)  # Save inside data folder
        with open(file_path, "w") as f:
            json.dump(response.json(), f, indent=4)
        print(f"✅ {filename} saved successfully in {DATA_DIR}/")

# Main execution block
if __name__ == "__main__":
    fetch_data(CURRENT_QUIZ_URL, "current_quiz.json")
    fetch_data(USER_QUIZ_URL, "user_quiz.json")
    fetch_data(HISTORICAL_QUIZ_URL, "historical_quiz.json")
