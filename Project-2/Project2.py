import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

y0 = 1  # initial values
x0 = 2
h = 0.3  # step

t = np.linspace(0, 5, 1000)

def ode(xn, yn):  # differential equation
    f = -yn + np.log(xn)
    return f

y = []
x = []

def rungeKuttaT4(yn, xn, h, n):  # 4th degree runge-kutta method
    for i in range(xn, n):
        k1 = ode(xn, yn)
        k2 = ode(xn + h/2, yn + (h/2) * (k1))
        k3 = ode(xn + h/2, yn + (h/2) * (k2))
        k4 = ode(xn + h, yn + (h) * (k3))

        t4 = (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        yn = yn + (h * t4)
        xn = xn + h
        y.append(yn)
        x.append(xn)

rungeKuttaT4(y0, x0, h, 1000)

# Define the ODE for odeint
def model(y, x):
    return -y + np.log(x)

# Solve ODE using odeint
y_odeint = odeint(model, y0, x)

# Create a figure and axis
fig, ax = plt.subplots()

# Plotting the data
ax.plot(x, y, label='runge-kutta', color='blue')
ax.plot(x, y_odeint, label='odeint', color='red', linestyle='--')

# Setting labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('1000 points comparison of runge-kutta and ode for -y=lnx')
ax.legend()

# Display the plot
plt.show()
