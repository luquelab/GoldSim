---
layout: default
title: Approach
nav_order: 4

\usepackage{mathtools}
\usepackage{physics}
\usepackage[version=4]{mhchem}
---

# Approach

This section describes the mathematical formalism used for the modules.

---

## Module 1 - eDAR

### Photosynthesis and respiration

eDAR stands for electron Donor-Acceptor Ratio. When there are more electron donors acceptors (oxygen) than donors (sugar) in a given ecosystem, a catabolic metabolism dominates. Otherwise, anabolic metabolism dominates. 
This module models respiration, photosynthesis, and fermentation. 
Let us start writing the differential equations that model a system that does respiration and photosynthesis: 

$$
\begin{align}
  \frac{d W}{d t}&=&R^{W}_{in}W - \lambda P^{W}_{out} W \\
  \frac{d C}{d t}&=&R^{C}_{in}C - \lambda P^{C}_{out} C \nonumber \\
  \frac{d O}{d t}&=& \lambda P^{O}_{in}O - R^{O}_{out} O \nonumber \\	
  \frac{d S}{d t}&=& \lambda P^{S}_{in}S - R^{S}_{out} S \nonumber
\end{align}
$$

Each equation describes the rate at which the concentration of the corresponding compound changes, with $$W$$, $$C$$, $$O$$, and $$S$$, representing $$H_2O$$, $$CO_2$$, $$O_2$$, 
and $$C_6H_{12}O_6$$, respectively. Naturally, changes are due to of respiration and photosynthesis. Respiration reduces the concentration of $$O$$ and $$S$$ at rates $$R^{O}_{out}$$, 
and $$R^{S}_{out}$$, and increases that of $$W$$ and $$C$$ at rates $$R^{W}_{in}$$ and $$R^{C}_{in}$$. Photosynthesis
does the opposite. However, the rates $$P^{W}_{out}$$, $$P^{C}_{out}$$, $$P^{O}_{in}$$, and $$P^{S}_{in}$$ are weighted by $$\lambda$$,
 a parameter related to Photosynthetic Active Radiation (PAR) that limits the amount of $$C$$ and $$W$$ that can be metabolized.


By conservation of matter, we know that:

$$
\begin{align}
R^{S}_{out}S + R^{O}_{out} O = R^{W}_{in}W + R^{W}_{in}C  \\
P^{W}_{out} W + P^{C}_{out} C =  P^{O}_{in}O + P^{S}_{in}S \nonumber
\end{align}
$$

By the stoichiometry of respiration and photosynthesis, we know that:

$$
\begin{align*}
R^{S}_{out} S=\alpha^{R}_{out} R^{O}_{out} O  \\
P^{W}_{out} W=\alpha^{P}_{out} P^{C}_{out} C \nonumber
\end{align*}
$$

and that:

$$
\begin{align}
R^{C}_{in} C = \alpha^{R}_{in}(R^{S}_{out}S + R^{O}_{out} O) \\
R^{W}_{in} W = (1-\alpha^{R}_{in})(R^{S}_{out}S + R^{O}_{out} O) \nonumber \\
P^{O}_{in} O  = \alpha^{P}_{in}(P^{W}_{out} W + P^{C}_{out} C) \nonumber \\
P^{W}_{in} W  = (1 - \alpha^{P}_{in})(P^{W}_{out} W + P^{C}_{out} C) \nonumber
\end{align}
$$

Combining the previous two equations we can rewrite it the previous equation as:

$$
\begin{align}
R^{C}_{in} C = \alpha^{R}_{in}(1 + \alpha^{R}_{out}) R^{O}_{out} O \\
R^{W}_{in} W = (1-\alpha^{R}_{in})(1 + \alpha^{R}_{out}) R^{O}_{out} O \nonumber \\
P^{O}_{in} O  = \alpha^{P}_{in}(1 + \alpha^{P}_{out}) P^{C}_{out} C \nonumber \\
P^{W}_{in} W  = (1 - \alpha^{P}_{in})(1 + \alpha^{P}_{out}) P^{C}_{out} C) \nonumber
\end{align}
$$

Definitions:

