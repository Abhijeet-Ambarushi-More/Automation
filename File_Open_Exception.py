def main():
    try:
        open("Demo.txt","r")        # (r - read)  (w - create)
        print("File gets opened")

    except FileNotFoundError as fobj:
        print("File is not present in current directory")   
        # code band padla pan normally band padla..must handle exceptions in automation

if __name__ == "__main__":
    main()