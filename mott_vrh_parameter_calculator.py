#VRH fitting

# -----------------------------------------------------------------------------
# Description:
#   Calculates the characteristic temperature (T0) and the pre-exponential
#   factor (often σ₀) for the 3D Mott Variable Range Hopping (VRH) model.
#
#   This script uses the slope ('a') and y-intercept ('b') from a linear
#   fit of experimental data plotted as ln(conductivity) vs. T^(-1/4).
#
# Equations:
#   Slope (a) = -(T0)^(1/4)   =>   T0 = (-a)^4
#   Intercept (b) = ln(σ₀)     =>   σ₀ = exp(b)
# -----------------------------------------------------------------------------

a=-262.46648 #slope
b=81.34011 #intersect
K=8.617333262*1E-5 #boltzman constant in eV units
e=2.718281828459045
T0=pow(-a,4)


f0= pow(e,b)
print("value of T0 : "+"{:e}".format(T0))
print("value of f0 : "+"{:e}".format(f0))
