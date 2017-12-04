import numpy as np
import matplotlib.pyplot as plt

calculated = np.loadtxt("rp082209.tot", skiprows=5, usecols=(0,1))
experimental = np.loadtxt("Expdata208ng.txt", skiprows=1, usecols=(0,1,2))

plt.plot(calculated[:,0],np.log(calculated[:,1]),label="TALYS")
plt.errorbar(experimental[:,0],np.log(experimental[:,1]),yerr=experimental[:,2],fmt='ro', label="Bergqvist et.al.")
plt.xlabel("Energy in MeV")
plt.ylabel("cross section in mb")
plt.legend()
plt.xlim(-1,20)
plt.show()



