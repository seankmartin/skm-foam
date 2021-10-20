---
tags: PhD
date: 2021--10--18
type: note
---

# Open Data

The idea is to add value by analysing open data, this could most likely come from a combination of different data sources.
The sources below are also in my Zotero library under OpenData

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

## Papers

- What
- Recording modality
- Brain regions
- Species and age
- Conditions
- Availability
- Size
- Already known
- My questions

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

## Inspiration

- [10.1016/j.pneurobio.2012.09.004](https://www.sciencedirect.com/science/article/pii/S0301008212001505)
- Use Open Data in my Zotero.


## Ideas for thesis

1. Explain the growth in recording fidelity (e.g. https://www.sciencedirect.com/science/article/pii/S0959438817303161?via%3Dihub - Steinmetz 2018)
2. A table of comparison is always nice.
3. In Siegle et al. Nature 2021, they used CA1, CA3 and DG units as controls because they have so many units. In this case, to check their visual responsivity pipeline. This is a another great use case of the larger scale data.
4. Integrate SIMURAN with tools like AllenSDK and ONE - they are the future, and I am going to use them so it is needed.