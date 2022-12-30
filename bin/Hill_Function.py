#2/12/2022 - Modified version of the Hill Function for eDAR
#Update on 19/12/2022. Generalized version for min and maximum values

import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib 

#Domain of edar and vector of edar values
#--------------------------------------------
eDAR_min=0.1
eDAR_max=2

eDAR_vec=np.arange(eDAR_min, eDAR_max, 0.01)
#--------------------------------------------

#K for conventional Hill function
Ka=1

exponents=[1,3,5,7,9]
Hills=[]
Hills_Modified=[]

for exponent in exponents:
    #conventional hill
    Hill=[(eDAR)**exponent/(eDAR**exponent + Ka**exponent) for eDAR in eDAR_vec]

    #Modified hill and parameters
    alpha=( (eDAR_max-eDAR_min)**exponent - 2*(1-eDAR_min)**exponent)/((eDAR_max-eDAR_min)**exponent - (1-eDAR_min)**exponent)
    
    Ka_modified=(1-eDAR_min)*((2-alpha)**(1/exponent))
    
    Hill_Modified=[(eDAR-eDAR_min)**exponent/(alpha*((eDAR-eDAR_min))**exponent + Ka_modified**exponent) for eDAR in eDAR_vec]

    Hills.append(Hill)
    Hills_Modified.append(Hill_Modified)


#PLOTS
#--------------------------------------------------------------
#Fontsizes
size_axis=9;size_ticks=9;

plt.plot(eDAR_vec,Hills[-2],label="Ka="+str(exponents[-2]), color='r')
plt.plot(eDAR_vec,Hills_Modified[-2],label="Ka="+str(exponents[-2]), color='b')
plt.ylabel('Hill(e-DAR)',fontsize=size_axis)
plt.xlabel('e-DAR',fontsize=size_axis)

print(Hills[-2])
print(Hills_Modified[-2])
# for Hill in range(len(Hills)):
#     plt.plot(eDAR_vec,Hills[Hill],label="Ka="+str(exponents[Hill]))
#     plt.ylabel('Hill(e-DAR)',fontsize=size_axis)
#     plt.xlabel('e-DAR',fontsize=size_axis)
#     plt.legend(loc='best',fontsize=size_ticks,frameon=False)

width_line=1
plt.axhline(y=0.5, color='k', linewidth=width_line,linestyle='dashed')
plt.axvline(x=Ka, color='k', linewidth=width_line,linestyle='dashed')

plt.ylabel('Hill function',fontsize=size_axis)
plt.xlabel('e-DAR',fontsize=size_axis)
plt.legend(loc='best',fontsize=size_ticks,frameon=False)


plt.show()
#--------------------------------------------------------------
