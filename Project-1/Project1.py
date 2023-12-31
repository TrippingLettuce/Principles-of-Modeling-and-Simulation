#pip imports README.md
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def network_bandwidth(y, t, rate):
    return rate - y

print("Please indicate the rate of change of network bandwidth: ")
rate = int(input()) # rate of change of network bandwidth

t = np.linspace(0, 60, 100) # time points for the solution

y0 = 0

# solving the ODE using odeint
sol = odeint(network_bandwidth, y0, t, args=(rate,))

# print the solution
print(sol)


# % matplotlib inline
plt.rcParams.update({'font.size': 14})  
plt.title('Rate of Network Bandwidth vs Data Transmitted')
plt.xlabel('Time (s)')
plt.ylabel('Rate of data transmitted')
plt.plot(t, sol)
plt.show()