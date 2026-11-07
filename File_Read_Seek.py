# seek(kuthe, kuthun)
# kuthun: 0/1/2

# 0 - Start
# 1 - Current
# 2 - End

def main():
    try:
        fobj = open("Demo.txt","r")        # (r - read)  (w - create) (a - append)
        print("File gets opened")

        fobj.seek(10,0)

        Data = fobj.read()

        print(Data)

    except FileNotFoundError as fobj:
        print("File is not present in current directory")   
        # code band padla pan normally band padla..must handle exceptions in automation

if __name__ == "__main__":
    main()