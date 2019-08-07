def isPrime(inpt):
    for i in range(2, inpt):
        if(j % i == 0):
            return False
    return True



if __name__ == "__main__":

    inp = int(input("Enter a number: "))

    for j in range(2, inp+1):
        if(isPrime(j)):
            print(str(j) +" - prime")
        else:
            print(str(j) +" - not prime")
            

