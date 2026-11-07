import os

def main():
    try:
        # fobj.remove() -> Not applicable
        os.remove("Demo.txt")

    except FileNotFoundError as fobj:
        print("File is not present in current directory")   
        # code band padla pan normally band padla..must handle exceptions in automation

if __name__ == "__main__":
    main()