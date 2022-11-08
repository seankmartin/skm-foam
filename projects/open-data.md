---
tags: PhD
date: 2021--10--18
type: note
---

# Open Data

The idea is to add value by analysing open data, this could most likely come from a combination of different data sources.
The sources below are also in my Zotero library under OpenData.

Some other sets here:
- https://gui.dandiarchive.org/#/dandiset/search?search=LFP and https://openneuro.org/ for LFP data etc.
- https://en.wikipedia.org/wiki/List_of_neuroscience_databases

## Allen 2022 visual behaviour npixels

[Whitepaper](https://brainmapportal-live-4cc80a57cd6e400d854-f7fdcae.divio-media.net/filer_public/f7/06/f706855a-a3a1-4a3a-a6b0-3502ad64680f/visualbehaviorneuropixels_technicalwhitepaper.pdf) and [data](https://allensdk.readthedocs.io/en/latest/visual_behavior_neuropixels.html)
Realistically this is the closes matching other dataset from [IBL](https://dandiarchive.org/dandiset/000045).

## Allen citation

Dataset: Allen Institute MindScope Program (2019). Allen Brain Observatory -- Neuropixels Visual Coding [dataset]. Available from brain-map.org/explore/circuits. Primary publication: Siegle, J. H., Jia, X., Durand, S., et al. (2021). Survey of spiking in the mouse visual system reveals functional hierarchy. Nature, 592(7612), 86-92. https://doi.org/10.1038/s41586-020-03171-x

## Fundamentals

We have the following types of data usually.

1. Neural data, e.g. MRI, LFP, spikes, calcium concentration
2. Sensory data, e.g. stimuli, environment
3. Behavior data, e.g. running speed, whisker movement, grooming etc.
4. Internal state e.g. hunger, interest etc.

1, 2 and 3 would be measurable.

### Train and test

To avoid having to create train and test data, it is possible that one dataset could be used for both.
This could be performed by splitting the data into chunks of train and test. For example in Stringer et al. 2019.
So Train -- Test -- Train -- Test ...

You can also test reliability by computing a particular measure on two separate parts of the recording.

## Hypotheses

### Increased spike count correlation decreases task perfomance

There already seems to be evidence for this. E.g. Rigotti et al. reference 19 *check in more detail from Cunningham towards the neural population doctrine.
Drawback - need to have data that involves tasks - measureable performance, not sure how many of these there are.
In theory though, this would work with any brain regions which is a big plus.
Also an interesting stroy and could be expanded to information theory past just correlation.
I would need to investigate how many studies look for neural corr, and if they claim it is "good" - as opposed to "bad" here.
Also this - claiming mixed selectivity is there https://www.sciencedirect.com/science/article/pii/S0959438816000118.

Essentially, what I think this would boil down to is that signal correlations reduce task performance.
However, there is much discussion on this, so it is a large topic (which is both good and bad).
The most discussion is around correlation, information, redundancy, probability (Bayesian and frequentist), and a bit of decoding.

This could actually be very important [Different population dynamics in the supplementary motor area and motor cortex during reaching](https://academiccommons.columbia.edu/doi/10.7916/d8-0a1x-7b98)

- They show that on a single neuron level, the responses from supplementary motor area and motor cortex are similar but on a population level they appear to be performing different functions.
- Remember the proposed relationship (by me, but seems pretty clear) - that correlation increase, decreases the dimensionality of the neural representation. As such papers that discuss dimensionality and task performance also investigate the same thing, such as [The importance of mixed selectivity in complex cognitive tasks | Nature](https://www.nature.com/articles/nature12160). Note that this paper has an absolutely massive suplemental material associated with it.

Note on the topic of correlations, [Correlations and Neuronal Population Information | Annual Review of Neuroscience](https://www.annualreviews.org/doi/10.1146/annurev-neuro-070815-013851) has a good description of the different correlations usually used in neuroscience.
"Work in the past few decades has greatly advanced our understanding of how neuronal popu-
lation information is influenced by correlations. Theoretical work has been instrumental in this
progress. It has shown us that some forms of correlations limit information, whereas others do
not. At least in the context of population information, theoretical progress has also revealed that
simply characterizing response statistics can have limited value: Describing correlations does not
translate into understanding information, as the largest correlations do not necessarily have the
strongest effect on information. We view this progress as a cautionary tale because we are entering
an era when our power to measure brain activity is exploding, while our conceptual frameworks
remain underdeveloped. Our situation is perhaps analogous to pre-Newtonian physics, which
attempted to understand the movements of the stars and planets through extremely careful and
detailed measurements. Ultimately, however, orbits were understood in a straightforward way
with Newtonian physics. We see a risk that we—like pre-Newtonian physicists, but abetted by
much more powerful instrumentation—will drown in a sea of description, measuring and char-
acterizing population activity patterns rather than understanding the computations and functions
they underlie."

**Papers:**

- [Information-limiting correlations | Nature Neuroscience](https://www.nature.com/articles/nn.3807)
- [Correlated neuronal discharge rate and its implications for psychophysical performance | Nature](https://www.nature.com/articles/370140a0)
- [Redundancy reduction revisited](https://www.tandfonline.com/doi/abs/10.1080/net.12.3.241.253)
- [Neural correlations, population coding and computation | Nature Reviews Neuroscience](https://www.nature.com/articles/nrn1888)
- [Correlations enhance the behavioral readout of neural population activity in association cortex | Nature Neuroscience](https://www.nature.com/articles/s41593-021-00845-1)
- [Good decisions require more than information | Nature Neuroscience](https://www.nature.com/articles/s41593-021-00883-9)
- [Correlations and Neuronal Population Information | Annual Review of Neuroscience](https://www.annualreviews.org/doi/10.1146/annurev-neuro-070815-013851)
- [Learning and attention reveal a general relationship between population activity and behavior](https://doi.org/10.1126/science.aao0284)

### Population dynamics are similar between brain regions as long as they have reasonably similar stuctural connectivity.

Essentially, this would be claiming that neural activity really is dominated by structural activity.
It makes sense on a base level, as does the previous hypothesis.
Big plus is that almost anything could be used, but I don't really know if there is much support on this.

### Systems level hypothesis

This one would be a bit TBD, but pick my favourite brain regions/ data avaiable in my favourite tasks with my favourite hypothesis about this.
It would be delving a lot into a specific thing.

### Distinct processes occupy different space in flow field

Individual distinct tasks occupy different spaces in a flow field of neural activity e.g. LFADS.

### ANNs similar to real network

ANNs are either goal driven (get a network to produce the outcome, but don't care too much about the underlying structure). For example as in Sussilo's work, where you check the dynamics after training a net.
This has been employed on retinal ganglion cells and also in PMC (primary motor cortex).
Or they are data driven, whereby you attempt to capture each neuron in the ANN (e.g. Paninski's work).

### Neuron groupings by brain area are meaningful

In terms of just functional groupings from a matrix of spiking activity, an automatic algorithm could estimate which neurons are from different brain areas.
This would seem to agree with Semedo 2014 - extracting latent structure.

## Other lists

- https://www.nwb.org/example-datasets/
- https://github.com/openlists/ElectrophysiologyData

## Research strategy

1. Previous papers that I am aware of.
2. Citations to Neuropixels 1 and 2 that make recordings.
3. Connected papers.com to Neuropixels 2.

## Requirements

1. What data sources are available?
2. How can I access these?
3. How much storage will I need?
4. What has already been determined from this data?
5. What would I like to investigate in this data?

## Topics

- What
- Recording modality
- Brain regions
- Species and age
- Conditions
- Availability
- Size
- Already known
- My questions

## Non-human data

### Stringer et al. Science 2019

- Around 10,000 neurons in VC with facial movements with 3000 across brain with eight Npixel probes.

### NeuroSeeker probe

- Seems that all might be available is this http://www.kampff-lab.org/cmos-scanning/ but need to look more.

### Neuropixels 1.0 and 2.0

- I think there is some introductory recordings presented with the probe release papers.
- Yes, 2.0 has data here https://figshare.com/articles/dataset/_Imposed_motion_datasets_from_Steinmetz_et_al_Science_2021/14024495

### Carandini work

- Check what Carandini and Harris have that is not on IBL.
- https://figshare.com/articles/dataset/Dataset_from_Steinmetz_et_al_2019/9598406
- https://rdr.ucl.ac.uk/authors/Matteo_Carandini/6778853
- https://www.biorxiv.org/search/%20author1%3Acarandini%20author2%3Aharris%20numresults%3A75%20sort%3Apublication-date%20direction%3Adescending%20format_result%3Astandard

### Siegle et al. Nature 2021

- Tens of thousands of neurons in six cortical and two thalamic regions.
- Npixel probes
- Visual (V1, LM, AL, RL, AM, PM) and Thalamic (LGN, LP)
- Mice, about 117 days old
- Responding to visual stimuli.
- Allen Brain Observatory ([AllenSDK](https://allensdk.readthedocs.io), [DANDI](https://allensdk.readthedocs.io), [Registry of Open data on AWS](https://registry.opendata.aws/)). See [docs](http://help.brain-map.org/display/observatory/Documentation) for some help.
- Up to 1TB
- Functional connectivity reflects a previously performed hierarchy suggested by anatomical tracing. Used CCG time-lag analysis to estimate this.
- Could I tie visual processing into area I am more interested in?

### de Vries et al. Nat Neuro 2019

- 60,000 neurons from six visual areas, four layers
- In vivo two-photon calcuim imaging
- Visual
- Mice, 12 transgenic lines, 243 of them.
- Allen Brain Observatory
- Was compared to results from Siegle et al. Nature 2021 in [Siegle et al. Elife 2021](https://elifesciences.org/articles/69068). Some extra data resulted from this on [Zenodo](https://zenodo.org/record/5090747#.YW_2MhrMKUk).
- In line with my other research, most neurons they recored (34%) respond to nothing reliably. In general they are classifying neurons, predicting behaviour etc.

### IBL, Bonacchi et al. BioRxiv 2020

- IBL has a large repository of sharing data.
- Npixel probes
- Open Neurophysiology Environment [One](https://int-brain-lab.github.io/iblenv/notebooks_external/one_quickstart.html). Seems some data also on [Alyx](https://alyx.readthedocs.io/en/latest/).
- Explore what is available - many opportunities here!

## DANDI archive

- https://gui.dandiarchive.org/#/dandiset/000037
- https://gui.dandiarchive.org/#/dandiset/000045
- https://gui.dandiarchive.org/#/dandiset/000022
- https://gui.dandiarchive.org/#/dandiset/000061
- https://gui.dandiarchive.org/#/dandiset/000115

## Human data

- Difficulty https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0166598
- From this, recordings are long and noisy.
- Most recordings are performed in epileptic patients - and as such are in the MTL (HC, amyg, EC, PHC).
- Parkinson's is another, but DBS

### Fedele et al. Nature 2021

- https://www.nature.com/articles/s41597-020-00790-x?sf241908532=1
- Recordings performed in humans in the amygdala in 9 patients iEEG and single-neuron recordings.
- Movies (horror) presented for fear response.

### Rey et al. Current Bio 2020

- https://doi.org/10.1016/j.cub.2020.01.035
- Recordings in MTL (Medial Temporal Lobe)
- From 450 units recording, only 35 could be used - 16 in Amygdala and 19 from HC.

## Inspiration

- [10.1016/j.pneurobio.2012.09.004](https://www.sciencedirect.com/science/article/pii/S0301008212001505) - the writing is a bit dense, but the idea is interesting.
- https://elifesciences.org/articles/61277/executable
- Use Open Data in my Zotero.

## Ideas for study

1. Measure population activity in different states across these datasets. Describe the population and the difference in tasks, very much akin to Humpries 2012 on single cells.
2. Population dynamics.

## Essence

So going back to basics, the interest is communication / interaction between neurons and brain regions.
Options would include population dynamics in different regions and their impact, or in the same regions, or perhaps new methods. However, I think the latter would come out most naturally from trying to actually do a large open data experiment.
So if we think of LFADS, that would be one option to do something similar.

How to start at this and make a prototype style for this.

1. Create a new git repository.
2. Start to describe how to download the data within this repository.
3. Create figure folders.
4. So in the best case, I would have metadata to work with, and can start to describe.
5. From there I can do basic descriptive statistics.
6. At this point I should be able to form solid hypotheses, however I should be able to start thinking about these already - just ideas not formalised.
7. From there I can start to gather the analyses that could be used to test these hypotheses, and perhaps find the gaps that might exist.
8. Analysis time! Any developed methods should be verified elsewhere, and perhaps presented separately.