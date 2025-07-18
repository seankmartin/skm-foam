---
tags: PhD
---

# Thesis

## Possible avenues and things to do

1. Cool vis with brainrender https://www.biorxiv.org/content/10.1101/2020.02.23.961748v2.full
2. OR a vis with Inviwo (I have one these lying around).
3. Make a video/multiple videos on explanations. Can use e.g. https://github.com/ManimCommunity/manim.
4. Pull in all my old notes (where relevant). Just make sure not leaving out important sources for my ideas etc. No plagiarising accidentally!

## Why not FMRI as the focus

- Nothing wrong with it, for example see paper, the connectome predicts resting-state functional connectivity across the Drosophilia brain. This suggests that correlation in FMRI as a proxy for structural connectivity may be somewhat valid (link between functional connectivity + structural connectivity). However, they used CI to test it here.
- However, the main reason is the lack of temporal and spatial resolution. It has been shown that (check conclusion again myself here) metabolic flux tracks behavioural changes on a slow rate, about every 10s to 100seconds. This is fine for most MRI studies as the participant is not changing behaviour regularly, however, for fast changing behavioural decisions not so much. Paper: Coupling of activity, metabolism and behaviour across the Drosophila brain

## Ideas for thesis from open data

1. Explain the growth in recording fidelity (e.g. https://www.sciencedirect.com/science/article/pii/S0959438817303161?via%3Dihub - Steinmetz 2018)
2. A table of comparison is always nice.
3. In Siegle et al. Nature 2021, they used CA1, CA3 and DG units as controls because they have so many units. In this case, to check their visual responsivity pipeline. This is a another great use case of the larger scale data.
4. Integrate SIMURAN with tools like AllenSDK and ONE - they are the future, and I am going to use them so it is needed.

This idea of generating new discoveries from existing data is growing, for example see the allen [Neurodatarehack](https://alleninstitute.org/what-we-do/brain-science/events-training/2022-neurodatarehack-hackathon/) which includes opportunities for a year long Kavli foundation grant.

## From LFP papers

Bits from the discussion on the origin of LFP might be worth further discussing, how I see it as a byproduct - but it is of course not epiphenomenal, the electrical/chemical influence of these oscillations is certainly impactful on spiking. 

## Visualisations

- https://connectivity.brain-map.org/3d-viewer
- Inviwo
- Atlas.py in my connectivity paper code
- brainrender examples (mouse light api?) - http://ml-neuronbrowser.janelia.org/
- https://www-nature-com.elib.tcd.ie/articles/s41593-022-01041-5

## APIs

- brainglobe (morphapi, brainglobe-atlas)
- neuroM (blue brain)
- Allen SDK
- ONE (Open Neurophysiology Environment)

## Possible things to include in connectivity

1. Full calculations
2. Appendix images on calculation
3. Difference between considering full brain regions vs only considering the part in the probe.
4. Convergence rate of stats
5. Theoretical piece based around Anne and Konrad growth rate of neural recordings and the future.
6. Can include information on matrix stats for comparison.

## Software section

Include information about tools in the software section that are openly available to use.
Franklab similar ideas [SIMURAN](https://www.youtube.com/watch?v=KAMFt8-WFKo)
