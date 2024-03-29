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
    print("q r1 r2 r | t1 t2 t")
    # print(str(q) +" "+ str(r1) +" "+ str(r2) +" "+ str(r) + " | " +str(t1) +" "+ str(t2) +" "+ str(t))
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
        # print(str(q) +" "+ str(r1) +" "+ str(r2) +" "+ str(r) + " | " +str(t1) +" "+ str(t2) +" "+ str(t))
    return t2


if __name__ == "__main__":
    p=int(input("Enter p: "))
    q=int(input("Enter q: "))
    e=int(input("Enter e: "))
    message=int(input("Enter m: "))
    n=p*q
    order=(p-1)*(q-1)
    d=eucledian(e,order)
    if(d < 0):
        d += order
    print("d", d)
    Enc=(message**e)%n
    Dec=(Enc**d)%n
    print("Encryption: ", Enc)
    print("Decryption: ", Dec)

# output :-
# Enter p: 3
# Enter q: 11
# Enter e: 17
# Enter m: 3
# d 13
# Encryption:  9
# Decryption:  3