#VRH fitting
a=-262.46648 #slope
b=81.34011 #intersect
K=8.617333262*1E-5 #boltzman constant in eV units
e=2.718281828459045
T0=pow(-a,4)


f0= pow(e,b)
print("value of T0 : "+"{:e}".format(T0))
print("value of f0 : "+"{:e}".format(f0))
