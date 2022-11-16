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

eDAR stands for electron Donor-Acceptor Ratio. When there are more electron donors acceptors (oxygen) than donors (sugar) in a given ecosystem, a catabolic metabolism dominates. Otherwise, anabolic metabolism dominates. 
This module models respiration, photosynthesis, and fermentation. 
Let us start writing the differential equations that model a system that does respiration and photosynthesis: 

$$
\begin{align*}
  \frac{d W}{d t}&=&R^{W}_{in}W - \lambda P^{W}_{out} W \\
  \frac{d C}{d t}&=&R^{C}_{in}C - \lambda P^{C}_{out} C\\
  \frac{d O}{d t}&=& \lambda P^{O}_{in}O - R^{O}_{out} O \\	
  \frac{d S}{d t}&=& \lambda P^{S}_{in}S - R^{S}_{out} S 
\end{align*}
$$

Each equation describes the rate at which the concentration of the corresponding compound changes, with $$W$$, $$C$$, $$O$$, and $$S$$, representing $$H_2O$$, $$CO_2$$, $$O_2$$, 
and $$C_6H_{12}O_6$$, respectively. Naturally, changes are due to of respiration and photosynthesis. Respiration reduces the concentration of $$O$$ and $$S$$ at rates $$R^{O}_{out}$$, 
and $$R^{S}_{out}$$, and increases that of $$W$$ and $$C$$ at rates $$R^{W}_{in}$$ and $$R^{C}_{in}$$. Photosynthesis
does the opposite. However, the rates $$P^{W}_{out}$$, $$P^{C}_{out}$$, $$P^{O}_{in}$$, and $$P^{S}_{in}$$ are weighted by $$\lambda$$,
 a parameter related to Photosynthetic Active Radiation (PAR) that limits the amount of $$C$$ and $$W$$ that can be metabolized.


By conservation of matter, we know that:

$$
\begin{align*}
R^{S}_{out}S + R^{O}_{out} O = R^{W}_{in}W + R^{W}_{in}C \\
P^{W}_{out} W + P^{C}_{out} C =  P^{O}_{in}O + P^{S}_{in}S
\end{align*}
$$

By the stoichiometry of respiration and photosynthesis, we know that:

$$
\begin{align*}
R^{S}_{out} S=\alpha^{R}_{out} R^{O}_{out} O \\
P^{W}_{out} W=\alpha^{P}_{out} P^{C}_{out} C
\end{align*}
$$

and that:

$$
\begin{align*}
R^{C}_{in}C = \alpha^{R}_{in}(R^{S}_{out}S + R^{O}_{out} O) \\
R^{W}_{in}W = (1-\alpha^{R}_{in})(R^{S}_{out}S + R^{O}_{out} O) \\
P^{O}_{in} O  = \alpha^{P}_{in}(P^{W}_{out} W + P^{C}_{out} C) \\
P^{W}_{in} W  = (1 - \alpha^{P}_{in})(P^{W}_{out} W + P^{C}_{out} C)
\end{align*}
$$

Combining the previous two equations we can rewrite it the previous equation as:

$$
\begin{align*}
R^{C}_{in}C = \alpha^{R}_{in}(1 + \alpha^{R}_{out}) R^{O}_{out} O \\
R^{W}_{in}W = (1-\alpha^{R}_{in})(1 + \alpha^{R}_{out}) R^{O}_{out} O \\
P^{O}_{in} O  = \alpha^{P}_{in}(1 + \alpha^{P}_{out}) P^{C}_{out} C \\
P^{W}_{in} W  = (1 - \alpha^{P}_{in})(1 + \alpha^{P}_{out}) P^{C}_{out} C)
\end{align*}
$$

Definitions:

| Symbol | Meaning | Units| Value |
| ----------- | ----------- | ----------- | ----------- | 
|O| $$O_2$$ concentration | $$\frac{g}{m^3 h}$$ |  | 
|S| $$C_{6}H_{12}O_{6}$$  | $$\frac{g}{m^3 h}$$ | | 
|C| $$CO_2$$ | $$\frac{g}{m^3 h}$$ |  |  
|W| $$H_2O$$ | $$\frac{g}{m^3 h}$$ |  |   
| $$\lambda$$ | PAR Rate |         | [0,1]| 
|$$\alpha^{R}_{out}$$ | $$O_2$$ to $$C_{6}H_{12}O_{6}$$ stoichiometry | |0.29  |
|$$\alpha^{R}_{out}$$ | $$H_2O$$ to $$CO_{2}$$ stoichiometry | |0.51|
|$$R^j_i$$| Respiration rate| $$h^{-1}$$ | [0,1]  |
|$$P^j_i$$| Photosynthesic rate| $$h^{-1}$$ | [0,1] |
|$$\alpha^P_{in}$$ | Photosynthesis to O |   | 0.51 |
|$$\alpha^R_{in}$$ | Respiration to W |   | 0.29 |






