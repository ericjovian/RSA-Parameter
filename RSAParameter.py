import sys
from random import randint
import math

pq = []

def isPrime(num, cycle):
    if num == 1:
        return False
    for x in range(cycle):
        val = randint(1, num - 1)
        if pow(val, num-1, num) != 1:
            return False
    return True

def generatePrime(n):
    notPrime = True
    while notPrime:
        p = randint(2**(n-1), 2**n)
        #cycle "p" 1000 times until a prime is found
        if isPrime(p, 1000):
            return p

def N(p,q):
    return p*q

def PhiN(p,q):
    return (p-1)*(q-1)

def e(N, phiN):
    n = []
    nn = []
    for i in range(2, N):
        n.append(i)
        for j in range (2, phiN):
            if(set(n) & set(nn)):
                return(set(n) & set(nn))
                break
            else:
                n.append(j)

def modInverse(e, phiN):
    if math.gcd(e, phiN) != 1:
        return None
    u1, u2, u3 = 1, 0, e
    v1, v2, v3 = 0, 1, phiN

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % phiN

def d(phiN,e):
    d = modInverse(e, phiN)
    return d



#shell arguments functions
def shellarg():
    p = sys.argv[1]
    q = sys.argv[2]
    if p.isdigit():
        p = int(p)
        if p > 31:
            pq.append(generatePrime(p))
        else:
            print("only accept more than 32-bit")
    else:
        print("please use the correct format")
    if q.isdigit():
        q = int(q)
        if q > 31:
            pq.append(generatePrime(q))
            pq.append(N(pq[0],pq[1]))
            pq.append(PhiN(pq[0],pq[1]))
            pq.append(65537)
            pq.append(d(pq[3],pq[4]))
            print(pq)
            with open('out.txt', 'w') as f:
                f.write("p: "+'%d' % pq[0]+'\n')
                f.write("q: "+'%d' % pq[1]+'\n')
                f.write("N: "+'%d' % pq[2]+'\n')
                f.write("e: "+'%d' % pq[4]+'\n')
                f.write("d: "+'%d' % pq[5])
                f.close()
        else:
            print("only accept more than 32-bit")
    else:
        print("please use the correct format")

shellarg()
