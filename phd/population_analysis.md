---
tags: PhD
date: 2021--10--28
type: note
---

# Population Analysis

Some more of these are probably available in my literature review / thesis.

## Pairwise correlations

- Just compute a bunch of these, e.g. as in Stringer et al Science 2019.
- It is hard to interpret though, and feels as though it does not make full use of the population available.

## Sorted raster plots

A common method of activity visualisation is to perform raster plots with sorted neurons.
However: note that the chosen sorting method greatly changes how the data appears.
For instance: A PCA sorting can make data appear quite uniform, while a manifold embedding can make the data look much more chaotic.
This is further emphasised with random sorting.

## Shared variance component analysis

- Asymptotically unbiased lower-bound estimate for the amount of a neural population's variance reliably encoding a latent signal.
- Seems to require two populations.
- Implemented in Stringer et al. Science 2019 but I should look for another place too.
- Needs thousands of cells recorded per area - so tough without CI TBH.

## Peer prediction anlaysis

- Predict acitvity of one neuron from the others.
- To contrast with SVCA, "SVCA finds the dimensions of activity in a large population that can be most reliably predicted from a held-out set of neurons" Stringer et al. 2019.
- Can use lower (much) N cells as a result.

## gLARA - Group Latent Auto-Regressive Analysis

- Instead of analysing direct connections from neurons, latent variables are estimated for different groups, and then these are related to eachother.
- Similar to pCCA - probabilistic canonical correlations.

## ANNs

- Usually either goal directed or data driven. See cunningham 2017 for more.
- Effective in areas such as PMC and retinal ganglion, but not sure on multi-region ANNs.

## To check

- Anything in brainbox? https://github.com/int-brain-lab/ibllib/blob/master/brainbox/ephys_plots.py