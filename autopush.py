import subprocess
import os
import time
from datetime import datetime
import pytz  # Ensure pytz is installed (pip install pytz)

# Define your repository location
repo_dir = 'C:/Users/Home/Documents/python/'

# Change the working directory to your repo
os.chdir(repo_dir)

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result

def check_and_push_changes():
    # Check if there are any changes
    status = run_command('git status --porcelain')

    if status.stdout:
        print("Changes detected, committing and pushing to remote...")
        
        # Stage changes
        run_command('git add .')

        # Generate the current timestamp in IST
        ist_timezone = pytz.timezone("Asia/Kolkata")
        current_time = datetime.now(ist_timezone).strftime("%d/%m/%y at %H:%M IST")
        commit_message = f"Automated commit on {current_time}"

        # Commit changes
        run_command(f'git commit -m "{commit_message}"')

        # Push to GitHub
        run_command('git push origin master')
        print("Changes pushed to GitHub.")
    else:
        print("No changes detected.")
        print("Will check after 120 seconds.")

# This script will run every 2 minutes (120 seconds)
while True:
    check_and_push_changes()
    time.sleep(120)  # Wait for 2 minutes before checking again