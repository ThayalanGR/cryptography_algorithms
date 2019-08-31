def diffeHellman(q, alp, xa, xb):
    ya = (alp ** xa) % q
    yb = (alp ** xb) % q
    print("Ya: ", ya)
    print("Yb: ", yb)

    a = (yb ** xa) % q
    b = (ya ** xb) % q

    print("a: ", a)
    print("b: ", b)

if __name__ == "__main__":
    q, alp, xa, xb = list(map(int, input("Enter values of q, alp, xa, xb: ").split(" ")))
    diffeHellman(q, alp, xa, xb)

# output:-
# Enter values of q, alp, xa, xb: 13 3 11 17
# Ya:  9
# Yb:  9
# a:  3
# b:  3