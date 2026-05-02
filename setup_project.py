import whitebox
import os

def verify_environment():
    """Checks for WBT binary and creates necessary folders."""
    if not os.path.exists("./WBT"):
        print("MISSING: WhiteboxTools binary folder. Please download it.")
    
    # Create data folders if they don't exist
    folders = ["data/raw", "data/processed", "models"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    
    print("Environment Verified.")

if __name__ == "__main__":
    verify_environment()