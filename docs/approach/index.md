---
layout: default
title: Approach
nav_order: 4
---

# Approach

This section describes the mathematical formalism used for the modules.

## Module 1 - Phage-Bacterial dynamics

$$\begin{eqnarray*}
\frac{dB}{dt}&=& \underbrace{r_{max}H''_{eDAR}H_{DOC}B}_{growth} - \underbrace{dBP}_{infection} \\
\frac{dP}{dt}&=& \underbrace{c\big(1-P(L)\big)\mu_pI}_{\text{lytic burst}} +\underbrace{c\mu_iL}_{\text{induct growth}} - \underbrace{mP}_{decay} \\
\frac{dI}{dt}&=& \underbrace{dBP}_{infection} - \underbrace{P(L)I}_{lysogenic} - \underbrace{\big(1-P(L)\big)L}_{lytic} \\
\frac{dL}{dt}&=& \underbrace{r_{max}H''_{eDAR}H_{DOC}L }_{growth} +
\underbrace{P(L)I}_{\text{new lysogens}} - \underbrace{\mu_iL}_{induction}
\end{eqnarray*} $$

In this model, bacterial growth and lytic/lysogenic infection are metabolic-dependent processes:

#1. Bacterial Growth:

$$\begin{equation}
\frac{dB_{growth}}{dt}&=&r_{max}H''_{eDAR}B
\end{equation}$$

#2. Probability of Lysogeny:

$$\begin{eqnarray*}
P_L=P_L(max)H'(eDAR) + P_L(min) (1 - H'(eDAR))
\end{eqnarray*}$$

$$H'(eDAR)$$ and $$H''(eDAR)$$ are modified Hill Functions such that:

$$\begin{equation*}
H''(eDAR) = 1 + H'(eDAR)
\end{equation*}$$


Per capita version of the model:

$$\begin{eqnarray*}
\frac{1}{B}\frac{dB}{dt}&=& r_{max}H''_{eDAR}H_{DOC}} - dP \\
\frac{1}{P}\frac{dP}{dt}&=& \frac{c\big(1-P(L)\big)\mu_pI}{P} +\frac{c\mu_iL}{P} - m \\
\frac{1}{I}\frac{dI}{dt}&=& \frac{dBP}{I} - P(L) - \big(1-P(L)\big)\frac{L}{I} \\
\frac{1}{L}\frac{dL}{dt}&=& r_{max}H''_{eDAR}H_{DOC} + \frac{P(L)I}{L} - \mu_i
\end{eqnarray*} $$



and


$$\begin{equation}
H'(eDAR) = \frac{(eDAR - eDAR_{min})^{n}}{K^n + \alpha (eDAR - eDAR_{min}
\end{equation}$$


where $$\alpha=[0,1]$$ is a coefficient that approaches $$H'(eDAR)$$
to 1 for values close to $$eDAR_{max}$$ and K is the value of eDAR
such that $$H'(eDAR)=0.5$$ (Goldilocks line). For convenience, we set arbitrary values for the minimum and maximum values of $$eDAR$$:

$$\begin{eqnarray*}
eDAR_{min}=0.1\\
eDAR_{max}=1.5
\end{eqnarray*} $$ 


## Module 2 - eDAR

eDAR stands for electron Donor-Acceptor Ratio. When there are more electron donors acceptors (oxygen) than donors (sugar) in a given ecosystem, a catabolic metabolism dominates. Otherwise, anabolic metabolism dominates. In the case of cellular respiration, where glucose ($$C_{6}H_{12}O_6$$) is the electron donor and oxygen ($$O_2$$) is the electron acceptor, we have:

$$
\begin{equation}
   eDAR=6\frac{C_{6}H_{12}O_6}{O_2}
\end{equation}
$$

where the brackets represent concentration in molarity ($$mol/l$$) and the factor six corresponds to the stoichiometry of the respiration ( a molecule of glucose requires six molecules of $O_2$ for being completely oxidized). That is, eDAR is equal to 1 (Goldilocks line) if there are 6 moles of $O_2$ for mole of glucose. If we measure eDAR in grams:

$$
\begin{align}
   eDAR=6\frac{[C_{6}H_{12}O_6]}{[O_2]} = 6\frac{ X \cancel{mol C_{6}H_{12}O_6/\cancel{L}}}{Y \cancel{mol O_2}/\cancel{L}} \frac{180.156 g C_{6}H_{12}O_6}{\cancel{1 mole C_{6}H_{12}O_6}} \frac{\cancel{1 mol O_2}}{ 31.999 g} =\\
   6 \frac{180.156}{31.999 } \frac{X g C_{6}H_{12}O_6}{ Y g O_2} = 33.78 \frac{X g C_{6}H_{12}O_6}{ Y g O_2} \nonumber
\end{align}
$$

### Photosynthesis and respiration

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
  \frac{d C}{d t}&=&(1- e^-DAR)R^{C}_{in}C + e^-DAR \cdot F^{C}_{in} C - \lambda P^{C}_{out} C \nonumber \\
  \frac{d O}{d t}&=& P^{O}_{in}O - (1-e^-DAR)R^{O}_{out} O  \nonumber \\	
  \frac{d S}{d t}&=& P^{S}_{in}S - (1-e^-DAR) \cdot R^{S}_{out} S - e^-DAR \cdot F^{S}_{out} S \nonumber \\
  \frac{d E}{d t}&=& e^-DAR \cdot F^{E}_{in} E \nonumber
  
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

From the stoichiometry of the reactions we still have:

$$
\begin{align*}
R^{S}_{out} S=\alpha^{R}_{out} R^{O}_{out} O  \\
P^{W}_{out} W=\alpha^{P}_{out} P^{C}_{out} C \nonumber
\end{align*}
$$

## Module 3 - Energy from metabolism

In this model, the rate of energy (power) is a positive function of the incoming power and a negative function of outcoming power:

$$
\begin{align} 
\frac{dE}{dt}&=&W_{in} - W_{out} , 
\end{align}
$$

The incoming power occurs via respiration and fermentation. The outcoming power represents the rate at which bacteria use the energy obtained for metabolism.

$$
\begin{align} 
\frac{dE}{dt}&=&\frac{dM_R}{dt} \frac{\epsilon_{R}}{m_{R}} + \frac{dM_F}{dt} \frac{\epsilon_{F}}{m_{F}} - B  w_B , 
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


