import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < 50:
        z = z*z + c
        n += 1
    return n

x = np.linspace(-2, 1, 1000)
y = np.linspace(-1.5, 1.5, 1000)

X, Y = np.meshgrid(x, y)
C = X + 1j*Y

Z = np.array([mandelbrot(c) for c in C.flat]).reshape(C.shape)

plt.imshow(Z, cmap='hot', extent=[-2, 1, -1.5, 1.5])
plt.show()
