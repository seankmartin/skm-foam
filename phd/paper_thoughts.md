---
tags: neuroscience
date: 2021--08--14
type: note
---

# Paper thoughts

I have read many more papers than this, but I did not keep the notes as cleanly.
If I see some of those that are important (they are in other computer docs, physical notebooks etc.) I will try to place here.

## Spontaneous behaviours drive multidimensional brainwise activity

authors: Stringer & Pachitariu et al.
keywords: Population, data, behaviour, mouse, CI, neuropixels
status: Read in some detail
importance: High
url: https://dx.doi.org/10.1126%2Fscience.aav7893

Very interesting article. Lots of analysis performed on thousands on cells, see [[open-data]] for description of data.
Some new-ish to me methods employed also. E.g. Peer prediction and SVCA.
Interesting hypothesis also that there exists a multidimensional representation of behaviour in visual cortex and that previously reported "noise" during stimulus presentations may in face be behaviourally driven.

## Towards the neural population doctrine

authors: Saxena and Cunningham
keywords: Population-level neuroscience, review
status: Read in detail
importance: Very high
url: https://doi.org/10.1016/j.conb.2019.02.002

Focuses on the results from population-level neuroscience, as opposed to the methodoligical details.
In this sense it is very important, as insights can be gained into where population-level science is advancing the field over more traditional levels of investigation.
Spefifically:

- Trial-to-trial variability in populations of neurons is a key indicator for behavioural states. This is probably the most interesting one to me.
- Decoding accuracy is more than the sum of its parts. I would have been surprised if this was not the case. Nonetheless 'mixed selectivity' would pretty much guarantee this. Some good theory available to generate null models of predictive ability for X dimensional neural data, e.g. Cunningham's previous work in around 2016/17.
- Analysis of neural activity over time reveals computational strategies. This one is the LFADS style state space representation of neural activity in a flow field. It is cool, and seems that activity over time in neural populations is seperable based on the task at hand.
- Nodes in ANNs emulate activity in CERTAIN regions of the brain. This is key, I don't think ANNs will work all over the brain, and I'm not even convinvced they will work when multiple regions are invovled. However, they do work in areas like VC, MC, and the retinal ganglion cells. However, there is a study using a CNN to model responses between inferior temporal cortex (IT) and V4 [Performance-optimized hierarchical models predict neural responses in higher visual cortex](https://www.pnas.org/content/111/23/8619) which was goal-directed not data-directed (but the data ended up being similar to the net).
- Finally, the perils of high-dimensional data and shedding light on the deabte about thwether theses analysses are actually producing novel findings about the brain, or if they are recepitulating old knowledge [Is population activity more than the sum of its parts? | Nature Neuroscience](https://www.nature.com/articles/nn.4627).

## Information-limiting correlations

authors: Moreno-Bote et al.
keywords: Correlation, information
status: Skimmed
importance: Medium-high
url: https://doi.org/10.1038/nn.3807

This article focuses on the so called "noise-correlations" (which I don't really like) - the correlations among neurons at a fixed stimulus. This is hardly noise though. However, the name mostly comes from the other correlation being labelled as signal correlation. The correlations among neurons with varying stimulus.
There is a reference at the end about signal correlations, which I feel there must be something more up to date than 2000s early.

One crucial thing the article suggests is that direct decoding is better than trying to estimate information when a population of neurons is available which were recorded simultaneously.
E.g. "These results have an important implication: the effect of attention
or perceptual learning on information in a particular area cannot be
assessed by simply measuring pairwise correlations. Thus, the fact
that pairwise correlations decrease when attention is engaged, which
has been observed in several studies 10,11 , cannot be taken as evidence
that information must have gone up, nor as a mechanism that can
explain any improved performance. The only way to determine the
true effect of correlations in these kinds of studies is to record from
large populations of neurons in parallel and decode the neural activity
with and without attention, or before and after perceptual learning."

## Large-scale neural recordings with single neuron resolution using Neuropixels probes in human cortex

authors: Paulk et al.
keywords: Neuropixels, recordings
status: Skimmed
importance: High
url: https://doi.org/10.1038/s41593-021-00997-0

Some key quotes "Overall, human electrophysiology technical capabilities have
substantially lagged what is possible in animals." (usually well below 150 units).
In this, they aimed at temporal lobe. (n = 3) with two in anasthesia, one awake. (n = 6 failed recordings).
Subjects don't seem to be recorded in tasks (understandably)

## A mechanism for inter-areal coherence through communication based on connectivity and oscillatory power

authors: Schneider et al.
keywords: LFP, coherence
status: Skimmed
importance: Medium
url: https://doi.org/10.1016/j.neuron.2021.09.037

Can be used to explaing coherence results as it relies on Connectivity and power.
Main takeaway, coherence alone not enough for communication.

## Does the brain care about average? A simple test

authors: Tlaie et al.
keywords: Analysis
status: Not read
importance: High
url: https://doi.org/10.1101/2021.11.28.469673

Should likely try to perform the same tests.

## Local field potentials reflect cortical population dynamics in a region-specific and frequency-dependent manner

authors: Gallego-Carracedo et al.
keywords: Analysis, LFP
status: Skimmed
importance: High
url: https://doi.org/10.1101/2021.11.28.469673

Very interesting, relationship between latent dynamics and LFP (since both are similar).
Actually some very cool stuff. Correlation depends a lot on frequency and no reliable relationship in "no acitvity" but during a task they were similar.
Very cool.

## Disentangling the flow of signals between populations of neurons

authors: Gokcen et al.
keywords: Analysis, flow
status: Skimmed
importance: High
url: https://doi.org/10.1101/2021.08.30.458230

Proposes delayed latents across groups to disentangle the direction of the latent interactions.
Similar to my interest in information flow and task performance.

[//begin]: # "Autogenerated link references for markdown compatibility"
[open-data]: ../projects/open-data "Open Data"
[//end]: # "Autogenerated link references"
