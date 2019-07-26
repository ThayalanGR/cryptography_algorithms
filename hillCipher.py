
balance = 0


def hillCipher(salt, inputString):
    global balance
    
    hashString = []
    
    alphabetsArr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "x"]

    inputArr = []

    lenOfTheString = len(inputString)

    if(lenOfTheString == 3):
        inputArr.append(inputString)
    elif(lenOfTheString < 3):
        tempStr = inputString
        temp = lenOfTheString % 3
        while (temp < 3):
            tempStr += "x"
            temp += 1
        inputArr.append(tempStr)
    elif(lenOfTheString > 3):
        temp = lenOfTheString
        tempStr = ""
        count = 1
        secondaryCount = 1
        tempCount = temp % 3
        decide = temp - tempCount
        for i in inputString:
            if(secondaryCount <= decide):
                if(count == 3):
                    tempStr += i
                    count = 1
                    inputArr.append(tempStr)
                    tempStr = ""
                else:
                    tempStr += i
                    count += 1  
            else:
                tempStr = ""
                modulusValue = 3 - len(inputString[decide:])
                balance = modulusValue
                tempStr = inputString[decide : ] + ("x" * modulusValue)
                inputArr.append(tempStr)
                break
            secondaryCount += 1

    print(inputArr)
    for k in inputArr:
        tempArr = []
        for i in salt:
            tempSum = 0
            for j in range(0, len(i)):
                tempSum += i[j] * alphabetsArr.index(k[j])

            tempArr.append(tempSum % 25)
        
        for i in tempArr:
            hashString.append(alphabetsArr[i])



    return "".join(hashString)



if __name__ == "__main__":

    # key matrix
    keyMatrix = [[1, 2, 1], [2, 3, 2], [2, 2, 1]]

    # inverse key matrix
    inverseKeyMatrix = [[-1, 0, 1], [2, -1, 0], [-2, 2, -1]]

    # get string to encrypt
    inputStr = raw_input("Enter the String to be encrypted : ")
    print("Entered String : "+ inputStr)

    # encrypt the string

    encryptedString = hillCipher(keyMatrix, inputStr)

    print("Encrypted String : "+ encryptedString)

    # decrypt the string

    decryptedString = hillCipher(inverseKeyMatrix, encryptedString)

    print("Decrypted String : "+  decryptedString[:len(decryptedString)-balance])
