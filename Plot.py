import numpy as np
import matplotlib.pyplot as plt


print("Enter a function");
print("1. Sin");
print("2. Cos");

a = input(">>");

x = np.linspace(-np.pi,np.pi,4);

if a == 1: 
	y = np.sin(x);
else:
	y = np.cos(x);

plt.plot(x,y);

plt.show();
