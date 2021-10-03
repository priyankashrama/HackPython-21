import sys
sys.setrecursionlimit(10**6)

def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]  #initiate array named prime with all value True, ie everynumber [0,n] are prime
    p = 2
    while (p * p <= n):
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):  #if any number is prime then its multiple must be composite
            # Update all multiples of p to be not prime 
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1


    '''
        till here the status of code is:
            0:prime
            1:prime
            2:prime
            3:prime
            5:prime
            7:prime
            11:prime
            .
            .
            .

        But 0 and 1 are not prime, so we will have to count numbers from 2
    '''

    ans=[]
    for i in range(2,len(prime)):
        if prime[i]:
            ans.append((i))
    return ans




# INPUT 
num=int(input("Input a number to find prime number smaller than it : "))
primeNumArray= SieveOfEratosthenes(num)
print()

print("Prime numbers smaller than "+str(num)+" are : ")
for ele in primeNumArray:
    print(ele)
