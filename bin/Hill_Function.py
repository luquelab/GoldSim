#2/12/2022 - Modified version of the Hill Function for eDAR
#Update on 19/12/2022. Generalized version for min and maximum values
#Update 03/01/2023. A hill function for sugar

import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib 

#Domain of edar and vector of edar values
#--------------------------------------------
eDAR_min=0.1
eDAR_max=1.5

Initial_Glucose_Conc=7.965 #g/m3
Max_Glucose_Conc=1506 #g/m3

eDAR_vec=np.arange(eDAR_min, eDAR_max+0.01, 0.01)

eDAR_vec=np.arange(eDAR_min, 1.9+0.01, 0.01)
Glucose_vec=np.arange(0, Max_Glucose_Conc, 0.01)
#--------------------------------------------

#K for conventional Hill function
Ka=0.1*Initial_Glucose_Conc


exponents=[1,3,5,7,9]
Hills=[]
Hills_Modified=[]

for exponent in exponents:
    #conventional hill
    Hill=[(Glucose)**exponent/(Glucose**exponent + Ka**exponent) for Glucose in Glucose_vec]

    #Modified hill and parameters
    alpha=( (eDAR_max-eDAR_min)**exponent - 2*(1-eDAR_min)**exponent)/((eDAR_max-eDAR_min)**exponent - (1-eDAR_min)**exponent)
    print(alpha)
    
    Ka_modified=(1-eDAR_min)*((2-alpha)**(1/exponent))

    Hill_Modified=[(eDAR-eDAR_min)**exponent/(alpha*((eDAR-eDAR_min))**exponent + Ka_modified**exponent) for eDAR in eDAR_vec]

    Hills.append(Hill)
    Hills_Modified.append(Hill_Modified)


#PLOTS
#--------------------------------------------------------------
#Fontsizes
size_axis=9;size_ticks=9;
#exp_plot=1
#plt.plot(Glucose_vec,Hills[exp_plot],label="Ka="+str(exponents[exp_plot]), color='r')


plt.plot(eDAR_vec,Hills_Modified[-2],label="n="+str(exponents[-2]), color='b')
plt.ylabel('Hill(e-DAR)',fontsize=size_axis)
plt.xlabel('e-DAR',fontsize=size_axis)

width_line=1
plt.axhline(y=0.5, color='k', linewidth=width_line,linestyle='dashed')
plt.axvline(x=1, color='k', linewidth=width_line,linestyle='dashed')

plt.ylabel('Hill function',fontsize=size_axis)
plt.xlabel('e-DAR',fontsize=size_axis)
#plt.legend(loc='best',fontsize=size_ticks,frameon=False)


plt.show()
#--------------------------------------------------------------
