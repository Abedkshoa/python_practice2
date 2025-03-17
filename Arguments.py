def print_name_upper(name):
    print(name.upper())

# Example usage:
print_name_upper("abed_kshoa")



import os

def list_of_files(path):
    try:
        files = os.listdir(path)
        print("Files in directory:", ", ".join(files))
    except FileNotFoundError:
        print("Error: Path not found")
    except PermissionError:
        print("Error: Permission denied")

# Example usage:
# list_of_files("/path/to/folder")
