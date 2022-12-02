#2/12/2022 - Modified version of the Hill Function for eDAR

import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib 


eDAR_vec=np.arange(0, 2, 0.01)
print(eDAR_vec)

Ka=1
exponents=[1,3,5,7,9]
Hills=[]

for exponent in exponents:
    Hill=[(eDAR)**exponent/(eDAR**exponent + Ka**exponent) for eDAR in eDAR_vec]

    Hills.append(Hill)


#Fontsizes
size_axis=9;size_ticks=9;

plt.plot(eDAR_vec,Hills[-2],label="Ka="+str(exponents[-2]), color='r')
plt.ylabel('Hill(e-DAR)',fontsize=size_axis)
plt.xlabel('e-DAR',fontsize=size_axis)


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
