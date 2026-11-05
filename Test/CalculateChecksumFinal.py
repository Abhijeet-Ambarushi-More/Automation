import sys
import os
import hashlib  # functions to calculate checksum

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)    # takes 1024 bytes of input- standard size

    while(len(Buffer)>0):       # until length of buffer becomes 0
        hobj.update(Buffer)     # keeps updating the Checksum/hash the next 1000 bytes
        Buffer = fobj.read(1024)   # Unit on hard disk - block , Unit of RAM - page

    fobj.close()

    return hobj.hexdigest()     # this is the checksum

def main():
    Ret = CalculateChecksum("DemoX.txt")

    print("Checksum of file is : ",Ret)

if __name__ == "__main__":
    main()

# read() works for small files, but imagine hashing a 5 GB video.
# Reading the entire file at once would consume a huge amount of RAM.