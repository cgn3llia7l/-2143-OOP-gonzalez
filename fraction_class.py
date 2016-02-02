class Fraction:

    def __init__(self,numerator,denominator):

        self.num = numerator
        self.den = denominator
        
    def __str__(self):
        return "%s / %s" % (self.numerator , self.denominator)
        
    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d
        
    def _mul_(self,rhs):
       x1 = (self.num * rhs.den)+(rhs.num*self.den)
       y = self.den * rhs.den
       i=0
       if x1 < y:
           x=x1
           return fraction(x,y)
       if x1 == y:
           x=1
           y=1
           return fraction(x,y)
       else:
           x2=x1-y
           
           if x2 < y:
               x=x2
               i+=1
               print (i)
               return fraction(x,y)
           else:
               x=x2-y
               i+=1
               print(i)
               return fraction(x,y)
       
if __name__ == '__main__':
    a = fraction(1,2)
    b = fraction(4,5)
    c = a * b
    print(c)
