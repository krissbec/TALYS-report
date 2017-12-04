import numpy as np
import matplotlib.pyplot as plt

Os187calc= np.loadtxt("rp076188.tot", skiprows=5, usecols=(0,1))
experimental = np.loadtxt("187OsEXP.tot", skiprows=3, usecols=(0,3,4))
#HF = np.loadtxt("hf209.tot", skiprows=5, usecols=(0,1))
#experimental = np.loadtxt("Expdata208ng.txt", skiprows=1, usecols=(0,1,2))

plt.plot(Os187calc[:,0],np.log(Os187calc[:,1]),label="TALYS")
#plt.plot(BSFG[:,0],np.log(BSFG[:,1]),label="BSFG")
#plt.plot(HF[:,0],np.log(HF[:,1]),label="HF")

plt.errorbar(experimental[:,0],np.log(experimental[:,1]),yerr=experimental[:,2],fmt='ro', label="Segawa et.al.")
plt.xlabel("Energy in MeV")
plt.ylabel("cross section in mb")
plt.legend()
plt.xlim(-1,20)
plt.show()