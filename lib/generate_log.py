from datetime import datetime
import os
import requests

def generate_log(data):
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, 'w') as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    print(f"Log written to {filename}")

    pass

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
