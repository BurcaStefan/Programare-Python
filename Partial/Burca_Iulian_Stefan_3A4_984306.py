import sys
import os

def main():
    try:
        
        if len(sys.argv) != 2:
            raise Exception("Nr invalid de param")
        file=sys.argv[1]
        if not os.path.isfile(file):
            raise FileNotFoundError("Fisierul nu exista")
        
        content=open(file, 'r').read().split()
        for line in content:
            count=0
            for ch in line:
                if ch==".":
                    count+=1
            if count==3:
                for ch in line:
                    if ch==".":
                        ch.replace(".", " ")
                vectorx=line.split()
                for xi in vectorx:
                    print(xi)
            # for ch in line:
            #     if ch==":":
            #         count+=1
            # if count==7:
            #     for ch in line:
            #         if ch==":":
            #             ch.replace(":", " ")
            #     vectorx=line.split()
            #     for xi in vectorx:
            #         print(xi)
    except FileNotFoundError as e:
        print(f"Eroare la fisier: {e}") 
    except Exception as e:
        print(f"Eroare: {e}")

if __name__=="__main__":  
    main()    

        
    
    