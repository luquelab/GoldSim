---
layout: default
title: phacos
nav_order: 7
---

# PHACOS Experiment

## Corrected Hill function

The carrying capacity will be changed by a product of two Hill functions: a modified Hill function for eDAR and a Hill function for the
concentration of glucose.


## eDAR Hill Function

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

Then, the corrected Hill Function should fulfill three conditions:
1. $$H'(eDAR_{min})=0$$
2. $$H'(eDAR_{max})=1$$
3. $$H'(1)=0.5$$. (Goldilocks line)

From these three conditions, we proposed the following function:

$$\begin{equation*}
H'(eDAR)=\frac{(eDAR - eDAR_{min})^{n}}{K^n + \alpha (eDAR - eDAR_{min})^{n}}
\end{equation*}	$$

where $$\alpha=[0,1]$$ is a coefficient that approaches $$H'(eDAR)$$ to 1 for values close to $$eDAR_{max}$$ and K is the value of eDAR that makes $$H'(eDAR)=0.5$$ (Goldilocks line). The values of $$K$$ and $$\alpha$$ for $$H'(eDAR)$$ are:

$$\begin{eqnarray*}
K=(2-\alpha)^{1/n}(1-eDAR_{min}) \\
\alpha=\frac{(eDAR_{max} - eDAR_{min})^{n} - 2(1 - eDAR_{min})^{n}}{(eDAR_{max}- eDAR_{min})^{n} - (1 - eDAR_{min})^{n}}
\end{eqnarray*}	$$

Furthermore, I modify H'(eDAR) so that it ranges between 1 and 2. Therefore:

$$\begin{eqnarray*}
H''(eDAR)=1 + H'(eDAR)
\end{eqnarray*}	$$

H''(eDAR)=1 when the metabolism is totally catabolic and H''(eDAR)=2 when the metabolism is fully anabolic (it doubles growth rate).

## Glucose Hill Function

In this case, I will use a conventional Hill Function. However, I am going to model it such that it limits growth for very small values of
DOC concentration:

$$\begin{equation*}
H'(eDAR)=\frac{DOC^{3}}{K^3_{DOC} + DOC^{3}}
\end{equation*}	$$

The exponent was chosen out of convenience to create a function that only limits growth at very low concentrations and grows very fast.