#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:37:17 2022

@author: brunobiazetto
"""

#Problem 1 
import numpy as np
#a
print ("a:")
# Given data:
components = ["n-pentane", "cis-2-butane", "n-butane"]
f = np.array([25, 40, 35])  # in mol/s
#antoine parameters
A = np.array([15.8333, 15.8171, 15.6782]) #in bar, K
B = np.array([2477.07, 2210.71, 2154.90]) #in bar, K
C = np.array([-39.94, -36.15, -34.42]) #in bar, K
#getting the number of system components 
NC = len(components)  
#setting the pressure 
PF = 200 # in kPa
PFmmhg = PF*7.500062 # in mmhg, pressure was converted to mmHg
n=1

# Create the variables.
PP = np.zeros(NC)     #partial pressures
P0 = np.zeros(NC)     # vapor pressures (in mmHg)
alpha = np.zeros(NC)  # relative volatilities w.r.t. to the key component
K = np.zeros(NC)      # K values
xi = np.zeros(NC)     # split fractions
v = np.zeros(NC)      # vapor molar flowrates (in kmol/hr)
l = np.zeros(NC)      # liquid molar flowrates (in kmol/hr)
y = np.zeros(NC)      # vapor mole fractions
x = np.zeros(NC)      # liquid mole fractions

#Finding Bubble Point
T = 150 # T guess in Kelvin, used to find the actual Bubble point T
P=0
#iteration over different T in order to get the correct one
while P <= PFmmhg:
    # Compute vapor pressures using the Antoine equation.
    P0 = np.exp(A - B/(T+C)) #using antoines equation to find the vapor pressures 
    PP = (f/100)*P0 #applying feed parameters to get partial pressure 
    P = sum(PP) #summing the partial pressures 
    T += 0.01 # increase T for the next loop
    
print("The Bubble Point Temperature is:", T, "K")


#Finding Dew Point 
# Compute vapor pressures using the Antoine equation and the temperature found for the bubble point 
P0 = np.exp(A-B/(T+C))
K = P0/PFmmhg #Finding K values for all components based on vapor pressures 
alpha = K/K[n] #Finding alpha based on the K value
x=f/100
alpha_avg = sum(x/alpha) #Getting the solution average alpha
P = PFmmhg*alpha_avg #calculating the dew point pressure
T = B[n]/(A[n]-np.log(P))-C[n] #using the pressure previously found to get the dew point temperature
print ("The Dew Point Temperature is:", T, "K")

#-------------------------------------------------------------------
#B:
print ("b:")
#B Will never converge, the liquid temperature is below both the dew and bubble point, therefore it will never flash and nothing can be recovered 
print("Will never converge, the liquid temperature is below both the dew and bubble point, therefore it will never flash and nothing can be recovered")
#--------------------------------------------------------------------
#c
print ("c:")
PF = 100 # in kPa, Feed pressure
PFmmhg = PF*7.500062 # in mmhg
phi = 0.6 #recovery specified 
T = 150 # T guess in Kelvin for the recovery
n=1 #specifying desired component (cis-2-butane)
error = 1 #initializing the error 
#iteration over different T in order to get the correct one
while error >= 0.01:
    # Compute vapor pressures using the Antoine equation.
    P0 = np.exp(A - B/(T+C))
    alpha = P0/P0[n] #computing alpha for each component 
    xi = (phi*alpha)/(1+phi*(alpha-1))
    # Solve mass balance and calculate mole fractions.
    l = (1-xi)*f #liquid composition
    x = l/sum(l) #liquid fraction composition 
    alpha_avg = sum(x*alpha) #calculating the alpha average
    k=0 #specifying the most abundant element 
    P0_comp = PFmmhg*alpha[k]/alpha_avg #computing the pressure based on the most abundant element
    T_comp = B[k]/(A[k]-np.log(P0_comp)) - C[k] #finding T based on the pressure found above
    error = abs(T_comp-T) #calculating the error 
    T += 0.01 # increase T for the next loop
    
print ("The Operation Temperature is:", T, "K")
   
