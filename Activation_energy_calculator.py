#Activation energy calculator
#arrhenius fitting
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
