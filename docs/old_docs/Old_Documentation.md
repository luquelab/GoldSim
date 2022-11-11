---
layout: default
title: Former Approach
nav_order: 5

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


| Parameter | Description | Value| Minimum/Maximum | Source| Phage Species| Host|
| ------- | -------------- | ----------- | ----------- | ----------- | ----------- | ----------- | 
| $$r$$ | Maximum Growth Rate |$$7 \cdot 10^{-3} h^{-1}$$| $$2.95 \cdot 10^{-3}, 7 \cdot 10^{-3} h^{-1}$$ | (Silveira et. al, 2021)|  |
| $$H$$ | Hill functions      | $$[0,1]$$ |   | | | 
| $$c$$ | Burst size | $$11$$ | |(M.Middelboe et al.,2001) | Myoviridae | Vibrio sp. |
| $$m$$ | Decay rate | $$0.528 hr^{-1}, 0.012 h^{-1}$$| |(C.A. Suttle,1994), Da Paepe et al, 2006   |Myoviridae |Vibrio sp. |
| $$\mathcal{P}(L)$$ | Probability of lysogeny | [0.1,0.7] |  |
| $$\mu_i$$ | Induction rate |$$1.2 \cdot 10^{-6} hr^{-1}$$| |Emily's thesis   | | |

Concentrations for lysogeny [0.01, 0.1]:

| Parameter | Description | Min | 1st Qu| Median| Mean| 3rd Qu| Max| Source|
|-------|--------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------| 
| $$d$$ | Phage adsorption rate | $$1.4 \cdot 10^{-9} ml/h $$| $$4.6 \cdot 10^{-8} ml/h $$ | $$1.1 \cdot 10^{-7} ml/h $$ | $$1.4 \cdot 10^{-7} ml/h $$ | $$2.1 \cdot 10^{-7} ml/h $$ | $$3.7 \cdot 10^{-7} ml/h $$ | Luque et. al, 2020 |
| $$\tau_{ld}$$ | Commitment time | $$11 h $$| $$109 h $$ | $$262 h $$ | $$311 h $$ | $$489 $$ | $$807 h $$ | Luque et. al, 2020 |
| $$B_0$$ | Initial sensitive concentration | $$3.8 \cdot 10^4 cells/ml$$ | $$4.7 \cdot 10^{5} cells/ml$$ | $$1.5 \cdot 10^{6}  cells/ml $$| $$2.1 \cdot 10^{6}  cells/ml $$| $$3.4 \cdot 10^{6}  cells/ml $$| $$6.7 \cdot 10^{6}  cells/ml $$|  Luque et. al, 2020 |
| $$P_0$$ | Initial phage concentration | $$1.8 \cdot 10^5 phage/ml$$ | $$4.0 \cdot 10^{6} phage/ml$$ | $$9.1 \cdot 10^{6}  phage/ml $$| $$1.3 \cdot 10^{7}  phage/ml $$| $$1.9 \cdot 10^{7}  phage/ml $$| $$3.9 \cdot 10^{7}  phage/ml $$|  Luque et. al, 2020|
| $$L_0$$ | Initial lysogen concentration | $$0.01 \cdot B_0 $$| $$0.0325 \cdot B0$$ | $$0.055 \cdot B0$$ | $$0.055 \cdot B0$$ | $$0.0775 \cdot B0$$ | $$0.1 \cdot B_0 $$ | inferred from Luque et. al, 2020 |
| $$I_{N0}$$ | Initial infected concentration |$$0 cells/ml $$| | | | | |
| $$I_{P0}$$ | Initial phage producing concentration | $$0 cells/ml $$| | | | | |

Concentrations for lysogeny [0.1, ~0.5]:

