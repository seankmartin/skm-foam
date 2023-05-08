---
tags: neuroscience
date: 2023--02--24
type: note
---

# Neural Dimension Reduction

## GPFA

Yu 2009 first GPFA introduction paper. Spike counts were taken in nonoverlapping 20-ms bins, then square-rooted.10 For the twostage methods, these square-rooted counts were first smoothed over time using a Gaussian kernel before being passed to a static dimensionality-reduction technique: PCA, PPCA, or FA. LDS and GPFA were given the square-rooted spike counts with no kernel presmoothing. In the results section, Yu et al. compared the performance of the twostage methods to that of LDS and GPFA. They found that the twostage methods performed worse than LDS and GPFA, and that the performance of the twostage methods was highly dependent on the dimensionality-reduction technique used. They also found that the twostage methods were more sensitive to the choice of hyperparameters than LDS and GPFA. Yu et al. concluded that the twostage methods were not suitable for neural dimension reduction.

## CCA and PCFA

In Semedo et al. 2022, the use the CCA and PCFA algorithms. The PCFA is jitter corrected.

## PCA

In Okazawa et al. 2021 they used PCA to visual the neural population response manifolds. For them, they applied this to the PSTHs.

## Some details

It seems window sizes are generally small (maybe a few 100ms), and the binsize ranges from 1 - 25ms. However, this is often chosen based on how narrow of an interaction we are looking. E.g. if using very small bins 1ms - 20ms, the CCA will often only pick up one dimension of activity. Also note pCCA, which also gives probabilities.

## References

1. Yu, Byron M., et al. "Gaussian-process factor analysis for low-dimensional single-trial analysis of neural population activity." Advances in neural information processing systems 21 (2008).
2. Semedo et al. Feedforward and feedback interactions between visual cortical areas use different population activity patterns.
3. Okazawa et al. 2021 - Representational geometry of perceptual decisions in the monkey parietal cortex.