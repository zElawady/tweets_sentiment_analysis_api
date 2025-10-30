import os
import sys
import subprocess

def main():
    # Add the project root directory to Python path
    project_root = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, project_root)
    
    # Get the path to the frontend file
    frontend_path = os.path.join(project_root, "src", "view", "frontend.py")
    
    # Run the Streamlit app using subprocess
    try:
        subprocess.run(["streamlit", "run", frontend_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit app: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nShutting down...")
        sys.exit(0)

if __name__ == "__main__":
    main() 
