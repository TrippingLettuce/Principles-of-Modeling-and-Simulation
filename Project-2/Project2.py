
y0=1 #initial values
x0=1 
h=0.1 # step


def ode(yn,xn): #differential equation
    f = xn+yn
    return f

def rungeKuttaT4(yn,xn,h,n): #4th degree runge-kutta method
    if (n == 0): return
    k1=ode(xn,yn)
    k2=ode(xn+h/2,yn+(h/2)*(k1))
    k3=ode(xn+h/2,yn+(h/2)*(k2))
    k4=ode(xn+h,yn+(h)*(k3))

    t4 = (1/6)*(k1+2*k2+2*k3+k4)
    yn=yn+(h*t4)
    print(yn)
    rungeKuttaT4(yn,xn+h,h,n-1)


rungeKuttaT4(y0,x0,h,5)