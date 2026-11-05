def main():
    try:
        fobj = open("Demo.txt","w")        # (r - read)  (w - create)
        print("File gets opened")

        fobj.close()    # Good practice to close the file at the end if we opened it

    except FileNotFoundError as fobj:
        print("File is not present in current directory")   
        # code band padla pan normally band padla..must handle exceptions in automation

if __name__ == "__main__":
    main()