| Symbol | Meaning | Units| Value |
| ----------- | ----------- | ----------- | ----------- | 
|O| $$O_2$$ concentration | $$\frac{g}{m^3}$$ |  | 
|S| $$C_{6}H_{12}O_{6}$$  | $$\frac{g}{m^3}$$ | | 
|C| $$CO_2$$ | $$\frac{g}{m^3}$$ |  |  
|W| $$H_2O$$ | $$\frac{g}{m^3}$$ |  |
|E| $$C_2H_6O$$ | $$\frac{g}{m^3}$$ |  |   
| $$\lambda$$ | PAR Rate |         | [0,1]| 
|$$\alpha^{R}_{out}$$ | $$O_2$$ to $$C_{6}H_{12}O_{6}$$ stoichiometry | |0.29  |
|$$\alpha^{R}_{out}$$ | $$H_2O$$ to $$CO_{2}$$ stoichiometry | |0.51|
|$$P^j_i$$| Photosynthesic rate| $$h^{-1}$$ | [0,1] |
|$$R^j_i$$| Respiration rate| $$h^{-1}$$ | [0,1] |
|$$F^j_i$$| Fermentation rate| $$h^{-1}$$ | [0,1], 2\cdotR^j_i$$ |
|$$\alpha^P_{in}$$ | Photosynthesis to O |   | 0.51 |
|$$\alpha^R_{in}$$ | Respiration to W |   | 0.29 |


### Photosynthesis, respiration, and fermentation

As a next step, we include ethanol fermentation as an anaerobic metabolism:

$$
\begin{equation}
C6H12O6 \rightarrow 2 C2H6O + 2 CO2  
\end{equation}
$$

For the sake of our argument we will assume that fermentation happens at twice the rate as respiration occurs. This gives the following differential equations for the governors:

$$
\begin{align}
  \frac{d W}{d t}&=&(1- e^-DAR)R^{W}_{in}W - \lambda P^{W}_{out} W \\
  \frac{d C}{d t}&=&(1- e^-DAR)R^{C}_{in}C + e^-DAR F^{C}_{in} C - \lambda P^{C}_{out} C \nonumber \\
  \frac{d O}{d t}&=& P^{O}_{in}O - (1-e^-DAR)R^{O}_{out} O  \nonumber \\	
  \frac{d S}{d t}&=& P^{S}_{in}S - (1-e^-DAR) R^{S}_{out} S - e^-DAR F^{S}_{out} S \nonumber \\
  \frac{d E}{d t}&=& e^-DAR F^{E}_{in} E \nonumber
  
\end{align}
$$

By conservation of matter:
$$
\begin{align}
R^{S}_{out} S + R^{O}_{out}=R^{W}_{in}W + R^{C}_{in}C \\
P^{S}_{in}S + P^{O}_{in}O=\lambda P^{W}_{out} W + \lambda P^{C}_{out} C \nonumber \\
F^{E}_{in}E + F^{C}_{in} C=F^{S}_{out} S \nonumber
\end{align}
$$

## Module 2 - Energy from metabolism

In this model, the rate of energy (power) is a positive function of the incoming power and a negative function of outcoming power:

$$
\begin{align} 
\frac{dE}{dt}&=&W_{in} - W_{out} , 
\end{align}
$$

The incoming power occurs via respiration and fermentation. The outcoming power represents the rate at which bacteria use the energy obtained for metabolism.

$$
\begin{align} 
\frac{dE}{dt}&=&\frac{dM_R}{dt} \frac{\epsilon_{R}}{m_{R}} + \frac{dM_F}{dt} \dot
\end{align}
$$


$$
\begin{align} 
\frac{dE}{dt}&=&\frac{dM_R}{dt} \frac{\epsilon_{R}}{m_{R}} + \frac{dM_F}{dt} \dot \frac{\epsilon_{F}}{m_{F}} - B \cdot w_B , 
\end{align}
$$

where $$\frac{dM_R}{dt}$$ and $$\frac{dM_E}{dt}$$ represent the mass being metabolized, $$\epsilon_{R}$$ and $$\epsilon_{F}$$ represent the energy generated by a single respiration and fermentation, and $$m_{R}$$ and $$m_{F}$$
the mass of a single respiration and a single fermentation. $$B$$ represents the concentration of bacteria, and $$w_B$$ is the metabolic rate of a single bacteria.

A single respiration entails $$m_{r1}=6.18e-22 g$$ from the six molecules of $$O_2$$ and a single molecule of $$C_6H_{12}O_6$$  and it generates 26 ATP molecules, or 25.7 meV. Each bacteria consumes $$w_b=1 J/h$$ .



Assume that $$E_{B}=1 J/(cells/ml)$$ is the energy that it takes to duplicate a bacteria. Then, the growth of bacteria can be expressed as:

$$
\begin{align} 
\frac{dB}{dt}&=&\frac{W_{out}}{E_{B}} B  
\end{align}
$$


