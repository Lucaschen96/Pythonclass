import math
from scipy import integrate
pi=math.pi
T=0

for i in range(1,50,1):
    a=(270-45)/i
    b=(270-0.01)/i
    def f(x):
        return math.exp(-i*(x-10)**2/(2*85))
    v,err=integrate.quad(f,a,b)
    E=(1/math.sqrt(2*pi*85/i))*v
    T += E
K=T/51
print(K)

