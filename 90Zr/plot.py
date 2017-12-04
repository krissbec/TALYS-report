import numpy as np
import matplotlib.pyplot as plt

ZrDefault = np.loadtxt("rp041091.tot", skiprows=5, usecols=(0,1))
ZrDefaulttest = np.loadtxt("rp041091test.tot", skiprows=5, usecols=(0,1))
Artemis = np.loadtxt("artemis.tot", usecols=(0,4,6))
#HF = np.loadtxt("hf209.tot", skiprows=5, usecols=(0,1))
#experimental = np.loadtxt("Expdata208ng.txt", skiprows=1, usecols=(0,1,2))

plt.plot(ZrDefault[:,0],np.log(ZrDefault[:,1]),label="TALYS")
plt.plot(ZrDefaulttest[:,0],np.log(ZrDefaulttest[:,1]),label="TALYS")
#plt.plot(Artemis[:,0]/1000,np.log(Artemis[:,1]),label="A.Spyrou et.al.")
#plt.plot(HF[:,0],np.log(HF[:,1]),label="HF")


plt.errorbar(Artemis[:,0]/1000,np.log(Artemis[:,1]),yerr=Artemis[:,2],fmt='ro', label="Artemis et.al.")
plt.xlabel("Energy in MeV")
plt.ylabel("cross section in mb")
plt.legend()
#plt.xlim(-1,20)
plt.show()