import os
import sys

def read_files(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError("Directorul nu exista!")
   
        sum=0
        for (root, directories, files) in os.walk(directory):
            for fileName in files:
                full_fileName = os.path.join(root, fileName)
                try:
                    file = open(full_fileName, 'r', encoding='utf-8')
                    sum += sum + os.path.getsize(full_fileName)
                    file.close()
                except Exception as e:
                    print("Eroare la citirea fisierului!")                        
        print(sum)

    except FileNotFoundError as fnfe:
        print("ERROR: ",fnfe)
    except PermissionError as pe:
        print("ERROR: ", pe)
    except Exception as e:
        print("ERROR: ",e)

if len(sys.argv) != 2:
    print("Foloseste: python.exe d:/Facultate/A3S1/Programare-Python/Laboratoare/Lab7/Ex3.py <director>")
    sys.exit()

directory = sys.argv[1]
read_files(directory)

#python.exe d:/Facultate/A3S1/Programare-Python/Laboratoare/Lab7/Ex3.py D:\Facultate\A3S1\Programare-Python\Laboratoare\Lab7