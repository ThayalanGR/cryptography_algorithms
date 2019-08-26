def calcT(t1, q, t2):
    return t1-(q*t2)

def eucledian(a, b):
    r1 = max([a, b])
    r2 = min([a, b])
    r = r1 % r2
    q = r1 // r2
    t1 = 0
    t2 = 1
    t = calcT(t1, q, t2)
    while True:
        if(r == 0):
            break
        r1 = r2
        r2 = r
        r = r1 % r2
        q = r1 // r2
        t1 = t2
        t2 = t
        t = calcT(t1, q, t2)
    return t2


if __name__ == "__main__":

    p=int(input("Enter p (only prime number is allowed): "))
    q=int(input("Enter q (only prime number is allowed): "))
    e=int(input("Enter the value of e: "))
    message=int(input("Enter the message length: "))
    n=p*q
    order=(p-1)*(q-1)
    d=eucledian(e,order)
    Enc=(message**e)%n
    Dec=(Enc**d)%n
    print(Enc,Dec)