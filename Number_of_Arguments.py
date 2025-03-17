import os

def create_folder_structure(parent_folder, sub_folder):
    parent_path = os.path.join(os.getcwd(), parent_folder)
    sub_folder_path = os.path.join(parent_path, sub_folder)

    # Check if the parent folder exists
    if not os.path.exists(parent_path):
        os.makedirs(parent_path)  # Create parent folder
        print(f"Created folder: {parent_path}")

    # Check if the sub-folder exists
    if not os.path.exists(sub_folder_path):
        os.makedirs(sub_folder_path)  # Create sub-folder
        print(f"Created sub-folder: {sub_folder_path}")
    else:
        print("Folders already exist. No action taken.")

if __name__ == "__main__":
    parent = input("Enter parent folder name: ")
    sub = input("Enter sub-folder name: ")
    create_folder_structure(parent, sub)

