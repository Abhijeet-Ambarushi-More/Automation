import sys

def main():
    print("--------------------------------------------------------------------------------")
    print("Marvellous Automation Script")
    print("--------------------------------------------------------------------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to trvael the directory")
            print("For better usage , please check --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("please execute the script as ")
            print("pyhton FileNem.py DirectoryName")
            print("Directory name should be absolute path")
        else:
            DirectoryName = sys.argv[1]     # args[0] is filename which we runiing in cmd
            print("Directory is : ",DirectoryName)
        
    else:
        print("Invalid number of arguments")
        print("please use --h or --u for more information ")

    print("--------------------------------------------------------------------------------")
    print("Thank you for using Marvellous Automation Script")
    print("--------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
