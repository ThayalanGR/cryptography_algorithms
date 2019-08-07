import re

def generatePlayfairCipher(key, inpStr):
    # declare necessary variables
    encString = ""
    encArr = []
    keyMatrix = []
    alphabets = []
    spaces = []
    aggArr = []
    startAlp = 97
    # generate alphabets
    for i in range(26):
        if(not startAlp == 106):
            alphabets.append(chr(startAlp))
        startAlp += 1
    
    # generate key matrix 5 * 5
    # remove spaces in the input key text and remove duplicate characters
    textMat = list(dict.fromkeys(list(key.replace(" ", ""))))
    if "j" in textMat:
        tempIndex = textMat.index("j")
        textMat[tempIndex] = "i"
    keyMatrix.extend(textMat)
    for i in alphabets:
        if not i in textMat:
            keyMatrix.append(i)
    print(keyMatrix)
    keyMatrix = [keyMatrix[i: i+5] for i in range(0, len(keyMatrix), 5)]
    print(keyMatrix)
    # aggregate input string and create digraphs
    # finding index of spaces using regular expression
    patt = re.finditer('\s+', inpStr)
    spaces = [i.start(0) for i in patt]
    print(spaces)
    # removing spaces form inpstring and splitting the string into digraphs
    tempStr = inpStr.replace(" ", "")
    if(len(tempStr) % 2 != 0):
        tempStr += "x"

    print(tempStr)
    # split string into digraphs
    aggArr = [list(tempStr[i:i+2]) for i in range(0, len(tempStr), 2)]
    print(aggArr)

    # process digraphs => compare with key matrix and genrate ciphre
    for i in aggArr:
        print(i)
        tempi = 0
        tempj = 0
        for j in keyMatrix:
            print(j)
            if(i[0] in j):
                tempi = [keyMatrix.index(j), j.index(i[0])]
            if(i[1] in j):
                tempj = [keyMatrix.index(j), j.index(i[1])]
        print("tempi", tempi)
        print("tempj", tempj)

        # all cases with key matrix intersection
        if(tempi == tempj):
            # both are same element
            print("same")

            pass
        elif(tempi[1] == tempj[1] and not tempi[0] == tempj[0]):
            # horizontal
            print("vertical")
            encArr.extend([keyMatrix[tempi[0]][tempi[1]+1 % 5], keyMatrix[tempj[0]][tempj[1]+1 % 5]])


        elif(tempi[0] == tempj[0] and not tempi[1] == tempj[1]):
            # vertical
            print("horizontal")
            encArr.extend([keyMatrix[tempi[0]][tempi[1]+1 % 5], keyMatrix[tempj[0]][tempj[1]+1 % 5]])
        else:
            # intersection
            print("intersection")
            encArr.extend([keyMatrix[tempj[0]][tempj[1]+1 % 5], keyMatrix[tempi[0]][tempi[1]-1 % 5]])
    # return encrypted string
    print(encArr)

    return encString


if __name__ == "__main__":
    # get key text
    keyTxt = str(input("Enter the key text: "))

    # get input string to be encrypted
    inpString = str(input("Enter the input string to be encrypted: "))

    # call the generatePlayfairCipher method 
    encryptedString = generatePlayfairCipher(keyTxt, inpString)

    # print encrypted string
    print(encryptedString)
    # decryption logic

    # call decryptcipher method give input as key and enc string

    # print decrypted string