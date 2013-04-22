%cython
from cpython cimport bool

class FactorInt:
    def __Init__(self, integer):
        #initialize class with initial string, and denominator and check if it is integer
        if type(integer) == int:
            self.n = integer
            if not isAlreadyPrime():
                self.denominator = [7,5,3,2]
                self.string = ""
                if isNegativeCython(self.n):
                    self.negative = True
                    self.n = -1 * self.n
                self.lastnumber = str(self.n) 
            elif self.n==0:
                raise ValueError, "0 cannot be factored"
            else: #print if given vallue is already a prime number
                raise ValueError, str(self.n)+" is already a prime number"
        else: #raise ValueError if it is not an integer
            raise ValueError, "Arguement is not an integer"
    
    #check if the number is divisible by specific number
    def isDivisible(int numtor, int denumtor):
        cdef bool div = numtor%denumtor==0
        return div
    
    #check if the number is divisible by any number
    def isDivisible(int numtor2):
        return isAlreadyPrime(numtor2)
        
    #if check if integer is already prime number
    def isAlreadyPrime(int numtor3):
        cdef int n = numtor3
        for prime in [2,3,5,7,9,11]:
            if isDivisible(n, prime):
                return False
        return True
    
    #check to see if input is negative
    def isNegative(self,g2):
        return g2<0
    
    #cythonization of it input is negative
    def isNegtaiveCython(int g2):
        cdef bool tof = g2<0
        return tof
        
    #looping through 2,3,5,7 which are prime numbers between 1 - 10 except 1
    #and return resulted string
    def toString(self):
        for de in self.denominator:
            #every new loop start while loop until input number is not divisible by new loop number
            #and add divisible string at the front.
            while isDivisible(de):
                self.lastnumber = self.lastnumber / de
                self.string = str(de)+"*"+self.string(self.lastnumber)
        if self.negative: #if negative add negative value
            self.string = str(-1)+"*"+self.string
        return str(self.n)+": "+self.string
