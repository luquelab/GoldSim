import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.pyplot import figure
import matplotlib.ticker as mtick



def mass_interest(de,vi,mi0,v,time):
    mi=de*vi - (de*vi - mi0)*np.exp(-v*time/vi)

    return mi

def mass_sample(mi0,de,vi,ms0,v,time):
    ms=v*de*time + vi*(de - (mi0/vi))*(np.exp(-v*time/vi)-1)
    
    return ms

#Initial parameters
Vol_interest_vec=[vi for vi in np.arange(1,2,0.1)]
Vol_sample_vec=[vi for vi in np.arange(0.1,1.1,0.1)]


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

mi=mass_interest(de,vi,mi0,v,time)
di=mi/vi

ms=mass_sample(mi0,de,vi,mi0,v,time)
vs=v*time
ds=ms/vs



v_vector=[0.1,1,10,50,100,1000]
print(v_vector)
print(len(v_vector))

di_of_ds=de-v*time*(ds-di)
di_list=[]
ds_list=[]
for vj in v_vector:
    mi_j=mass_interest(de,vi,mi0,vj,time)
    di_j=mi_j/vi
    di_list.append(di_j)

    ms_j=mass_sample(mi0,de,vi,mi0,vj,time)
    vs_j=vj*time
    ds_j=ms_j/vs_j
    ds_list.append(ds_j)
    



# Configuration of plots
#====================================================================
#Path to save figure
Output_Path='/home/sergio/work/Github/GoldSim/results/subaquatic_sampling/'

#Fontsizes
size_axis=7;size_ticks=6;size_title=5

#Figure Size
cm = 1/2.54  # centimeters in inches
Width=8*cm;Height=18*cm #Width and height of plots

#Gridspec
Rows=3;Cols=1

#Extensions to save                    
Extensions=['.png','.svg']            

#Linewidth                   
width_line=1                             
#====================================================================
fig=figure(figsize=(Width, Height), dpi=300)
gs=gridspec.GridSpec(Rows,Cols)  
gs.update(left=0.2,right=0.95,bottom=0.1,top=0.97,wspace=0.0,hspace=0.5)

ax_00=plt.subplot(gs[0,0]) 
plt.plot(time,di)
#plt.ticklabel_format(style='sci', axis='y',useOffset=None, scilimits=(0,0))
ax_00.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))



ylimits_left=ax_00.get_ylim()

plt.ylabel('D$_i$ (VLP/ml)',fontsize=size_axis)
plt.xlabel('time (s)',fontsize=size_axis)

#plt.ticklabel_format(axis='y', style='sci', scilimits=(7,7))
plt.xticks(fontsize=size_ticks)
plt.yticks(fontsize=size_ticks) 


ax_01=plt.subplot(gs[1,0])
plt.plot(time,ds)
ax_01.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))

plt.ylim([ylimits_left[0],ylimits_left[1]])

plt.ylabel('D$_s$ VLP/ml',fontsize=size_axis)
plt.xlabel('time (s)',fontsize=size_axis)

plt.xticks(fontsize=size_ticks)
plt.yticks(fontsize=size_ticks)

ax_02=plt.subplot(gs[2,0])
plt.plot(ds,di)
ax_02.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
ax_02.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
#plt.ylim([ylimits_left[0],ylimits_left[1]])
plt.ylabel('D$_i$ (VLP/ml)',fontsize=size_axis)
plt.xlabel('D$_s$ (VLP/ml)',fontsize=size_axis)

plt.xticks(fontsize=size_ticks)
plt.yticks(fontsize=size_ticks)

Name_Fig='Density_Interest_Sample'
[plt.savefig(Output_Path+Name_Fig+ext,dpi=300) for ext in Extensions]

plt.show()


#====================================================================
Width=8*cm;Height=5*cm #Width and height of plots
fig=figure(figsize=(Width, Height), dpi=300)

#Gridspec
Rows=1;Cols=1
gs=gridspec.GridSpec(Rows,Cols)  
gs.update(left=0.2,right=0.95,bottom=0.1,top=0.97,wspace=0.0,hspace=0.5)

ax_00=plt.subplot(gs[0,0])

index_30=np.where(time == 30)[0][0]

for element in range(len(v_vector)):
    plt.scatter(ds_list[element][-1],di_list[element][-1],s=10,label='v='+str(v_vector[element])+ ' ml/s')

#    plt.scatter(ds_list[element][index_30],di_list[element][index_30],s=10,marker="s",label='v='+str(v_vector[element])+ ' ml/s')
    print(element)

#zip(ds_list, di_list):
plt.legend(loc='best',fontsize=size_ticks)
# plt.xscale("log")
# plt.yscale("log")


plt.xlabel('Sample density (VLP/ml)',fontsize=size_axis)
plt.ylabel('Density of interest (VLP/ml)',fontsize=size_axis)

ax_00.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
ax_00.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))

#plt.ticklabel_format(axis='y', style='sci', scilimits=(7,7))
plt.xticks(fontsize=size_ticks)
plt.yticks(fontsize=size_ticks)

Name_Fig='Density_Interest_vs_Density_Sample'
[plt.savefig(Output_Path+Name_Fig+ext,dpi=300) for ext in Extensions]
plt.show()
