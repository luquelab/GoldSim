---
title: " A method for underwater sampling accounting for dilution"
subtitle: ""
author: "Sergio Cobo-Lopez, Forest L. Rohwer"
csl: "podzemna-voda.csl"
abstract: "Underwater measurements are important in field biology. Measurements are made from sites of interest that usually have a higher density of specific variables. This requires control over density, because of dilution rates"
graphics: yes
header-includes:
  - \usepackage{color}
  - \usepackage{caption}
  - \usepackage{anysize}
  - \usepackage{amsmath}
  - \usepackage{siunitx}

---

[comment]: <> (To compile this document with a bibliography: pandoc Sampling_Paper.md -o Sampling_Paper.pdf --bibliography ../../data/1_references/References.bib)

## Introduction

### Hypothesis and background

### Knowledge gap

### How to fill the knowledge gap

\begin{figure}[htbp]\centering\includegraphics[width=0.5\textwidth, height=!]{/home/sergio/work/Github/GoldSim/results/Figures_Sample_Paper/Figure_1.pdf}\caption{ \textbf{The subaquatic sampling system consists of an environment ($E$), a system of interest ($I$), and a sample ($S$)} The system of interest ($I$) is a subset of the environment ($E$). The hypothesis is that the concentration of certain biogeochemical properties is larger in $I$ than $E$ ($D_I>D_E$). As $I$ is sampled, $D_I$ will decrease by water dilution}\end{figure}



## Methods

| Input | Volume | Density |
| ----------- | ----------- |----------- |
|Environment|        $V_E=\inf$    | $D_E=10^6 VLP/ml$|
|System of Interest| $V_I=1.4 L$   | $D_I=10^7 VLP/ml$|
|Sample|             $V_S=0.5 L$   | $D_S=?$|
|Sample rate|        $v=10 ml/s$ | |

Let $I$ be a subaquatic system of interest in an environment $E$ with a constant volume $V_I$ (Figure 1). Suppose that our hypothesis is that the concentration of a certain biogeochemical property is higher in $I$ than in $D$, $D_I(t=0)>D_E$. To test this hypothesis, we take a sample $S$ from $I$. Let that sample have a volume $V_S$. As water flows out from $I$ at a rate $v$, water flows in from $E$ at the same rate, thus diluting the concentration $D_I$ over time.

Given the sample $S$, with volume $V_S$, and concentration $D_S$, we want to be able to infer the initial concentration of interest $D_I$.

First, we want to get the concentration $D_I$ as a function of time as we extract water at a rate of $v$. Because $V_I$ is constant, only the mass $M_I$ changes over time:

\begin{equation} 
\frac{dM_I}{dt}=(-D_I(t) + D_E)v \,
\end{equation}

Integrating, and dividing by $V_I$ we get the density:

\begin{equation}
D_I(t)=D_E - (D_E - D_I(0)) \exp^{-\frac{v}{V_I} t}
\end{equation}


In the case of the sample both the mass and density change over time:

\begin{eqnarray} 
\frac{dM_S}{dt}&=&D_Iv \\
\frac{dV_S}{dt}&=&v 
\end{eqnarray}

Integrating, we get:

\begin{equation}
M_S(t)=M_s(0) + vD_Et - (M_I(0) - D_E V_I) \exp^{-\frac{-v}{V_I}t}.
\end{equation} 

For the volume:

\begin{equation}
V_S(t)=v T 
\end{equation}
 

## Results

\begin{figure}[htbp]\centering\includegraphics[width=0.5\textwidth, height=!]{/home/sergio/work/Github/GoldSim/results/Figures_Sample_Paper/Figure2.png}\caption{ \textbf{GoldSim model of the sampling} The model integrates the mass, volume, and density of $I$ and $S$ over time}\end{figure}

\begin{figure}[htbp]\centering\includegraphics[width=0.5\textwidth, height=!]{/home/sergio/work/Github/GoldSim/results/Figures_Sample_Paper/Density_Interest.png}\caption{ \textbf{Density of system of Interest ($D_I$) over time} $D_I$ decreases exponentially to $D_E$, the density of the environment}\end{figure}

\begin{figure}[htbp]\centering\includegraphics[width=0.5\textwidth, height=!]{/home/sergio/work/Github/GoldSim/results/Figures_Sample_Paper/Density_Sample.png}\caption{ \textbf{Density of Sample ($D_S$) over time}}\end{figure} 



## Discussion
