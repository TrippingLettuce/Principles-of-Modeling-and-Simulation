import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time

y0 = 1  # initial values
x0 = 2
h = 0.3  # step

t = np.linspace(0, 5, 1000)

def ode(xn, yn):  # differential equation
    f = -yn + np.log(xn)
    return f

y = []
x = []

rkComputationalSteps = 0

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
        global rkComputationalSteps
        rkComputationalSteps = rkComputationalSteps+6

# Define the ODE for odeint
def model(y, x):
    return -y + np.log(x)

# Start measuring time for Runge-Kutta
start_time_rk = time.time()

# Run the Runge-Kutta method
rungeKuttaT4(y0, x0, h, 1000)

# End measuring time for Runge-Kutta
end_time_rk = time.time()

# Compute the elapsed time for Runge-Kutta
elapsed_time_rk = end_time_rk - start_time_rk

# Start measuring time for odeint
start_time_odeint = time.time()

# Solve ODE using odeint
y_odeint = odeint(model, y0, x)

# End measuring time for odeint
end_time_odeint = time.time()

# Compute the elapsed time for odeint
elapsed_time_odeint = end_time_odeint - start_time_odeint

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

# Display computation times on the plot
time_text_rk = f"Time for rungeKuttaT4: {elapsed_time_rk:.4f} seconds"
time_text_odeint = f"Time for odeint: {elapsed_time_odeint:.4f} seconds"
ax.text(0.05, 0.95, time_text_rk, transform=ax.transAxes, verticalalignment='top', color='blue')
ax.text(0.05, 0.90, time_text_odeint, transform=ax.transAxes, verticalalignment='top', color='red')


# Display the plot
plt.show()

print(f"Runge-Kutta, number of computational steps: {rkComputationalSteps}")