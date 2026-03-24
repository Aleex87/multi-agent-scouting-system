import datetime
import os

# This file print in the terminal, write on a file and insert a timestamp.

LOG_FILE = "logs/workflow.log"

def log(message: str):
    os.makedirs("logs", exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"

    print(full_message)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(full_message + "\n")