---
layout: default
title: phacos
nav_order: 7
---

# PHACOS Experiment

## Corrected Hill function

The carrying capacity will be changed by a Hill function of eDAR. Recall that:

$$\begin{equation*}
eDAR=6 \frac{C_6H_{12}O_6}{O_2}
\end{equation*}	$$

Here, we will consider that:
$$\begin{equation*}
eDAR= \frac{DOC}{O_2}
\end{equation*}	$$

and will not make assumptions about the stoichiometry of DOC to $O_2$.

However, a conventional Hill Function will not be realistic, because it requires eDAR to take values between 0 and infinite. This is not something to expect. The first question was, what are realistic minimum and maximum values of eDAR?
According to [Silveira et al, 2019](https://doi.org/10.7554/eLife.49114), we have:

$$\begin{eqnarray*}
eDAR_{min}=0.24\\
eDAR_{max}=1.36
\end{eqnarray*}	$$

Let us assume, for modeling purposes that:
$$\begin{eqnarray*}
eDAR_{min}=0.1\\
eDAR_{max}=1.5
\end{eqnarray*}	$$

Then, the corrected Hill Function should fulfill three conditions:
1. $$H'(eDAR_{min})=0$$
2. $$H'(eDAR_{max})=1$$
3. $$H'(1)=0.5$$. This is because eDAR=1 corresponds to the goldilocks line.

From these three conditions, we proposed the following function:

$$\begin{equation*}
H'(eDAR)=\frac{(eDAR - eDAR_{min})^{n}}{K^n + \alpha (eDAR - eDAR_{min})^{n}}
\end{equation*}	$$

where $$\alpha=[0,1]$$ is a coefficient that approaches $$H'(eDAR)$$ to 1 for values close to $$eDAR_{max}$$ and K is the value of eDAR that makes $$H'(eDAR)=0.5$$ (Goldilocks line). The values of $$K$$ and $$\alpha$$ for $$H'(eDAR)$$ are:

$$\begin{eqnarray*}
K=(2-\alpha)^{1/n}(1-eDAR_{min}) \\
\alpha=\frac{(eDAR - eDAR_{min})^{n} - 2(1 - eDAR_{min}^{n}}{(eDAR - eDAR_{min})^{n} - (1 - eDAR_{min})^{n}}
\end{eqnarray*}	$$

