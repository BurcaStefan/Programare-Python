import sys
import os

def read_files(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError("Directorul nu exista!")

        extension_py=0
        extension_txt=0
        for (root, directories, files) in os.walk(directory):            
            if not os.access(directory, os.R_OK):
                raise PermissionError("Nu aveti permisiunea de a citi directorul!")
            
            for fileName in files:
                full_fileName = os.path.join(root, fileName)
                print(full_fileName)
                if full_fileName.endswith(".py"):
                    extension_py += 1
                elif full_fileName.endswith(".txt"):
                    extension_txt += 1

    except ValueError as ve:
        print("ERROR: ",ve)
    except FileNotFoundError as fnfe:
        print("ERROR: ",fnfe)
    except Exception as e:
        print("ERROR: ",e)
        
    return extension_py, extension_txt

if len(sys.argv) != 2:
    print("Foloseste: python.exe d:/Facultate/A3S1/Programare-Python/Lab7/Ex4.py <director>")
    sys.exit()

directory = sys.argv[1]
ext_py, ext_txt = read_files(directory)
print("Numarul de fisiere .py: ", ext_py)
print("Numarul de fisiere .txt: ", ext_txt)



#python.exe d:/Facultate/A3S1/Programare-Python/Laboratoare/Lab7/Ex4.py D:\Facultate\A3S1\Programare-Python\Laboratoare