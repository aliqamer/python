import uuid
import base64

def fun():
    data = generateUUID()
    print('uuid: '+str(data))
    # Standard Base64 Encoding
    encodedBytes = base64.b64encode(str(data).encode("utf-8"))
    encodedStr = str(encodedBytes)

    print(encodedStr)

    decodedUUID = base64.b64decode(encodedStr)
    print(decodedUUID)

def generateUUID():
    return uuid.uuid4()

if __name__ == '__main__':
    import sys
    fun()
