#Daniel Bashir
#CS5 Black
#hw8pr4
#Secret sharing with the Lagrange Polynomial method


from random import randint

def create_random_poly(degree,yint):
    """
    Inputs: degree of a polynomial, y intercept
    Output: The polynomial with random coefficients
    """
    polynomial = ""
    for i in range(1,degree+1):
        coeff = randint(1,1000)
        polynomial += (str(coeff) + '*' + 'x**' + str(degree-(i-1)) + '+' )
    polynomial += str(yint)
    return polynomial

def eval_poly(poly,x):
    """
    Inputs: polynomial returned by create_random_poly
    Output: value at which we evaluate polynomial
    """
    return eval(poly.replace('x',str(x)))

def distributeSecret(n, k, secret):
    """
    Inputs: number of points function returns, k = number of points to return the secret, and secret is the secret
    Output: a list of n lists, each of which is a point
    """
    points = []
    secretPoly = create_random_poly(k-1,secret)
    print(secretPoly)
    for i in range(n):
        xVal = randint(1,1000)
        points.append([xVal,eval_poly(secretPoly,xVal)])
    return points

def eval_pointspoly(points, x):
    """
    Inputs: points like those from distribute secret and an x value to find a polynomial
    Output: evaluated polynomial at point x
    """
    evaluatedPoly = 0
    print(len(points))
    
    for i in range(len(points)):
        prePoly = 1
        for j in range(len(points)):
            if points[i][0] != points[j][0]:
                part = (x-points[j][0])/(points[i][0]-points[j][0])
                prePoly *= part
        evaluatedPoly += prePoly*points[i][1]
        print(evaluatedPoly)
    return eval_poly(str(evaluatedPoly),x)
