import math
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 8})
plt.rcParams['axes.facecolor'] = 'w'
plt.rcParams['savefig.facecolor'] = 'w'
import numpy as np

def newNumber():
    z = complex(input("Complex Number (x+yj): "))
    return z

def propiedades(z):
    rz = z.real
    iz = z.imag
    phase = math.atan(iz/rz)
    modulus = math.sqrt((math.pow(rz, 2))+(math.pow(iz, 2)))
    print(f"Real part: {rz}")
    print(f"Imaginary part: {iz}")
    print(f"Modulus: {modulus}")
    print(f"\u03B8: {phase}")

    if rz > iz:
        limit = abs(rz)+1
    else:
        limit = abs(iz)+1
    ax = plt.subplot(1,2,1)
    plt.suptitle(z)
    plt.plot(rz, iz, 'b.')
    plt.plot(0, 0, 'r+')
    plt.grid(color='m', linestyle='dotted', linewidth=0.5)
    plt.xlabel("Real Part")
    plt.xlim(-limit,limit)
    plt.ylabel("Imaginary Part")
    plt.ylim(-limit,limit)
    ax.set_aspect('equal', adjustable='box')
    ax = plt.subplot(1,2,2,projection = 'polar')
    plt.polar(phase, modulus, 'b.')
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    z=newNumber()
    propiedades(z)