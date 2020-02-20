import pyAesCrypt

buffer = 65536

def Encrypt(fileName,key,encryptedFileName):
    with open(fileName,"rb") as fileR:
        with open(encryptedFileName,"wb") as fileW:
            pyAesCrypt.encryptStream(fileR,fileW,key,buffer)