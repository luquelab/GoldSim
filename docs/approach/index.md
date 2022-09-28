---
layout: default
title: Approach
nav_order: 4

\usepackage{mathtools}
\usepackage{physics}
---

# Approach

This section describes the mathematical formalism used for the modules.

---

## Module 1 - eDAR

eDAR stands for electron Donor-Acceptor Ratio. When there are more electron donors acceptors (oxygen) than donors (sugar) in a given ecosystem, a catabolic metabolism dominates. Otherwise, anabolic metabolism dominates. The electron acceptors and donors are never balanced.

This module models respiration, photosynthesis and oxygen runoff.

$$
\begin{align*}
  \frac{d W}{d t}&=&R^{W}_{in}W - \lambda P^{W}_{out} W \\
  \frac{d C}{d t}&=&R^{W}_{in}C - \lambda P^{C}_{out} C\\
  \frac{d O}{d t}&=&\lambda P^{O}_{in}O - R^{O}_{out} O - \gamma O\\	
  \frac{d S}{d t}&=&\lambda P^{S}_{in}S - R^{S}_{out} S
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
|$$\alpha_1$$ | $$O_2$$ to $$C_{6}H_{12}O_{6}$$ stoichiometry | |0.29  |
|$$\alpha_2$$ | $$H_2O$$ to $$CO_{2}$$ stoichiometry | |0.51|
|$$R^j_i$$| Respiration rate| $$h^{-1}$$ | [0,1]  |
|$$P^j_i$$| Photosynthesic rate| $$h^{-1}$$ | [0,1] |
|$$\gamma$$ | $$O_2$$ runoff rate | $$h^{-1}$$  | [0,1]   |
|$$\alpha^p_{out}$$ | Photosynthesis to O |   | 0.51 |
|$$\alpha^p_{out}$$ | Respiration to W |   | 0.29 |

where $$\lambda$$ is a coefficient that limits the concentration of $$CO_2$$ that can be metabolized according to the amount of Photosynthetic Active Radiation (PAR) available and $$\alpha$$ controls the $$O_2$$ runoff.


Let us define $$P^{W}_{out}=\alpha_1 P^{C}_{out}$$ and $$R^{S}_{out}=\alpha_2 R^{0}_{out}$$, where $\alpha_1$ and $\alpha_2$ are the stoichoimetric coefficients for $$CO_2$$ to $$H_{2}0$$ and $$O_2$$ to $$C_{6}H_{12}O_{6}$$, respectively. Then, we have:

$$
\begin{align*}
  \frac{d W}{d t}&=&R^{W}_{in}W - \lambda \alpha_1 P^{C}_{out} W \\
  \frac{d C}{d t}&=&R^{W}_{in}C - \lambda P^{C}_{out} C \\
  \frac{d O}{d t}&=& P^{O}_{in}O - R^{O}_{out} O - \gamma O \\	
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


## Module 2 - bacterial-phage ecology. Lysis-lysogeny decision

$$
\begin{align*}   
\frac{dB}{dt}&=&\underbrace{r H_{O_2}H_{DOC}H_{eDAR}B}_{\text{growth}} -
\underbrace{dBP}_{\text{Infection}} \\
\frac{dP}{dt}&=&\underbrace{c\mu_p \big[1 - \mathcal{P}(L)\big]I_n}_{burst} -
\underbrace{dBP}_{\text{infection}} - \underbrace{mP}_{\text{viral decay}} + 
\underbrace{c\mu_i L}_{\text{burst induction}} \\ 
\frac{dI_n}{dt}&=&\underbrace{dBP}_{\text{Infection}} - 
\underbrace{\big[1 -\mathcal{P}(L) \big] I_n}_{\text{lysis}} -
\underbrace{\mathcal{P}(L) I_n}_{lysogeny} \\ 
\frac{dL}{dt}&=&\underbrace{rH_{O_2}H_{DOC}H_{eDAR}L}_{\text{growth}} +
\underbrace{\mathcal{P}(L)I_n }_{\text{lysogeny}} -
\underbrace{\mu_i L}_{\text{induction}} \\
\end{align*}
$$


| Parameter | Description | Value| Source| 
| ----------- | ----------- | ----------- | ----------- | 
| r | Maximum Growth Rate | $$0.17 h^{-1} $$|  Silveira et. al, 2021 |             
| H | Hill functions      | $$[0,1]$$ |   | 
| d | Infection rate |  $$3e-8 ml/h $$  |  |
| $$\mu_p$$ | Lysis rate |  |   | 
| c | Burst size | 5 | ??  | 
| $$\mathcal{P}(L)$$ | Probability of lysogeny | $$[0.01, 0.6]$$ | Silveira et. al, 2021  |
| m | Decay rate | $$0.005 h^{-1}$$| Da Paepe et al, 2006  | 
| $$\mu_i$$ | Induction rate |  |   |
