---
layout: default
title: phacos
nav_order: 7
---

# PHACOS Experiment

## Hill functions

The carrying capacity will be changed by a product of two Hill functions: a modified Hill function for eDAR and a Hill function for the
concentration of glucose.


### Corrected eDAR Hill Function

Regarding eDAR recall that:

$$\begin{equation*}
eDAR=6 \frac{C_6H_{12}O_6}{O_2}
\end{equation*}	$$

The factor 6 accounts for the fact that six molecules of O2 are required to oxidize a molecule of glucose. Although there are many sources
of DOC (Dissolved Organic Carbon) we are going to assume that all of these sources can be approximated by glucose or associations of glucose
molecules (for instance, sucrose is the main source of energy in this experiment, but we are going to assume that a molecule of sucrose is
equivalent to two molecules of glucose.)

Our Hill Function of eDAR cannot be a regular Hill function, because it would require eDAR to take values between 0 and infinite. This is not happening in the experiment we are trying to model. In fact, any problem that we want to model should start determining minimum and maximum
values of eDAR. In our case, and according to [Silveira et al, 2019](https://doi.org/10.7554/eLife.49114), we have:

$$\begin{eqnarray*}
eDAR_{min}=0.24\\
eDAR_{max}=1.36
\end{eqnarray*}	$$

For modeling purposes we assume:

$$\begin{eqnarray*}
eDAR_{min}=0.1\\
eDAR_{max}=1.5
\end{eqnarray*}	$$

Then, the corrected Hill Function should meet three conditions:
1. $$H'(eDAR_{min})=0$$
2. $$H'(eDAR_{max})=1$$
3. $$H'(1)=0.5$$. (Goldilocks line)

From these conditions, we propose the following function:

$$\begin{equation*}
H'(eDAR)=\frac{(eDAR - eDAR_{min})^{n}}{K^n + \alpha (eDAR - eDAR_{min})^{n}}
\end{equation*}	$$

where $$\alpha=[0,1]$$ is a coefficient that approaches $$H'(eDAR)$$ to 1 for values close to $$eDAR_{max}$$ and K is the value of eDAR that makes $$H'(eDAR)=0.5$$ (Goldilocks line). The values of $$K$$ and $$\alpha$$ for $$H'(eDAR)$$ are:

$$\begin{eqnarray*}
K=(2-\alpha)^{1/n}(1-eDAR_{min}) \\
\alpha=\frac{(eDAR_{max} - eDAR_{min})^{n} - 2(1 - eDAR_{min})^{n}}{(eDAR_{max}- eDAR_{min})^{n} - (1 - eDAR_{min})^{n}}
\end{eqnarray*}	$$

We further modify H'(eDAR) so that it ranges between 1 and 2 to control bacterial growth:

$$\begin{eqnarray*}
H''(eDAR)=1 + H'(eDAR)
\end{eqnarray*}	$$

H''(eDAR)=1 when the metabolism is totally catabolic and H''(eDAR)=2 when it is fully anabolic (it doubles growth rate).

## Glucose Hill Function

In this case, I will use a conventional Hill Function. However, I am going to model it such that it limits growth for very small values of
DOC concentration:

$$\begin{equation*}
H'(eDAR)=\frac{DOC^{3}}{K^3_{DOC} + DOC^{3}}
\end{equation*}	$$

The exponent $$n=3$$ was chosen out of convenience: it creates a function that only limits growth at very low concentrations, grows very fast, and particularly it is equal to 1 for the initial concentration of glucose ($$7.965 g/m^3$$).

 The maximum growth rate $$r_{max}$$ should be the one given for relatively low levels of sugar and catabolic side of the Goldilocks line.

## Phage bacterial dynamics

The phage bacterial dynamics consist of four differential equations:

$$\begin{eqnarray*}
\frac{dB}{dt}&=& \underbrace{r_{max}H''_{eDAR}H_{DOC}B}_{growth} - \underbrace{dBP}_{infection} \\
\frac{dP}{dt}&=& \underbrace{c\big(1-P(L)\big)\mu_pI}_{lytic burst} + \underbrace{c\mu_iL}_{induct growth} - \underbrace{mP}_{decay} \\
\frac{dI}{dt}&=& \underbrace{dBP}_{infection} - \underbrace{P(L)I}_{lysogenic} - \underbrace{\big(1-P(L)\big)L}_{lytic} \\
\frac{dL}{dt}&=& \underbrace{r_{max}H''_{eDAR}H_{DOC}L }_{growth} + \underbrace{P(L)I}_{new lysogens} - \underbrace{\mu_iL}_{induction}
\end{eqnarray*}	$$

Here, $$B$$, $$P$$, $$I$$, and $$L$$ represent sensitive bacteria, phages, infected bacteria, and lysogens, respectively. $$P(L)$$ represents the probability of lysogeny, i.e. how likely is an infected bacteria to become a lysogen. 
The probability of lysogeny is a function of the modified Hill function for the eDAR:

$$\begin{eqnarray*}
P(L)=( P_{max}(L) - P_{min}(L) ) H'(eDAR) + P_{min}(L)
\end{eqnarray*}$$

## Metabolic dynamics

There are two metabolic processes in this system: cellular respiration (aerobic/catabolic) and fermentation (anaerobic/anabolic). $$H'(eDAR)$$ controls the ratio of respiration to fermentation:
$$H'(eDAR)=0$$ corresponds to fully catabolic metabolism (only cellular respiration because there is more $$O_2$$ than $$C_{6}H_{12}O_{6}$$), whereas $$H'(eDAR)=1$$ corresponds to fully anaerobic metabolism (only fermentation).
This results in the following equations:

$$
\begin{align*}
  \frac{d O}{d t}&=& - (1 - H'(eDAR)) R^{O}_{out} O  \\	
  \frac{d S}{d t}&=& - (1 - H'(eDAR)) R^{S}_{out} S - H'(eDAR) F^{S}_{out} S 
\end{align*}
$$

where $$R^{O}_{out}$$, $$R^{S}_{out}$$, and $$F^{S}_{out}$$ control the rate at which the total number of bacteria consume $$O_2$$ and $$C_{6}H_{12}O_{6}$$ (via respiration or fermentation). 
These rates are related to the following values:
$$r^{O}_{out}=4e-18 g/(h cell)$$ is the O2 consumption per bacterial cell.
By stoichiometry of $$O_2$$ and $$C_{6}H_{12}O_{6}$$ in respiration, we can infer that:
$$r^{O}_{out}=3.748e-18 g/(h cell)$$
Finally, we assume that the rate of fermentation is double the rate of respiration:
$$f^{O}_{out}=7.496e-18 g/(h cell)$$


## Experiments




