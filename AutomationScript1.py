import sys

def main():
    DirectoryName = sys.argv[1]     # args[0] is filename which we runiing in cmd

    print(len(sys.argv))
    print("Directory is : ",DirectoryName)

if __name__ == "__main__":
    main()
