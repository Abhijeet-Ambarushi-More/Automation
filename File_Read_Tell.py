def main():
    try:
        fobj = open("Demo.txt","r")        # (r - read)  (w - create) (a - append)
        print("File gets opened")

        print("File offset is : ",fobj.tell())

        Data = fobj.read(10)     # Array # deletes previous data and replace with this

        print(Data)

        print("File offset is : ",fobj.tell())

        fobj.close()    # Good practice to close the file at the end if we opened it

    except FileNotFoundError as fobj:
        print("File is not present in current directory")   
        # code band padla pan normally band padla..must handle exceptions in automation

if __name__ == "__main__":
    main()