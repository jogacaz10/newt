import sympy as sp
import math
def ne(ni,a,b,err,fx,x):

    der_exp=sp.diff(fx,x)
    der_exp2=sp.diff(der_exp,x)

    exp_f=sp.lambdify(x,fx)
    der_f=sp.lambdify(x,der_exp)
    der_f2=sp.lambdify(x,der_exp2)

    w=0
    i=0
    xi=(a+b)/2
    
    if (abs(exp_f(xi)*der_f2(xi))/(der_f(xi))**2)<1:
        print ("converge")
    while True :

        print('|',i,'|',xi,'|',abs(xi-(exp_f(xi))/der_f(xi)),'|',w,'|') 

        xi=float(abs(xi-(exp_f(xi))/der_f(xi)))
        w2=w
        w=float(abs((abs(xi-(exp_f(xi))/der_f(xi))-xi)/abs(xi-(exp_f(xi))/der_f(xi))))
        
        if i==ni or w<=err:
            break
        i=i+1
    return xi,w2
    
if __name__ == "__main__":
    x=sp.symbols('x')
    fx= math.e**x-3*x**2
    res=0.02
    Ni=100
    a=0
    b=1 
    result=ne(Ni,a,b,res,fx,x)
