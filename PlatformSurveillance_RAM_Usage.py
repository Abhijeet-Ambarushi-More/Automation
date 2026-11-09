import psutil
import sys
import os
import time
import schedule

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

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"Log file was created with name {FileName}")

    fobj.write(Border+"\n")     # By default new line la jat nahi
    fobj.write("----- Marvellous Platform Surveillance System -----\n")
    fobj.write("Log file gets created at : "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("--------------------System Report------------------\n")

    # CPU Information
    fobj.write("Number of active CPU cores : %s\n" %psutil.cpu_count())
    fobj.write("CPU usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    # RAM Information
    memory = psutil.virtual_memory()

    fobj.write("RAM usage : %s %%\n" %memory.percent)       # Bracket chi garaj nahi karan object banvla ahe
    fobj.write("Total RAM Availble : %s \n" %memory.total)
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("-------------------End of Log File------------------\n")
    fobj.write(Border+"\n")

    fobj.close()

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

    # Actual project code
    elif(len(sys.argv) == 3):

        # print("CPU Usage : ",psutil.cpu_percent())
        print("Schedular started successfully")
        print("Press Ctrl + C to abort the automation script")
        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurveillance, sys.argv[2])

        while True:
            schedule.run_pending()
            time.sleep(1)
        
    else:
        print("invalid number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h and --u flag for for getting more details")

    print(Border)
    print("Thank you for using our automation System")
    print(Border)


if __name__ == "__main__":
    main()