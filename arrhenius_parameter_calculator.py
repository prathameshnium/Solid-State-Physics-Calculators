#Activation energy calculator
# -----------------------------------------------------------------------------
# Description:
#   Calculates activation energy (Ea) and the pre-exponential factor (f0)
#   from the slope and y-intercept of a linearized Arrhenius plot.
#
#   This script assumes the plot is in the form of ln(rate) vs. 1000/T,
#   where 'a' is the slope and 'b' is the y-intercept.
#
# Equations:
#   Ea = -a * 1000 * k_B  (in eV)
#   f0 = exp(b)          (in Hz)
# -----------------------------------------------------------------------------
a=-1089.607 #slope
b=22.6918 #intersect
K=8.617333262*1E-5 #boltzman constant in eV units
e=2.718281828459045
E=-a*K*1000

f0= pow(e,b) #in Hz
print("value of activation energy in eV : "+"{:e}".format(E))
print("activation energy E  in eV:"+str(E))

print("value of f0 in Hz : "+"{:e}".format(f0)) 
print("value of f0 in Mhz : "+"{:e}".format(f0/1E6)) 
