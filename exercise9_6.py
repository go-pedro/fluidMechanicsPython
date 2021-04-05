# An oil with p = 900 kg/m' and v = 0.0002 m2/s flows upward through an inclined pipe as shown in Fig. 9-1. Assuming steady laminar flow, (a) verify that the flow is up and find the(b) head loss between section 1 and section 2, (c) flow rate, (d) velocity, and (e) Reynolds number. Is the flow really laminar?
import math as m

#inputs
g=9.81 #m/s2
rho=900 #kg/m3
nu=0.0002 #m2/s
p1=350000 #pressure_1, Pa
p2=250000 #pressure_2, Pa
d=6/100 #diameter, m
L=10 #lenght, m

#calculations
HGL1=0+p1/(rho*9.81)
HGL2 =(10*m.sin(40*m.pi/180))+p2/(rho*9.81)
hf=HGL1-HGL2
mu=rho*nu   #dynamic viscosity
Q=m.pi*rho*g*d**4*hf/(128*mu*L) #volume flow rate
v=Q/(m.pi/4*d**2)  #velocity, m/s
re_num=rho*d*v/mu



#printouts
print('HGL1, m=',HGL1)
print('HGL2, m=', HGL2)
print('---')
print(f'answer a) --> the flow is upwards; HGL2>HGL1, {HGL1}>{HGL2}')
print('---')
print('answer b) --> head losses, m =', hf)
print('dynamic viscosity, Pa.s =', mu)
print('volume flow rate in m3/h=',Q)
print('velocity, m/s=',v)
print('reynolds number=', re_num)
print('answer c) --> the flow is laminar!')



