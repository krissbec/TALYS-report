import numpy as np
import matplotlib.pyplot as plt

DefaultEnergy = np.loadtxt("defaultenergy209.tot", skiprows=5, usecols=(0,1))
MinusEnergy = np.loadtxt("minus1_7MeV209.tot", skiprows=5, usecols=(0,1))
#HF = np.loadtxt("hf209.tot", skiprows=5, usecols=(0,1))
#experimental = np.loadtxt("Expdata208ng.txt", skiprows=1, usecols=(0,1,2))

plt.plot(DefaultEnergy[:,0],np.log(DefaultEnergy[:,1]),label="DEfault energy")
plt.plot(MinusEnergy[:,0],np.log(MinusEnergy[:,1]),label="Minus 1.7MeV Energy")
#plt.plot(HF[:,0],np.log(HF[:,1]),label="HF")

#plt.errorbar(experimental[:,0],np.log(experimental[:,1]),yerr=experimental[:,2],fmt='ro', label="Bergqvist et.al.")
plt.xlabel("Energy in MeV")
plt.ylabel("cross section in mb")
plt.legend()
plt.xlim(-1,20)
plt.show()