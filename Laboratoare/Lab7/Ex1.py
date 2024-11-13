import sys
import os

def read_files(directory, extension):
    try:
        if not os.path.isdir(directory):
            raise ValueError("Calea directorului invalida!")
    
        valid_extensions = ['.txt', '.py']
        if extension not in valid_extensions:
            raise ValueError("Extensia invalida!")

        for (root, directories, files) in os.walk(directory):
            for fileName in files:
                full_fileName = os.path.join(root, fileName)
                if full_fileName.endswith(extension):
                    print("\n\n----------------------------------------", full_fileName, "----------------------------------------")
                    try:
                        file = open(full_fileName, 'r', encoding='utf-8')
                        print(file.read())
                        file.close()
                    except Exception as e:
                        print("Eroare la citirea fisierului!")                        

    except ValueError as ve:
        print("ERROR: ", ve)
    except Exception as e:
        print("ERROR: ", e)


if len(sys.argv) != 3:
    print("Foloseste: python.exe d:/Facultate/A3S1/Programare-Python/Laboratoare/Lab7/Ex1.py <director> <extensie>")
    sys.exit()

directory = sys.argv[1]
extension = sys.argv[2]

read_files(directory, extension)

#python.exe d:/Facultate/A3S1/Programare-Python/Laboratoare/Lab7/Ex1.py D:\Facultate\A3S1\Programare-Python\Laboratoare\Lab7 .py 