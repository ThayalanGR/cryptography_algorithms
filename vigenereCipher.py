def polyAlphabetic(inpStr, hashKey, isEncrypt):
    outputStr = []

    inpStrArr = inpStr.split(" ")

    if(isEncrypt):
        # encryption code
        for i in inpStrArr:
            print(i)
            tempKey = hashKey
            if(len(i) > len(hashKey)):
                tempLen = len(i) - len(hashKey)
                tempKey = hashKey * tempLen
            tempArr = []
            for j in range(0, len(i)):
                print(i[j], tempKey[j])
                tempSum = alphabets.index(i[j]) + alphabets.index(tempKey[j])
                print(tempSum)
                tempArr.append(alphabets[tempSum % 25])

            print(tempArr)
            outputStr.append("".join(tempArr))


    else:
        # decryption code
         # encryption code
        for i in inpStrArr:
            print(i)
            tempKey = hashKey
            if(len(i) > len(hashKey)):
                tempLen = len(i) - len(hashKey)
                tempKey = hashKey * tempLen
            tempArr = []
            for j in range(0, len(i)):
                print(i[j], tempKey[j])
                tempSum = alphabets.index(i[j]) - alphabets.index(tempKey[j])
                print(tempSum)
                tempArr.append(alphabets[tempSum % 25])

            print(tempArr)
            outputStr.append("".join(tempArr))



    return " ".join(outputStr)



if __name__ == "__main__":

    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z"]

    # get key
    key = raw_input("Enter the Key : " )

    print("Entered Key : "+ key)

    # get String
    inputString = raw_input("Enter the String to be encrypted : ")

    print("Entered String : " + inputString)

    # encrypt

    encryptedString = polyAlphabetic(inputString, key, True)

    print("Encrypted String: "+ encryptedString)

    # decrypt

    decryptedString = polyAlphabetic(encryptedString, key, False)

    print("Decrypted String: "+ decryptedString)

