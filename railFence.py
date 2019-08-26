
def railFenceEncryption(inpStr):
    output = ""
    odd = ""
    even = ""
    for i in range(len(inpStr)):
        if((i+1) % 2 == 0):
            even += inpStr[i]
        else:
            odd += inpStr[i]
    output  += odd + even
    return output

def railFenceDecryption(inpStr):
    output = ""
    if(len(inpStr) % 2 != 0):
        n = (len(inpStr)//2) + 1
    else:
        n = (len(inpStr)//2)
    for i in range(n):
        output += inpStr[i]
        if(n+i < len(inpStr)):
            output += inpStr[n+i]
    return output

if __name__ == "__main__":
    inp = str(input("Enter the String to be Encrypted: "))
    # generating cipher
    encString = railFenceEncryption(inp)
    print("Encrypted String: "+ encString)
    # decrypting cipher
    decString = railFenceDecryption(encString)
    print("Decrypted String: "+ decString)

