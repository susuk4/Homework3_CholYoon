def isPrime(testNumber):
    for prime in [2,3,5,7,11]:
        if testNumber%prime==0:
            return False
    else:
        return True

def factor_int(n):
    n = n
    lastnumber = str(n)
    remainder = n
    returnStr = ""
    #exception handler
    if n==0:
        raise ValueError, "0 cannot be factored"
    elif isPrime(n):
        raise ValueError, str(n)+" is already a prime number"
    denominator = [2,3,5,7,11]
    for de in denominator:
        while remainder%de==0:
            remainder = remainder/de
            lastnumber = str(remainder)
            returnStr = returnStr + str(de)
            if remainder != de and remainder != 1 and remainder != -1:
                returnStr = returnStr+"*"
            else:
                break
    if remainder != 1 and remainder != -1:
        returnStr = returnStr+str(remainder)
    elif remainder == -1:
        returnStr = "-1*"+returnStr
    return returnStr

#625 loops, best of 3: 48.5 µs per loop
