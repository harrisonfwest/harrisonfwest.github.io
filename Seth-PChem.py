import matplotlib.pyplot as plt
import numpy as np

n = 2.5 # mol

R = 8.31446261815324 # J K^-1 mol^-1
a = 0.034598 # L^2 bar mol^-2
b = 0.023733 # L mol^-1

def pressure(V: float, T: float):
    return n * R * T / (V - n * b) - n**2 * a / V**2

# vol_ranges = np.linspace(2, 0.5, 1000)

# plt.figure(figsize=(10, 8))
# for temp in np.arange(200, 400, 10):
#     plt.plot(vol_ranges, pressure(vol_ranges, temp))
# plt.gca().invert_xaxis()
# plt.xlabel('Volume (L)')
# plt.ylabel('Pressure (bar)')
# plt.show()

import scipy.optimize as spo

n = 1 # mol

V_range = [2.3891, 1.1361, 0.71355, 0.49741, 0.36195]
p_range = [20, 40, 60, 80, 100]

def new_pressure(V, a, b):
    return n * R * 600 / (V - n * b) - n**2 * a / V**2

fit = spo.curve_fit(new_pressure, V_range, p_range, p0=[0.034598, 0.023733])
fit_params = fit[0]
print(fit_params)

v_range = np.linspace(2.5, 0.3, 1000)
plt.plot(v_range, new_pressure(v_range, *fit_params))
plt.scatter(V_range, p_range)
plt.gca().invert_xaxis()
plt.show()