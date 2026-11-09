import psutil
import sys
import os

def PlatformSurveillance(FolderName):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)
    if (Ret == True):
        Ret = os.path.isdir(FolderName)
        print("Unable to process as directory name is existing but its not a directory ")
    else:
        os.mkdir(FolderName)        # make a new folder with the given name
        print("Directory for the log file gets created successfully")


def main():
    Border = "-"*50
    print(Border)
    print("---- Marvellous Platform Surveillance System ----")
    print(Border)

    # --h & --u handling
    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to perform ")
            print("1 : It fetches the information of running processess")
            print("2 : It fetches the information about the primary storage as RAM")
            print("3 : It fetches the information about the secondar storage as HDD")
            print("4 : It fetches the information about the microprocessor")
            print("5 : It gets auto scheduled periodically")
            print("6 : It maintains all records into log file")
            print("7 : It sends the log files through mail periodically")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for the log file creation")
        else:
            print("Unable to proceed as there is no matching arguments")
            print("Please use --h and --u flag for for getting more details")
    elif(len(sys.argv) == 3):
        PlatformSurveillance(sys.argv[2])   # ya navacha folder bananar
        
    else:
        print("invalid number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h and --u flag for for getting more details")

    print(Border)
    print("Thank you for using our automation System")
    print(Border)


if __name__ == "__main__":
    main()