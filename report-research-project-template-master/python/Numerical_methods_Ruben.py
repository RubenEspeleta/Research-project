#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:12:40 2023

@author: ruben
"""

import numpy as np
import matplotlib.pyplot as plt
b=2.5                       #width of the channel
g= 9.8                      # gravity
n = 0.029                   # coefficient of roughness of monning
t = 0                      # Analysis started at t=0
tf = 7200               # Time of simulation 
dt = 0.01                  #time interval
dtrec = 3600               #time interval of record
alpha = 0.6                #lax scheme parameter
L=7000                     #channel lenght(m)
N=700                      #Number of nodes along lenght L
I = 0.0003                 #slop of the bottom
h = 0.7                    #height of water downstream
dx = L/(N-1)               # mesh size
t1 = 2880
t2 = 25920
Q1 = 0.2
Q2 = 0.89
#........................................initial condition for h0 and u0...................................................
Q0=0.2                                   #upstream flow m3/s
Qunit=Q0/b                               #unit flow
hn = (((Qunit**2)*(n**2))/I)**0.3        #normal water depth
hc=((Qunit**2)/g)**(1/3)                 #critical water depth

dx = L/(N-1)                             #space step
x = np.linspace(0,L,N)
h_0=np.zeros(N)                          #defining h0
h_0[N-1]=h
for i in reversed(range(N-1)):
    h_0[i]=h_0[i+1]-dx*I*(((1-(hn/h_0[i+1])**(10/3))/(1-(hc/h_0[i+1])**3)))

u_0 = np.zeros(N)                        #defining u0
for i in range(N):
    u_0[i]=Q0/(b*h_0[i])

def flow(t):
    b=Q1
    a = (Q2 - Q1)/t1
    if t<t1:
        Q = a*t+b
    elif t>=t1 and t<=t2:
        Q = Q2
    else:
        Q=Q1
    return Q
H1 = np.zeros(N)
u1 = np.zeros(N)

H1 = np.zeros(N)
u1 = np.zeros(N)
while t<tf:

# UPSTREAM BC
    J=(n**2)*((u_0)**2)/((h_0)**(4/3))
    A1 = (g*dt*J[0])/(u_0[0])
    A2 = np.sqrt(g/(h_0[0]))
    A3 = (2*g*dt*J[0])/(3*(h_0[0]))
    AA1 = np.array([1+A1, -A2-A3 , -1+A1, A2-A3, 0])
    AA2 = np.array([1/(u_0[0]), 1/(h_0[0]), 0, 0, 0])
    AA3 = np.array([0, 0, dx, 0, (u_0[0])-(u_0[1])])
    AA4 = np.array([0, 0, 0, dx, (h_0[0])-(h_0[1])])
    AA5 = np.array([1/2, -(1/4)*A2, 1/2, -(1/4)*A2, 1/dt])
    AUP = np.array([AA1,AA2,AA3,AA4,AA5])  
    
    B1=g*dt*(I-(J[0]/3))
    QN = flow(t)
    QNP1 = flow(t+dt)
    B2=1+(QNP1/QN)
    B3 = (u_0[0])*dx
    B4 = (h_0[0])*dx
    B5 = (1/2)*(np.sqrt(g*(h_0[0])))
    BUP = np.array([B1,B2,B3,B4,B5])
    XUP = np.linalg.solve(AUP, BUP)
    u1[0]=XUP[0]
    H1[0]=XUP[1]
    

    C1 = (g*dt*J[N-1])/(u_0[N-1])
    C2 = np.sqrt(g/(h_0[N-1]))
    C3 = (2*g*dt*J[N-1])/(3*(h_0[N-1]))
    CC1 = np.array([1+C1, -1+C1 , -C2-C3, 0])
    CC2 = np.array([1/2, 1/2, (1/4)*C2, 1/dt])
    CC3 = np.array([0, 0, dx, (h_0[N-2])-(h_0[N-1])])
    CC4 = np.array([0, dx, 0, (u_0[N-2])-(u_0[N-1])])
    Adown = np.array([CC1,CC2,CC3,CC4])  
    
    D1=g*dt*(I-((J[N-1])/3))
    D2 = np.sqrt(g*(h_0[N-1]))
    DD1 = D1-D2
    DD2 = (-3/4)*D2+(L/dt)
    DD3 = (h_0[N-1])*dx +(((h_0[N-2])-(h_0[N-1]))*L)
    DD4 = (u_0[N-1])*dx +(((u_0[N-2])-(u_0[N-1]))*L)
    Bdown = np.array([DD1,DD2,DD3,DD4])
    Xdown = np.linalg.solve(Adown, Bdown)
    u1[len(u1)-1]=Xdown[0]
    H1[len(u1)-1]=h
    
# END UPSTREAM BC    
# LAX
    for i in range(1,N-1):
        U1=((u_0[i-1])-(u_0[i+1]))/(2*dx)
        U2=((u_0[i+1])+(u_0[i-1]))/(2)
        h1=((h_0[i-1])-(h_0[i+1]))/(2*dx)
        h2=((h_0[i+1])+(h_0[i-1]))/(2)

        H1[i]=dt*(((h_0[i])*U1)+((u_0[i])*h1))+(alpha*(h_0[i]))+((1-alpha)*h2)
        u1[i]=(g*dt*(I-J[i]+((u_0[i])*U1/g)+h1))+(alpha*(u_0[i]))+((1-alpha)*U2)
        

    h_0=H1
    u_0=u1
    t+=dt
plt.rc('font', size=30)
plt.figure()
plt.plot(x,u1)
plt.xlabel('Distance (m)')
plt.ylabel('Velocity (m/s)')
plt.show()