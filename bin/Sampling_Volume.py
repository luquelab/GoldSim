import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

def Mass_interest(de,vi,mi0,f,time):
    mi=de*vi - (de*vi - mio)*exp**(-v*time/vi)

    return mi
    
    


#Initial parameters
Vol_interest_vec=[vi for vi in np.arange(1,2,0.1)]
Vol_sample_vec=[vi for vi in np.arange(0.1,1.1,0.1)]
flow_rate_vec=[vf for vf in np.arange(1e-4,1.1e-3,1e-4)]


Den_environ=1e6 #things/ml

Vol_interest=1.4e3 #mL
Den_interest=1e7 #things/ml

Vol_sample=500 #mL

flow_rate=10 #mL/s

timestep=1 #s
time_experiment=60
time=np.arange(0,time_experiment + timestep,timestep)
print(time)

de=Den_environ
vi=Vol_interest
di0=Den_interest
mi0=Den_interest*Vol_interest
v=flow_rate

mi=de*vi - (de*vi - mi0)*np.exp(-v*time/vi)
di=de - (de - di0)*np.exp(-v*time/vi)

ms0= mi0 - vi*de
print(ms0)
ms = ms0 + v*de*time - vi*(di0 - de)*np.exp(-v*time/vi)
vs=v*time

ds=ms/vs

for  ind in range(len(time)):
    test=de - (vs[ind]/vi)*(ds[ind] - (ms0/vs[ind]) - de)*np.exp(v*time[ind]/vi)
    print(test)

plt.plot(time,ds)

plt.show()
