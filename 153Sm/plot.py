import numpy as np
import matplotlib.pyplot as plt

Sm153calc= np.loadtxt("rp062154.tot", skiprows=5, usecols=(0,1))
JEFF32= np.loadtxt("JEFFcs153.tot", skiprows=11, usecols=(0,1))
#experimental = np.loadtxt("187OsEXP.tot", skiprows=13, usecols=(0,2,3))
#HF = np.loadtxt("hf209.tot", skiprows=5, usecols=(0,1))
#experimental = np.loadtxt("Expdata208ng.txt", skiprows=1, usecols=(0,1,2))

plt.loglog(Sm153calc[:,0],Sm153calc[:,1],label="TALYS")
plt.loglog(JEFF32[:,0],JEFF32[:,1]*1e3,label="JEFF-3.2")
#plt.plot(BSFG[:,0],np.log(BSFG[:,1]),label="BSFG")
#plt.plot(HF[:,0],np.log(HF[:,1]),label="HF")

#plt.errorbar(experimental[:,0]/1000,experimental[:,1],yerr=experimental[:,2],fmt='ro', label="Segawa et.al.")
plt.xlabel("Energy in MeV")
plt.ylabel("cross section in mb")
plt.legend()
plt.xlim(0,20)
plt.show()