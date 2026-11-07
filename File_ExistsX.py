import os

def main():
    if(os.path.exists("Demo.txt")):
        print("File present in current directory")
    else:
        print("No such file in the directory")

if __name__ == "__main__":
    main()