| Parameter | Description | Min | 1st Qu| Median| Mean| 3rd Qu| Max| Source|
|------|----------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| $$d$$ | Phage adsorption rate | $$6.2 \cdot 10^{-9} ml/h $$| $$7.8 \cdot 10^{-8} ml/h $$ | $$1.6 \\cdot 10^{-7} ml/h $$ | $$1.7 \cdot 10^{-7} ml/h $$ | $$2.5 \cdot 10^{-7} ml/h $$ | $$3.7 \cdot 10^{-7} ml/h $$ | Luque et. al, 2020 |
| $$\tau_{ld}$$ | Commitment time | $$13 h $$| $$183 h $$ | $$352 h $$ | $$376 h $$ | $$558 $$ | $$807 h $$ | Luque et. al, 2020 |
| $$B_0$$ | Initial sensitive concentration | $$3.8 \cdot 10^4 cells/ml$$ | $$7.9 \cdot 10^{5} cells/ml$$ | $$2.0 \cdot 10^{6}  cells/ml $$| $$2.5 \cdot 10^{6}  cells/ml $$| $$3.9 \cdot 10^{6}  cells/ml $$| $$6.7 \cdot 10^{6}  cells/ml $$|  Luque et. al, 2020 |
| $$P_0$$ | Initial phage concentration | $$6.2 \cdot 10^5 phage/ml$$ | $$6.3 \cdot 10^{6} phage/ml$$ | $$1.3 \cdot 10^{7}  phage/ml $$| $$1.6 \cdot 10^{7}  phage/ml $$| $$2.5 \cdot 10^{7}  phage/ml $$| $$3.9 \cdot 10^{7}  phage/ml $$|  Luque et. al, 2020 |
| $$L_0$$ | Initial lysogen concentration | $$0.1 \cdot B_0 $$| $$~0.2 \cdot B0$$ | $$~0.3 \cdot B0$$ | $$~0.3 \cdot B0$$ | $$~0.4 \cdot B0$$ | $$~0.5 \cdot B_0 $$ | inferred from Luque et. al, 2020|
| $$I_{N0}$$ | Initial infected concentration |$$0 cells/ml $$| | | | | |
| $$I_{P0}$$ | Initial phage producing concentration | $$0 cells/ml $$| | | | | |


$$
\begin{align*}   
\frac{dB}{dt}&=&\underbrace{r(MTE)B}_{\text{growth}} -
\underbrace{dBP}_{\text{Infection}} \\
\frac{dP}{dt}&=&\underbrace{c\mu_p \big[1 - \mathcal{P}_L(eDAR)\big]I_n}_{burst} -
\underbrace{dBP}_{\text{infection}} - \underbrace{mP}_{\text{viral decay}} + 
\underbrace{c\mu_i (eDAR) L}_{\text{burst induction}} \\ 
\frac{dI_n}{dt}&=&\underbrace{dBP}_{\text{Infection}} - 
\underbrace{\big[1 -\mathcal{P}_L(eDAR) \big] I_n}_{\text{lysis}} -
\underbrace{\mathcal{P}_L(eDAR) I_n}_{lysogeny} \\ 
\frac{dL}{dt}&=&\underbrace{r(MTE)L}_{\text{growth}} +
\underbrace{\mathcal{P}_L(eDAR)I_n }_{\text{lysogeny}} -
\underbrace{\mu_i(eDAR) L}_{\text{induction}} \\
\end{align*}
$$

## Module 3 - Protist-pathogen interaction

Protists (E) are generally defined as unicellular eukariotes. For our purposes, protists kill bacteria and are poisoned by pathogens (lysogens). 

$$
\begin{align*}   
\frac{dB}{dt}&=&\underbrace{r(MTE)B}_{\text{growth}} -
\underbrace{dBP}_{\text{Infection}} - \underbrace{d_E BE}_{\text{protist predation}}\\
\frac{dL}{dt}&=&\underbrace{r(MTE)L}_{\text{growth}} +
\underbrace{\mathcal{P}_L(eDAR)I_n }_{\text{lysogeny}} -
\underbrace{\mu_i(eDAR) L}_{\text{induction}} \\
\frac{dE}{dt}&=&\underbrace{r_E(MTE, d_E)E}_{\text{growth and protist predation}} - \underbrace{d_E EL}_{\text{pathogen-protist immunity}}\\
\end{align*}
$$


