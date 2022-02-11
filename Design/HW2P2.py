#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:41:50 2022

@author: brunobiazetto
"""

#Problem 2 
import numpy as np

# Given data:
components = ["propylene", "trans-2-butene", "cis-2-butene", "1-butene", "ethylene", "propane"]
f = np.array([45, 10, 15, 6, 5, 4])  # in mol/s
A = np.array([15.7027,15.8177,15.8171,15.7564,15.5368,15.7260])
B = np.array([1807.53,2212.32,2210.71,2132.42,1347.01,1872.46])
C = np.array([-26.15,-33.15,-36.15,-33.15,-18.15,-25.16])
NC = len(components)  # number of components

# Create variables.
P0 = np.zeros(NC)        # vapor pressures (in mmHg)
alpha_LK = np.zeros(NC)  # relative volatilities w.r.t. to the light key component
alpha_HK = np.zeros(NC)  # relative volatilities w.r.t. to the heavy key component
xi = np.zeros(NC)        # split fractions
d = np.zeros(NC)         # distillate flowrates (in kmol/hr)
b = np.zeros(NC)         # bottoms flowrates (in kmol/hr)
x_D = np.zeros(NC)       # distillate mole fractions
x_B = np.zeros(NC)       # bottoms mole fractions

LK = 0 #propylene
HK = 1 #trans-2-butene
xi[LK] = 0.995 #recover 99.5% of propylene in distillate
xi[HK] = 1 - 0.99 #recover 99% of trans-2-butene in distillate

print ("a:")
#since the feed is saturated liquid, the feed temperature is equivalent to the bubble point temperature 
P = 15 #in bar, Feed pressure
PFmmhg = P*750.062 #in mmhg
T = 100 #in K, T guess
n=0 #specifying desired component (propylene)
error = 1 #initializing the error 
#iteration over different T in order to get the correct one
x = f/sum(f)
while P <= PFmmhg:
    # Compute vapor pressures using the Antoine equation.
    P0 = np.exp(A - B/(T+C)) #using antoines equation to find the vapor pressures 
    PP = (f/sum(f))*P0 #applying feed parameters to get partial pressure 
    P = sum(PP) #summing the partial pressures 
    T += 0.01 # increase T for the next loop
print ("The Feed Temperature is:", T, "K" )

#Calculate vapor pressures and relative volatilities.
P0 = np.exp(A - B/(T+C))
alpha_LK = P0/P0[LK]
alpha_HK = P0/P0[HK]

# Compute minimum number of trays.
Nmin = np.log(xi[LK]*(1-xi[HK])/(1-xi[LK])/xi[HK]) / np.log(alpha_HK[LK])
print ("The minimal number of plates is:", Nmin, "K")

#--------------------------------------------------------------------------
#b 
print ("b:")
alpha = P0/P0[HK] #computing volatilities based on HK vapor pressure
xi = alpha**Nmin*xi[HK]/(1+(alpha**Nmin-1)*xi[HK]) #calculating the recoveries
x_D = xi*f #multiplying the recoveries times the feed compoition to get distillate fractions
x_B = (1-xi)*f #calculating bottoms fractions based on the distillate recoveries 
d = x_D/sum(x_D) #distillate composition 
b= x_B/sum(x_B) #bottoms composition 

print("The distillate composition is:", d)
print("The bottoms composition is:", b)

#--------------------------------------------------------------------------
#c 
print ("c:")
deltaT_min = 10 #in K 
T_cold = 305.372 #in K, cooling water temp
TBC = deltaT_min + T_cold # Bubble temperature of the condenser is dentaT + the cooling water temperature 

n=0 #specifying the most abundant component in the distillate stream 
#Calculate vapor pressures and relative volatilities.
P0 = np.exp(A-B/(TBC+C)) 
alpha = P0/P0[n]
alpha_avg_L = sum(alpha*d)

#calculating the pressure of the saturated liquid based on the average volatility of the liquid stream
PDL = P0[n]*alpha_avg_L
print("pressures")
print("Saturated Liquid Pressure:", PDL, "mmHg")

#calculating the pressure of the saturated vapor based on the average volatility of the vapor stream
alpha_avg_V = sum(d/alpha)
PDV = P0[n]/alpha_avg_V
print("Saturated Vapor Pressure:", PDV, "mmHg")

#Calculating Temperatures 
n=2 #specifying the most abundant component in the bottom stream 
alpha = P0/P0[n] #computing volatility of distillate stream
alpha_avg_B = sum(b/alpha) #calculating average alpha in bottom stream based on bottoms composition and alpha from above 
#computing pressure and temperature based on the pressure calculated, bottoms volatility and antoine law
P1 = PDL*alpha_avg_B
T1 = B[n]/(A[n]-np.log(P1)) - C[n]
print("max temperature for higher pressure:", T1, "K")

#computing pressure and temperature based on the pressure calculated, bottoms volatility and antoine law
P2 = PDV*alpha_avg_B
T2 = B[n]/(A[n]-np.log(P2)) - C[n]
print("max temperature for higher pressure:", T2, "K")






