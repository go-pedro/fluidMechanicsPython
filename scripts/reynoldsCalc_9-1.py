# Water at 10°C flows in a 150-mm-diameter pipe at a velocity of 5.5 m/s. Is this flow laminar or turbulent? 
from thermo import Chemical

#inputs var
t_water=10+273.15 #temp water in K
d=150/1000 #diameter, m
v=5.5 #velocity,m/s

#get properties
water=Chemical('water', T=t_water, P=1E5)
rho_water=water.rho #density
print('water density',rho_water)
mu_water=water.mu #viscosity dynamic
print('water dynamic viscosity', mu_water)

# print(mu_water/rho_water)
n_reynolds=rho_water*v*d/mu_water
print('renolds number=',n_reynolds)

if n_reynolds >4000:
	print('the flow is turbulent...')
else:
	print('the flow is laminar...')