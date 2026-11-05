import sys
import os
import hashlib  # functions to calculate checksum

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)    # takes 1024 bytes of input- standard size  # Unit on hard disk - block , Unit of RAM - page

    while(len(Buffer)>0):       # until length of buffer becomes 0
        hobj.update(Buffer)     # keeps updating the Checksum/hash the next 1000 bytes
        Buffer = fobj.read(1024)    

    fobj.close()

    return hobj.hexdigest()     # this is the checksum

def FindDuplicate(DirectoryName):
    Ret = False

    Ret = os.path.exists(DirectoryName) # path ahe ka baghitala

    if Ret == False:
        print("Path is invalid")
        return

    Ret = os.path.isdir(DirectoryName)  # directory ahe ka baghitali

    if Ret == False:
        print("It is not a directory")
        return

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fName in FileName:
            fName = os.path.join(FolderName,fName)  # relative path ala, (Marvellous,Demo) -> Marvellous/Demo

            Checksum = CalculateChecksum(fName)

            print(f"{fName} : {Checksum}")

def main():
    FindDuplicate("Marvellous")

if __name__ == "__main__":
    main()

# read() works for small files, but imagine hashing a 5 GB video.
# Reading the entire file at once would consume a huge amount of RAM.