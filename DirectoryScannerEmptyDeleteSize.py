import sys
import os
import time
import schedule


def directoryScanner(Directorypath = "Marvellous"): 
    Border = "-"*60

    timestamp = time.ctime()
    LogFileName = "Marvellous %s.log"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    Ret = False

    Ret = os.path.exists(Directorypath)

    if (Ret == False):
        print("Marvellous Automation Error : There is no such directory with name",Directorypath)
        return
    
    Ret = os.path.isdir(Directorypath)

    if(Ret == False):
        print("Marvellous automation error : It is not a directory with name",Directorypath)
        return
    
    print("Log file gets created with name : ",LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("Marvellous Automation Script\n")
    fobj.write(Border+"\n\n")

    fobj.write("Files from the directory are : \n")
    fobj.write(Border+"\n\n")

    for FolderName, SubFolder , Filename in os.walk(Directorypath):
        for fname in Filename:
            fname = os.path.join(FolderName,fname)      # this solved the issue of name test1.txt which was created from vs code
            fobj.write(fname+"\n")   # je kahi banes te file madhe lihila jail

            print(f"File name {fname} : {os.path.getsize(fname)} bytes")

    fobj.write(Border+"\n")
    fobj.write("Log file gets created at : "+timestamp)
    fobj.write("\n"+Border+"\n")

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
            # schedule.every(1).minute.do(directoryScanner, sys.argv[1])
            directoryScanner(sys.argv[1])

            # while True:
                # schedule.run_pending()
                # time.sleep(1)
        
    else:
        print("Invalid number of arguments")
        print("please use --h or --u for more information ")

    print(Border)
    print("Thank you for using Marvellous Automation Script")
    print(Border)

if __name__ == "__main__":
    main()
