alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z"]



def caesarEncryption(string, key):
    encString = ""
    tmpSplit = string.split(" ")
    for j in tmpSplit:
        tempStrArr = list(j)
        for i in tempStrArr:
            temp = alphabets.index(i) + alphabets.index(key)
            encString += alphabets[temp%25]
        encString += " "

    return encString


def caesarDecryption(string, key):
    decString = ""
    tmpSplit = string.split(" ")
    for j in tmpSplit:
        tempStrArr = list(j)
        for i in tempStrArr:
            temp = alphabets.index(i) - alphabets.index(key)
            decString += alphabets[temp%25]
        decString += " "
    return decString



if __name__ == "__main__":
    print("Caesar Cipher")
    key = 'h'

    # getting input
    inp = raw_input("Enter the String to be encrypted: ")

    # encryption 
    encryptedString = caesarEncryption(inp, key)

    print("Encrypted String: "+ encryptedString)

    # decryption
    decryptedString = caesarDecryption(encryptedString, key)

    print("Decrypted String: "+ decryptedString)