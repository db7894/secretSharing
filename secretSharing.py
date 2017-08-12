#Secret Sharing w/ Lagrange Polynomials!

def distributeSecret():
    """
    asks the user for the number n of trustees and the number k of trustees 
    who should be able to recreate the secret (you may assume that k < n). 
    It then constructs a random polynomial of degree k-1 (all the random 
    coefficients on that polynomial are between 1 and 1000) and chooses 
    and prints n lists of the form [x, y], one for each trustee. 
    Each of these points should have a unique x value and should be on the 
    randomly chosen polynomial. Finally, the function prints the secret - 
    the y-intercept of the secret polynomial - for internal use by the bank.
    """

    #Get values of k and n, assume that k < n
    n = input("How many trustees are there?")
    k = input("How many should be able to reconstruct the secret?")

def verify(pointList, secret):
    """
    takes as input a list of exactly k points pointList (for example it might be [ [1, 2], [3, 5], [6, 8]] 
    if k is 3) and the numerical secret (the y-intercept of the secret polynomial) and returns the Boolean 
    True if the Lagrange polynomial reconstructed from the k points in pointList has y-intercept equal to 
    secret and False otherwise.
    """
    pass