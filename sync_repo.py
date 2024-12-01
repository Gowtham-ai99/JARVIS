import os
import shutil
import subprocess
import time
import stat

# Configuration
REPO_URL = "https://github.com/Gowtham-ai99/JARVIS.git"  # Replace with your GitHub repository URL
LOCAL_DIR = "C:/Users/Home/Documents/python/master"  # Temporary location for the repository
BRANCH_NAME = "master"  # Branch to pull from

def run_git_command(command, cwd=None):
    """Run a Git command and handle errors."""
    try:
        result = subprocess.run(command, cwd=cwd, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def delete_existing_repo():
    """Delete the existing repository folder if it exists."""
    if os.path.exists(LOCAL_DIR):
        print(f"Deleting existing repository from {LOCAL_DIR}...")
        try:
            shutil.rmtree(LOCAL_DIR, onerror=force_remove_readonly)
            print("Existing repository deleted successfully.")
        except Exception as e:
            print(f"Error deleting existing repository: {e}")

def clone_repo():
    """Clone the repository from scratch."""
    print(f"Cloning repository into {LOCAL_DIR}...")
    run_git_command(["git", "clone", REPO_URL, LOCAL_DIR])
    print("Repository cloned successfully.")

def force_remove_readonly(func, path, exc_info):
    """Force removal of read-only files."""
    os.chmod(path, stat.S_IWRITE)  # Change the file permission to writable
    func(path)

def main():
    """Main function to manage cloning and cleaning up."""
    try:
        delete_existing_repo()  # Ensure the folder is removed before cloning
        clone_repo()  # Clone the repository afresh
    finally:
        print("Process completed.")

if __name__ == "__main__":
    main()
