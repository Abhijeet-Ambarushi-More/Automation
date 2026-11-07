import sys
import os

def directoryScanner(Directorypath):
    print("Files from the directory are : ")
    
    fobj = open("Marvellous log.txt","w")

    fobj.write("Marvellous Automation Script\n")

    fobj.write("Files from the directory are : \n")

    for FolderName, SubFolder , Filename in os.walk(Directorypath):
        for fname in Filename:
            fobj.write(fname+"\n")   # je kahi banes te file madhe lihila jail

    fobj.close()

def main():
    Border = "-"*60
    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to trvael the directory")
            print("For better usage , please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("please execute the script as ")
            print("pyhton FileNem.py DirectoryName")
            print("Directory name should be absolute path")
        else:
            directoryScanner(sys.argv[1])
        
    else:
        print("Invalid number of arguments")
        print("please use --h or --u for more information ")

    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)

if __name__ == "__main__":
    main()
