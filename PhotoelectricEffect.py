# -*- coding: utf-8 -*-
"""lab 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xac7g4SIWdBduBq2dvNzBGgENqEmVigw
"""

import numpy as np

import matplotlib.pyplot as plt

xdata=[((1/4)-(1/(3**2))),((1/4)-(1/(4**2))),((1/4)-(1/(5**2)))]

ydata=[(1/655.56),(1/484.21),(1/434.25)]

plt.scatter(xdata,ydata,color='red')
plt.title('Figure 2: linear regression for experimental rydberg constant')
best_fit_model = np.polyfit(xdata, ydata, 1)
print(best_fit_model)
x = np.linspace(0.10, 0.25)
y = (1.09598849e-02* x) + 4.89783118e-06
plt.plot(x,y, '-g')

## Frequency data
x_frequency = [491,594,635,571,510]

## Stopping Voltage Data
y_voltage = [0.089,0.5157,0.6477,0.4673,0.1359]
y_critical_energy = [1.6021e-19*0.089,1.6021e-19*0.5157,1.6021e-19*0.6477,1.6021e-19*0.4673,1.6021e-19*0.1359]

plt.scatter(x_frequency, y_critical_energy, color = "red")

plt.title('Critical Energy versus Frequency of Light')
plt.xlabel('Frequency in Terahertz')
plt.ylabel('Critical Energy in eV')

best_fit_model = np.polyfit(x_frequency, y_critical_energy, 1)

plt.scatter(x_frequency, y_critical_energy, color = "red")

plt.title('Critical Energy over Frequency of Light')
plt.xlabel('Frequency in Terahertz')
plt.ylabel('Critical Energy in eV')

print(best_fit_model)

x = np.linspace(480, 640)
y = (6.55469620e-22* x) - 3.07736946e-19
plt.plot(x,y, '-g')

best_fit_model = np.polyfit(x_frequency, y_voltage, 1)

plt.scatter(x_frequency, y_voltage, color = "red")

plt.title('Critical Energy over Frequency of Light')
plt.xlabel('Frequency in Terahertz')
plt.ylabel('Critical Energy in eV')

print(best_fit_model)

x = np.linspace(480, 640)
y = (0.00409132* x) -1.92083482
plt.plot(x,y, '-g')

x_intensity = [20,40,60,80,100]
y_critical_voltage=[0.501,0.507,0.512,0.515,0.518]

best_fit_model2 = np.polyfit(x_intensity,y_critical_voltage,1)
plt.scatter(x_intensity,y_critical_voltage, color='blue')
plt.title("Critical Voltage over Light Intensity at a wavelength of 505nm")
plt.xlabel('Intensity %')
plt.ylabel('Critical Voltage in Volts')
print(best_fit_model2)

yfit=[4.98e-01+2.10e-04*xi for xi in x_intensity]
plt.plot(x_intensity, yfit)
plt.ylim([0.3,0.7])

##x1 = np.linspace(0, 100)
##plt.plot(x1, 2.10e-04*x1+4.98e-01)

##x1 = np.linspace(0, 100)
##y1 = (2.10e-04* x1) + 4.98e-01
##y1=np.linspace(0.3,0.7)
##plt.plot(x1,y1)

mult=2/(7.8e-4**2)
ydata=[183.1*mult,135.9*mult,101.2*mult,73.1*mult]
xdata=[5.1**2,4.35**2,3.95**2,3.3**2]

plt.scatter(xdata,ydata,color='red')
best_fit=np.polyfit(xdata,ydata,1)
print(best_fit)

fit=[-30636447.68311315+24419689.14215393*xi for xi in xdata]
plt.plot(xdata,fit)
