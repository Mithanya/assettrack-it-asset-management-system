import sys
import os

# Add the 'src' directory to Python's module search path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
sys.path.insert(0, src_path)

# Now we can safely import and run the main application from the src folder
import main as app_main

if __name__ == "__main__":
    app_main.main()
