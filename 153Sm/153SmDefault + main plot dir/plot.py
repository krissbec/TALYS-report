import numpy as np
import matplotlib.pyplot as plt

Sm153calc= np.loadtxt("rp062154.tot", skiprows=5, usecols=(0,1))
JEFF32= np.loadtxt("JEFFcs153.tot", skiprows=11, usecols=(0,1))
SmBSFG = np.loadtxt("rp062154BSFG.tot", skiprows=5, usecols=(0,1))
SmSFG = np.loadtxt("rp062154SFG.tot", skiprows=5, usecols=(0,1))
SmGoriely = np.loadtxt("rp062154Goriely.tot", skiprows=5, usecols=(0,1))
SmHila = np.loadtxt("rp062154Hila.tot", skiprows=5, usecols=(0,1))
SmHFB = np.loadtxt("rp062154HFB.tot", skiprows=5, usecols=(0,1))
#HF = np.loadtxt("hf209.tot", skiprows=5, usecols=(0,1))
#experimental = np.loadtxt("Expdata208ng.txt", skiprows=1, usecols=(0,1,2))
plt.loglog(JEFF32[:,0],JEFF32[:,1]*1e3,label="JEFF-3.2")
plt.loglog(Sm153calc[:,0],Sm153calc[:,1],label="TALYS FGM")
plt.loglog(SmSFG[:,0],SmSFG[:,1],label="TALYS GSF")
plt.loglog(SmBSFG[:,0],SmBSFG[:,1],label="TALYS BSFG")
plt.loglog(SmGoriely[:,0],SmGoriely[:,1],label="TALYS Goriely")

plt.loglog(SmHila[:,0],SmHila[:,1],label="TALYS Hilarie")
plt.loglog(SmHFB[:,0],SmHFB[:,1],label="TALYS HFB")
#plt.plot(BSFG[:,0],np.log(BSFG[:,1]),label="BSFG")
#plt.plot(HF[:,0],np.log(HF[:,1]),label="HF")

#plt.errorbar(experimental[:,0]/1000,experimental[:,1],yerr=experimental[:,2],fmt='ro', label="Segawa et.al.")
plt.xlabel("Energy in MeV")
plt.ylabel("cross section in mb")
plt.legend(prop={'size': 11})
plt.xlim(0,20)
plt.show()