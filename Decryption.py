import pyAesCrypt
from os import stat, remove

buffer = 65536

def Decrypt(fileName,key,decryptedFileName):
    size = stat(fileName).st_size
    with open(fileName,"rb") as fileR:
        try:
            with open(decryptedFileNAme,"wb") as fileW:
                pyAesCrypt.decryptStream(fileR,fileW,key,buffer,size)
        except:
            # Throw Exception and Handle it
            print("Null")