from pathlib import Path

def find_file(filename):
    root = Path(__file__).parent 
    matches = list(root.rglob(filename))

    if matches:
        file_path = matches[0]
        print("Found:", file_path)
        return file_path.resolve()
    else:
        print("File not found")
        return None