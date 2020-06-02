import matplotlib.pyplot as plot
import numpy as np
import math
import cmath
import sympy as sym
 
 
plot.scatter([0,-25,-50,-50], [0,0,10,-10], label= "p", color= "blue", marker= "X", s=100)
angle1 = ((2*0+1)/4)*180
angle2 = ((2*1+1)/4)*180
ca = (-25-50-50)/4
x = np.linspace(-70,70,1000)
asym1 = x
asym2 = -x
plot.plot(x+ca, asym1, color='blue', linestyle='dashed', linewidth = 2)
plot.plot(x+ca, asym2, color='blue', linestyle='dashed', linewidth = 2)
 
s = sym.symbols('s')
function = s**4+125*s**3+5100*s**2+65000*s
diff_f = function.diff(s)
na = sym.Poly(diff_f,s)
solu = np.roots(na.all_coeffs())
plot.scatter(solu[2], 0, color= 'r', marker= ".", s=150)
 
k = sym.symbols('k')
tmp = (4580*65000-125*k)/4580
solu1 = sym.solve(tmp)
a = 4580*s**2+solu1[0]
nh = sym.Poly(a,s)
i = np.roots(nh.all_coeffs())
plot.scatter([0,0], [i[0].imag,i[1].imag], color= 'r', marker= ".", s=100)
 
DAngle = 180 - (180-math.degrees(math.atan(10/50)) + 90 + (180-math.degrees(math.atan(10/25))))
 
for k in np.linspace(0,100000000,1000):
  a = sym.Poly(function+k, s)
  solu = np.roots(a.all_coeffs())
  for x in range(len(solu)):
      plot.scatter([solu[x].real], [solu[x].imag], color= "red",  
            marker= "o", s=10)
 
plot.axes().spines['left'].set_position(('data',0))
plot.axes().spines['bottom'].set_position(('data',0))
plot.show()
