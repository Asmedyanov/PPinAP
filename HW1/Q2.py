from numpy import pi, arccos, sqrt, exp,arcsin

T = 6e3  # K
F_nu = 3.6e-20  # erg*s^-1*cm^-2*Hz^-1
Lambda = 5.5e3 * 1.0e-10 * 1.0e2  # cm
c = 3e10  # cm/s
nu = c / Lambda
h = 6.6e-27  # cm^2*g*s^-1
k = 1.38e-16  # cm2 g s-2 K-1
I_nu = (8.0 * pi * h / c ** 3) * nu ** 3 / (exp(h * nu / (k * T)) - 1)
cos_f = F_nu / (2.0 * pi * I_nu)
teta = 2.0 * arcsin(sqrt(cos_f))
print(f'Teta = {teta} rad')
print(f'Teta = {teta*180.0/pi} grad')
print(f'Teta = {teta*180.0/pi*60} min')
