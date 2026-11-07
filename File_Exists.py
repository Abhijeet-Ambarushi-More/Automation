import os

def main():
    ret = os.path.exists("Demo.txt")
    
    if(ret == True):
        print("File present in current directory")
    else:
        print("No such file in the directory")

if __name__ == "__main__":
    main()