where each equation describes the change of concentrations of a given
where $$\lambda$$ is the Photosynthetic Active Radiation (PAR) rate, which limits the amount of $$CO_2$$ and $$H_2O$$ that can be metabolized.
Let us define $$P^{W}_{out}=\alpha_1 P^{C}_{out}$$ and $$R^{S}_{out}=\alpha_2 R^{0}_{out}$$, where $$\alpha_1$$ and $$\alpha_2$$ are the stoichoimetric coefficients for $$CO_2$$ to $$H_{2}0$$ and $$O_2$$ to $$C_{6}H_{12}O_{6}$$, respectively. Then, we have:

$$
\begin{align*}
  \frac{d W}{d t}&=&R^{W}_{in}W - \lambda \alpha_1 P^{C}_{out} W \\
  \frac{d C}{d t}&=&R^{W}_{in}C - \lambda P^{C}_{out} C \\
  \frac{d O}{d t}&=& P^{O}_{in}O - R^{O}_{out} O \\
  \frac{d S}{d t}&=& P^{S}_{in}S - \alpha_2 R^{O}_{out} S 		
\end{align*}
$$

where

$$
\begin{align*}
   P^O_{in} O &=& \lambda \alpha^p_{out} P^C_{out} \big[\alpha_1 W + C \big] \\
   P^S_{in} S &=& \lambda (1 - \alpha^p_{out}) P^C_{out} \big[\alpha_1 W + C \big] \\
   R^W_{in} W &=& \alpha^r_{out} RO^O_{out} \big[\alpha_2 S + O \big] \\
   R^C_{in} C &=& (1 - \alpha^r_{out}) RO^O_{out} \big[\alpha_2 S + O \big]
\end{align*}
$$

As a next step, we include ethanol fermentation as an anaerobic metabolism:

$$\ch{C6H12O6 ->[ ] 2 C2H6O + 2 CO2}$$

For the sake of our argument (anaerobic vs aerobic metabolism) we will assume that fermentation happens at twice the rate as respiration occurs. This gives the following differential equations for the governors:

$$
\begin{align*}
  \frac{d W}{d t}&=&R^{W}_{in}W - \lambda \alpha_1 P^{C}_{out} W \\
  \frac{d C}{d t}&=&R^{W}_{in}C - \lambda P^{C}_{out} C + \alpha_4 2 \alpha_2 F^{O}_{out} E\\
  \frac{d O}{d t}&=& P^{O}_{in}O - R^{O}_{out} O  \\	
  \frac{d S}{d t}&=& P^{S}_{in}S - \alpha_2 R^{O}_{out} S - 2 \alpha_2 R^{O}_{out} S \\
  \frac{d E}{d t}&=& \alpha_3 2 \alpha_2 F^{O}_{out} E \\
  
\end{align*}
$$

## Module 2 - Energy from respiration

A single respiration entails $$m_{r1}=6.18e-22 g$$ from the six molecules of $$O_2$$ and a single molecule of $$C_6H_{12}O_6$$  and it generates 26 ATP molecules, or 25.7 meV. Let us call this energy $$E_{R1}$$. Let us assume as 
a first approximation that:
* 1. Energy from respiration is produced at a rate that is equal to the number of respiration cycles multiplied by $$E_{R1}$$.
* 2. Each bacteria consumes $$w_b=1 J/h$$ .
Then, the energy consumption can be expressed as:

$$
\begin{align*} 
\frac{dE}{dt}&=&W_{in} - W_{out} , 
\end{align*}
$$

where $$W_{in}=\frac{R^{O}_{out} O + \alpha_2 R^{O}_{out}}{m_{r1}} E_{R1}$$ and $$W_{out}=w_b B$$. The numerator in $$W_{in}$$ represents the rate of mass being consumed by respiration. The quotient gives the number
of respiration cycles per unit of time.

Assume that $$E_{B}=1 J/(cells/ml)$$ is the energy that it takes to duplicate a bacteria. Then, the growth of bacteria can be expressed as:

$$
\begin{align*} 
\frac{dB}{dt}&=&\frac{W_{out}}{E_{B}} B  
\end{align*}
$$


