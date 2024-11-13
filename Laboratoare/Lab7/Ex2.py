import os

def rename_files_in_directory(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError("Directorul nu exista!")
        
        files = os.listdir(directory)
        index=1
                
        for (root, directories, files) in os.walk(directory):
            for fileName in files:
                old_path = os.path.join(root, fileName)
                if os.path.isfile(old_path):
                    extension = os.path.splitext(old_path)[1]
                    new_filename = f"file{index}{extension}"
                    index += 1
                    new_path = os.path.join(directory, new_filename)
                    os.rename(old_path, new_path)
                
    except FileNotFoundError as fnfe:
        print("ERROR: ", fnfe)
    except PermissionError as pe:
        print("ERROR: ", pe)
    except Exception as e:
        print("ERROR: ", e)

rename_files_in_directory("./Laboratoare/Lab7/FolderEX2")